import type { APIRoute } from "astro";

export const GET: APIRoute = ({ site }) => {
  const base = import.meta.env.BASE_URL.replace(/^\/|\/$/g, "");
  const sitemapPath = base
    ? `${base}/sitemap-index.xml`
    : "sitemap-index.xml";
  const sitemapURL = new URL(sitemapPath, site).toString();
  return new Response(`User-agent: *\nAllow: /\nSitemap: ${sitemapURL}\n`, {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
};
