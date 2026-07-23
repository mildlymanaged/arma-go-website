import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";

const site = process.env.SITE_URL || "https://armago.me";
const base = process.env.BASE_PATH || "/";

export default defineConfig({
  site,
  base,
  output: "static",
  trailingSlash: "always",
  integrations: [
    sitemap({
      filter: (page) =>
        ![
          "/privacy-policy/",
          "/terms-and-conditions/",
          "/refund-cancellation-policy/",
        ].some((route) => page.endsWith(route)),
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
});
