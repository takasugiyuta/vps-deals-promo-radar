import { loadArticles, readArticle, searchArticles } from "./shared.js";

const PROTOCOL_VERSION = "2025-11-25";
const CORS = {
  "access-control-allow-origin": "*",
  "access-control-allow-methods": "GET, POST, OPTIONS",
  "access-control-allow-headers": "content-type, accept, mcp-protocol-version, mcp-session-id",
};
const TOOLS = [
  {
    name: "search_articles",
    description: "Search published Lumafare VPS articles. Preserve source links and dates; do not infer missing facts.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", minLength: 1, maxLength: 200 },
        limit: { type: "integer", minimum: 1, maximum: 10 },
      },
      required: ["query"],
      additionalProperties: false,
    },
  },
  {
    name: "read_article",
    description: "Read one published Lumafare article by exact slug; return its source URLs and publication date.",
    inputSchema: {
      type: "object",
      properties: { slug: { type: "string", pattern: "^[a-z0-9]+(?:-[a-z0-9]+)*$" } },
      required: ["slug"],
      additionalProperties: false,
    },
  },
];

function response(body, status = 200) {
  return new Response(body === null ? null : JSON.stringify(body), {
    status,
    headers: { ...CORS, "content-type": "application/json; charset=utf-8", "mcp-protocol-version": PROTOCOL_VERSION },
  });
}

function rpcError(id, code, message) {
  return response({ jsonrpc: "2.0", id: id ?? null, error: { code, message } }, code === -32700 ? 400 : 200);
}

export async function onRequest({ request, env }) {
  if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: CORS });
  if (request.method === "GET") return new Response("This stateless MCP endpoint accepts JSON-RPC POST requests.", { status: 405, headers: { ...CORS, allow: "POST, OPTIONS", "content-type": "text/plain; charset=utf-8" } });
  if (request.method !== "POST") return new Response("Method not allowed.", { status: 405, headers: { ...CORS, allow: "POST, OPTIONS", "content-type": "text/plain; charset=utf-8" } });

  const accept = request.headers.get("accept") || "application/json";
  if (!accept.includes("application/json") && !accept.includes("*/*")) return new Response("This endpoint returns JSON, not an event stream.", { status: 406, headers: CORS });

  let rpc;
  try {
    const text = await request.text();
    if (text.length > 65536) return rpcError(null, -32600, "Request is too large.");
    rpc = JSON.parse(text);
  } catch {
    return rpcError(null, -32700, "Parse error.");
  }
  if (!rpc || rpc.jsonrpc !== "2.0" || typeof rpc.method !== "string") return rpcError(rpc?.id, -32600, "Invalid Request.");
  const id = Object.hasOwn(rpc, "id") ? rpc.id : undefined;
  if (rpc.method.startsWith("notifications/")) return new Response(null, { status: 202, headers: CORS });
  if (id === undefined) return rpcError(null, -32600, "A request id is required.");

  if (rpc.method === "initialize") {
    return response({
      jsonrpc: "2.0", id,
      result: {
        protocolVersion: PROTOCOL_VERSION,
        capabilities: { tools: { listChanged: false } },
        serverInfo: { name: "com.lumafare/articles", version: "1.0.0" },
        instructions: "Read-only search and exact-slug reading for published public articles. Preserve source URLs and dates; unknown facts remain unknown.",
      },
    });
  }
  if (rpc.method === "ping") return response({ jsonrpc: "2.0", id, result: {} });
  if (rpc.method === "tools/list") return response({ jsonrpc: "2.0", id, result: { tools: TOOLS } });
  if (rpc.method !== "tools/call") return rpcError(id, -32601, "Method not found.");

  const name = rpc.params?.name;
  const args = rpc.params?.arguments;
  if (!args || typeof args !== "object" || Array.isArray(args)) return rpcError(id, -32602, "Tool arguments must be an object.");
  const articles = await loadArticles(env.ASSETS);
  if (name === "search_articles") {
    if (typeof args.query !== "string" || !args.query.trim() || args.query.length > 200 || (args.limit !== undefined && (!Number.isInteger(args.limit) || args.limit < 1 || args.limit > 10))) {
      return rpcError(id, -32602, "Invalid query or result limit.");
    }
    const result = searchArticles(articles, args.query, args.limit);
    return response({ jsonrpc: "2.0", id, result: { content: [{ type: "text", text: JSON.stringify({ query: args.query, count: result.length, results: result }) }] } });
  }
  if (name === "read_article") {
    if (typeof args.slug !== "string" || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(args.slug)) return rpcError(id, -32602, "Invalid article slug.");
    const article = readArticle(articles, args.slug);
    const result = article
      ? { content: [{ type: "text", text: JSON.stringify(article) }] }
      : { content: [{ type: "text", text: JSON.stringify({ error: "article_not_found", slug: args.slug }) }], isError: true };
    return response({ jsonrpc: "2.0", id, result });
  }
  return rpcError(id, -32602, "Unknown tool.");
}
