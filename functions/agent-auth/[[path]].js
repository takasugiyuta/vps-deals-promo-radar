export async function onRequest() {
  return new Response(JSON.stringify({
    status: "under_construction",
    available: false,
    capabilities_status: "planned_contract_only",
    error: "temporarily_unavailable",
    error_description: "Authentication is not available. Use the public read-only article lookup service.",
  }), { status: 503, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", "x-robots-tag": "noindex" } });
}
