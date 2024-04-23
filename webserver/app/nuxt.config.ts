// https://nuxt.com/docs/api/configuration/nuxt-config
import { defineNuxtConfig } from 'nuxt/config'
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ['~/assets/css/main.css',
    '~/assets/css/bootstrap.min.css'
  ],
  app: {
    head: {
      title: "対話型Q&A Chatbot",
      meta: [
        { charset: "utf-8" },
        { name: "viewport", content: "width=device-width, initial-scale=1" },
      ],
      script: [
        { src: '/bootstrap.min.js' },
        { src: '/jquery.min.js' }
      ],
    }
  }
})
