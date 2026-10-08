function htmlToMarkdown(html) {
  return html
    .replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, "")
    .replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi, "")
    .replace(/<nav\b[^>]*>\s*<a[^>]*href=["']\/["'][^>]*>Home<\/a>[\s\S]*?<\/nav>/gi, "")
    .replace(/<a\b[^>]*href=["']([^"']+)["'][^>]*>([\s\S]*?)<\/a>/gi, "[$2]($1)")
    .replace(/<h1\b[^>]*>([\s\S]*?)<\/h1>/gi, "\n# $1\n")
    .replace(/<h2\b[^>]*>([\s\S]*?)<\/h2>/gi, "\n## $1\n")
    .replace(/<h3\b[^>]*>([\s\S]*?)<\/h3>/gi, "\n### $1\n")
    .replace(/<li\b[^>]*>([\s\S]*?)<\/li>/gi, "\n- $1")
    .replace(/<br\s*\/?\s*>/gi, "\n")
    .replace(/<\/(p|section|article|ul|ol|main|header|footer|div)>/gi, "\n\n")
    .replace(/<[^>]+>/g, "")
    .replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"').replace(/&#39;|&apos;/g, "'").replace(/&nbsp;/g, " ")
    .replace(/[ \t]+\n/g, "\n").replace(/\n{3,}/g, "\n\n").trim() + "\n";
}

export async function onRequest({ request, next }) {
  const response = await next();
  const headers = new Headers(response.headers);
  headers.append("Vary", "Accept");
  if (new URL(request.url).pathname === "/") {
    headers.set("Link", '<https://lumafare.com/.well-known/api-catalog>; rel="api-catalog"; type="application/linkset+json", <https://lumafare.com/openapi.json>; rel="service-desc"; type="application/vnd.oai.openapi+json", <https://lumafare.com/ai/>; rel="service-doc"; type="text/html"');
  }
  if (!request.headers.get("accept")?.toLowerCase().includes("text/markdown") ||
      !/^\/(?:$|articles\/[^/]+\/?$)/.test(new URL(request.url).pathname)) {
    return new Response(response.body, { status: response.status, statusText: response.statusText, headers });
  }
  if (!response.headers.get("content-type")?.includes("text/html")) return response;
  headers.set("content-type", "text/markdown; charset=utf-8");
  headers.set("cache-control", "no-store");
  headers.delete("content-length");
  headers.delete("content-encoding");
  headers.delete("etag");
  return new Response(htmlToMarkdown(await response.text()), { status: response.status, headers });
}
