import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tsconfigPaths from "vite-tsconfig-paths";
import tailwindcss from "@tailwindcss/vite";

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    tsconfigPaths({
      root: "./",
      projects: ["./tsconfig.app.json"],
    }),
    tailwindcss(),
  ],
  resolve: {
    alias: {
      "@": "/src",
      "@components": "/src/components",
      "@pages": "/src/pages",
      "@services": "/src/services",
      "@constants": "/src/constants",
      "@definitions": "/src/definitions",
      "@types": "/src/types",
      "@router": "/src/router",
      "@validators": "/src/validators",
      "@utils": "/src/utils",
      "@modules": "/src/modules",
    },
  },
});
