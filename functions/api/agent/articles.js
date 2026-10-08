import { json, loadArticles, readArticle, searchArticles } from "../../shared.js";

export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  const articles = await loadArticles(env.ASSETS);
  const slug = url.searchParams.get("slug");
  if (slug !== null) {
    if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug)) return json({ error: "invalid_slug" }, 400, { "access-control-allow-origin": "*" });
    const article = readArticle(articles, slug);
    if (!article) return json({ error: "article_not_found", slug }, 404, { "access-control-allow-origin": "*" });
    const { body, ...metadata } = article;
    return json({ ...metadata, body }, 200, { "access-control-allow-origin": "*" });
  }
  const query = url.searchParams.get("q") || "";
  if (query.length > 200) return json({ error: "query_too_long", max_length: 200 }, 400, { "access-control-allow-origin": "*" });
  const results = searchArticles(articles, query, url.searchParams.get("limit"));
  return json({ query, count: results.length, results }, 200, { "access-control-allow-origin": "*" });
}
