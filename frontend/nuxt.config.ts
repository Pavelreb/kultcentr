export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@pinia/nuxt', '@nuxtjs/tailwindcss'],
  css: ['~/assets/css/main.css'],
  runtimeConfig: {
    public: {
      apiBase: 'http://127.0.0.1:8000/api'
    }
  },
  app: {
    head: {
      htmlAttrs: { lang: 'ru' },
      title: 'Центр Культуры',
      titleTemplate: '%s — Центр Культуры',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content: 'Центр культуры: афиша мероприятий, публикации, фотогалерея и авторы. Будьте в курсе культурной жизни.'
        },
        { property: 'og:type', content: 'website' },
        { property: 'og:site_name', content: 'Центр Культуры' },
        {
          property: 'og:description',
          content: 'Центр культуры: афиша мероприятий, публикации, фотогалерея и авторы.'
        }
      ],
      link: [
        { rel: 'icon', type: 'image/png', href: '/favicon.png' },
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }
      ]
    }
  }
})