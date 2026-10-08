const DATA_PATH = "/agent-articles.json";

export async function loadArticles(assets) {
  const response = await assets.fetch(new URL(DATA_PATH, "https://lumafare.com"));
  if (!response.ok) throw new Error("Article index is unavailable");
  const value = await response.json();
  return Array.isArray(value.articles) ? value.articles : [];
}

export function searchArticles(articles, query, limit = 5) {
  const terms = String(query || "").trim().toLowerCase().split(/\s+/).filter(Boolean).slice(0, 12);
  if (!terms.length) return [];
  return articles
    .map((article) => {
      const haystack = `${article.title} ${article.description} ${article.question || ""} ${article.body}`.toLowerCase();
      const score = terms.reduce((sum, term) => sum + (haystack.includes(term) ? 1 : 0), 0);
      return { article, score };
    })
    .filter(({ score }) => score > 0)
    .sort((a, b) => b.score - a.score || a.article.title.localeCompare(b.article.title))
    .slice(0, Math.max(1, Math.min(Number(limit) || 5, 10)))
    .map(({ article }) => ({
      slug: article.slug,
      title: article.title,
      description: article.description,
      question: article.question || null,
      url: article.url,
      source_url: article.sources[0] || null,
      published: article.date,
    }));
}

export function readArticle(articles, slug) {
  return articles.find((article) => article.slug === slug) || null;
}

export function json(data, status = 200, extraHeaders = {}) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", ...extraHeaders },
  });
}
