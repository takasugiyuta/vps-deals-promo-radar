import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import { onRequestGet } from "../functions/api/agent/articles.js";
import { onRequest as mcpRequest } from "../functions/mcp.js";
import { onRequestPost as a2aPost } from "../functions/a2a.js";
import { onRequest as middleware } from "../functions/_middleware.js";
import { onRequest as authStub } from "../functions/agent-auth/[[path]].js";

const articleJson = await readFile(new URL("../site/agent-articles.json", import.meta.url), "utf8");
const env = { ASSETS: { fetch: async () => new Response(articleJson, { headers: { "content-type": "application/json" } }) } };

function mcp(method, params = {}, id = 1) {
  return new Request("https://lumafare.com/mcp", {
    method: "POST", headers: { "content-type": "application/json", accept: "application/json, text/event-stream" },
    body: JSON.stringify({ jsonrpc: "2.0", id, method, params }),
  });
}

test("article API supports bounded search, exact read and 404", async () => {
  const search = await onRequestGet({ request: new Request("https://lumafare.com/api/agent/articles?q=VPS+billing&limit=2"), env });
  const found = await search.json();
  assert.equal(search.status, 200);
  assert.equal(found.count, 1);
  assert.equal(found.results[0].slug, "compare-vps-deals-total-cost");
  assert.ok(found.results[0].source_url.startsWith("https://"));
  const read = await onRequestGet({ request: new Request("https://lumafare.com/api/agent/articles?slug=compare-vps-deals-total-cost"), env });
  assert.match((await read.json()).body, /renewal/i);
  const missing = await onRequestGet({ request: new Request("https://lumafare.com/api/agent/articles?slug=missing-entry"), env });
  assert.equal(missing.status, 404);
  const empty = await onRequestGet({ request: new Request("https://lumafare.com/api/agent/articles?q=nonexistenttoken"), env });
  assert.equal((await empty.json()).count, 0);
});

test("MCP JSON-RPC initializes, lists tools, searches and reads", async () => {
  const initialized = await mcpRequest({ request: mcp("initialize", { protocolVersion: "2025-11-25", capabilities: {}, clientInfo: { name: "test", version: "1" } }), env });
  const initBody = await initialized.json();
  assert.equal(initBody.result.protocolVersion, "2025-11-25");
  assert.equal(initialized.headers.get("mcp-protocol-version"), "2025-11-25");
  const listed = await mcpRequest({ request: mcp("tools/list"), env });
  assert.deepEqual((await listed.json()).result.tools.map((tool) => tool.name).sort(), ["read_article", "search_articles"]);
  const found = await mcpRequest({ request: mcp("tools/call", { name: "search_articles", arguments: { query: "VPS billing" } }), env });
  assert.match((await found.json()).result.content[0].text, /compare-vps-deals-total-cost/);
  const read = await mcpRequest({ request: mcp("tools/call", { name: "read_article", arguments: { slug: "compare-vps-deals-total-cost" } }), env });
  assert.match((await read.json()).result.content[0].text, /https:\/\//);
  const missing = await mcpRequest({ request: mcp("tools/call", { name: "read_article", arguments: { slug: "not-published" } }), env });
  assert.equal((await missing.json()).result.isError, true);
  const invalid = await mcpRequest({ request: mcp("tools/call", { name: "read_article", arguments: { slug: "../private" } }), env });
  assert.equal((await invalid.json()).error.code, -32602);
});

test("A2A JSON-RPC returns completed search and exact-article tasks", async () => {
  const send = async (id, text) => a2aPost({ request: new Request("https://lumafare.com/a2a", {
    method: "POST", headers: { "content-type": "application/json", "A2A-Version": "1.0" },
    body: JSON.stringify({ jsonrpc: "2.0", id, method: "SendMessage", params: { message: { messageId: `message-${id}`, role: "ROLE_USER", parts: [{ text }] } } }),
  }), env });
  const response = await send("a2a-search", "VPS billing");
  const body = await response.json();
  assert.equal(response.status, 200);
  assert.equal(body.id, "a2a-search");
  assert.equal(body.result.task.status.state, "TASK_STATE_COMPLETED");
  assert.match(body.result.task.artifacts[0].parts[0].text, /compare-vps-deals-total-cost/);
  const read = await (await send("a2a-read", "read compare-vps-deals-total-cost")).json();
  assert.match(read.result.task.artifacts[0].parts[0].text, /https:\/\//);
  const invalid = await a2aPost({ request: new Request("https://lumafare.com/a2a", { method: "POST", headers: { "content-type": "application/json" }, body: "{}" }), env });
  assert.equal((await invalid.json()).error.code, -32600);
});

test("Markdown negotiation preserves HTML and varies by Accept; auth stays construction-only", async () => {
  const html = "<!doctype html><html><body><main><h1>VPS deals</h1><p>Read <a href='/articles/example/'>this article</a>.</p></main></body></html>";
  const next = async () => new Response(html, { headers: { "content-type": "text/html; charset=utf-8" } });
  const ordinary = await middleware({ request: new Request("https://lumafare.com/"), next });
  const markdown = await middleware({ request: new Request("https://lumafare.com/", { headers: { accept: "text/markdown" } }), next });
  assert.match(ordinary.headers.get("vary"), /Accept/);
  assert.match(ordinary.headers.get("link"), /rel="api-catalog"/);
  assert.match(ordinary.headers.get("content-type"), /text\/html/);
  assert.match(markdown.headers.get("content-type"), /text\/markdown/);
  assert.match(await markdown.text(), /\[this article\]\(\/articles\/example\/\)/);
  const auth = await authStub();
  assert.equal(auth.status, 503);
  assert.equal(auth.headers.get("cache-control"), "no-store");
  assert.equal((await auth.json()).available, false);
});

test("discovery resources are valid and the skill digest matches served bytes", async () => {
  const skillBytes = await readFile(new URL("../site/ai/skills/site-lookup/SKILL.md", import.meta.url));
  const index = JSON.parse(await readFile(new URL("../site/.well-known/agent-skills/index.json", import.meta.url), "utf8"));
  assert.equal(index.skills[0].digest, `sha256:${createHash("sha256").update(skillBytes).digest("hex")}`);
  const card = JSON.parse(await readFile(new URL("../site/.well-known/agent-card.json", import.meta.url), "utf8"));
  assert.equal(card.supportedInterfaces[0].url, "https://lumafare.com/a2a");
  assert.equal(card.skills[0].id, "site-lookup");
  const catalog = JSON.parse(await readFile(new URL("../site/.well-known/ai-catalog.json", import.meta.url), "utf8"));
  assert.ok(catalog.entries.length >= 3);
  const robots = await readFile(new URL("../site/robots.txt", import.meta.url), "utf8");
  assert.match(robots, /^Content-Signal: search=yes, ai-input=yes, ai-train=no$/m);
  const auth = await readFile(new URL("../site/auth.md", import.meta.url), "utf8");
  assert.match(auth, /^# auth\.md$/m);
  assert.match(auth, /^## Agent Registration$/m);
  assert.match(auth, /registration_available: false/);
  assert.match(auth, /anonymous_registration: planned only; not available/);
  assert.match(auth, /do not call the registration endpoint/i);
  assert.match(auth, /HTTP 503/);
  const sitemap = await readFile(new URL("../site/sitemap.xml", import.meta.url), "utf8");
  assert.equal((sitemap.match(/<url>/g) || []).length, 12);
  const redirects = await readFile(new URL("../site/_redirects", import.meta.url), "utf8");
  assert.equal((redirects.match(/ 301$/gm) || []).length, 5);
});
