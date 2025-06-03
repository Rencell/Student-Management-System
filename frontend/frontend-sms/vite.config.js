import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  base : '/Student-Management-System/',
  plugins: [
    vue(),
    vueDevTools(),
    tailwindcss()
  ],
  
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },

  server: {
    proxy: {
      '/dj-rest-auth': {
        target: 'https://student-management-system-rmww.onrender.com', 
        changeOrigin: true,
      },
      '/api': {
        target: 'https://student-management-system-rmww.onrender.com', 
        changeOrigin: true,
      },
    }
  }
})
