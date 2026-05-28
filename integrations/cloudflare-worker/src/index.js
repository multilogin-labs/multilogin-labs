/**
 * Multilogin Labs · Cloudflare Worker
 *
 * Routes:
 *   GET /              → bounces to GitHub Pages hub
 *   GET /go            → 302 to partner pricing (UTM preserved)
 *   GET /search?q=...  → JSON of matching endpoints
 *   GET /endpoints     → cached endpoints.json (1h)
 *   GET /docs/<slug>   → 302 to docs/api/endpoints/<slug>.md on GitHub
 */
const CACHE_TTL = 60 * 60;

export default {
  async fetch(req, env, ctx) {
    const url = new URL(req.url);
    const path = url.pathname.replace(/\/$/, "");

    if (path === "" || path === "/") {
      return Response.redirect("https://multilogin-labs.github.io/multilogin-labs/", 302);
    }
    if (path === "/go") {
      return Response.redirect(env.PARTNER_URL, 302);
    }
    if (path === "/swagger") {
      return Response.redirect(
        "https://multilogin-labs.github.io/multilogin-labs/api/swagger.html",
        302,
      );
    }
    if (path === "/calculator") {
      return Response.redirect(
        "https://multilogin-labs.github.io/multilogin-labs/calculator.html",
        302,
      );
    }
    if (path.startsWith("/docs/")) {
      const slug = path.slice("/docs/".length).replace(/\.md$/, "");
      return Response.redirect(
        `https://github.com/multilogin-labs/multilogin-labs/blob/main/docs/api/endpoints/${slug}.md`,
        302,
      );
    }

    if (path === "/endpoints") {
      const data = await fetchEndpoints(env, ctx);
      return Response.json(data, {
        headers: corsHeaders(),
      });
    }

    if (path === "/search") {
      const q = (url.searchParams.get("q") || "").toLowerCase();
      const data = await fetchEndpoints(env, ctx);
      const hits = data.filter(
        (e) =>
          !q ||
          e.name.toLowerCase().includes(q) ||
          e.url.toLowerCase().includes(q) ||
          e.category.toLowerCase().includes(q),
      );
      return Response.json(hits.slice(0, 30), { headers: corsHeaders() });
    }

    return new Response("Not found", { status: 404 });
  },
};

async function fetchEndpoints(env, ctx) {
  const res = await fetch(env.ENDPOINTS_URL, {
    cf: { cacheTtl: CACHE_TTL, cacheEverything: true },
  });
  return res.json();
}

function corsHeaders() {
  return {
    "Access-Control-Allow-Origin": "*",
    "Cache-Control": `public, max-age=${CACHE_TTL}`,
    "Content-Type": "application/json",
  };
}
