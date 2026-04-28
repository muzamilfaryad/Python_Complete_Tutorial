import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
// Tailwind should be configured via PostCSS (postcss.config.cjs) and CSS imports.
// Do not import '@tailwindcss/vite' here — that package is not a valid Vite entry.
// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
})
