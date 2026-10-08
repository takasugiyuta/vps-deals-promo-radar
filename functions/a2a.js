import { loadArticles, readArticle, searchArticles } from "./shared.js";

const CORS = {
  "access-control-allow-origin": "*",
  "access-control-allow-methods": "POST, OPTIONS",
  "access-control-allow-headers": "content-type, a2a-version",
};

function jsonRpc(body, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: { ...CORS, "content-type": "application/json; charset=utf-8" } });
}

function error(id, code, message) {
  return jsonRpc({ jsonrpc: "2.0", id: id ?? null, error: { code, message } }, code === -32700 ? 400 : 200);
}

function answerFor(query, articles) {
  const readMatch = query.match(/^(?:read|open)\s+([a-z0-9]+(?:-[a-z0-9]+)*)$/i);
  if (readMatch) {
    const article = readArticle(articles, readMatch[1]);
    return article
      ? JSON.stringify({ article, instruction: "Cite the article URL and its source URLs. Unknown facts remain unknown." })
      : JSON.stringify({ results: [], message: "No published article exists for that slug." });
  }
  const results = searchArticles(articles, query, 5);
  return results.length
    ? JSON.stringify({ results, instruction: "Use these published pages and cite their URLs. Unknown facts remain unknown." })
    : JSON.stringify({ results: [], message: "No published article matched this request." });
}

export async function onRequestPost({ request, env }) {
  let rpc;
  try {
    const text = await request.text();
    if (text.length > 65536) return error(null, -32600, "Request is too large.");
    rpc = JSON.parse(text);
  } catch {
    return error(null, -32700, "Parse error.");
  }
  const id = rpc?.id;
  if (!rpc || rpc.jsonrpc !== "2.0" || typeof rpc.method !== "string" || id === undefined) return error(id, -32600, "Invalid Request.");
  if (rpc.method !== "SendMessage") return error(id, -32601, "Method not found.");

  const message = rpc.params?.message;
  if (!message || message.role !== "ROLE_USER" || !Array.isArray(message.parts)) return error(id, -32602, "SendMessage requires a user message with parts.");
  const query = message.parts.map((part) => typeof part?.text === "string" ? part.text : "").filter(Boolean).join(" ").trim();
  if (!query) return error(id, -32602, "The message must contain text.");
  if (query.length > 200) return error(id, -32602, "The message is too long; maximum length is 200 characters.");

  const reply = answerFor(query, await loadArticles(env.ASSETS));
  const task = {
    id: crypto.randomUUID(),
    contextId: message.contextId || crypto.randomUUID(),
    status: { state: "TASK_STATE_COMPLETED", timestamp: new Date().toISOString() },
    artifacts: [{
      artifactId: crypto.randomUUID(),
      name: "public-article-results",
      parts: [{ text: reply }],
    }],
  };
  return jsonRpc({ jsonrpc: "2.0", id, result: { task } });
}

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS });
}
