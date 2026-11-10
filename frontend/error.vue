<!-- frontend/error.vue -->
<!-- Страница ошибки (404 и др.). Рендерится вне основного layout -->
<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900 px-4 transition-colors duration-200">
    <div class="text-center max-w-lg">

      <!-- Иллюстрация: колонны, театральные маски, прожектор -->
      <svg viewBox="0 0 480 300" class="w-full max-w-md mx-auto" fill="none" aria-hidden="true">
        <!-- Луч прожектора -->
        <path d="M240 12 L145 195 L335 195 Z" class="fill-blue-400/10 dark:fill-blue-400/15"/>
        <circle cx="240" cy="16" r="11" class="fill-blue-500/30 dark:fill-blue-400/40"/>

        <!-- Фронтон -->
        <path d="M118 92 L240 46 L362 92" stroke="currentColor" stroke-width="6" stroke-linecap="round" class="text-gray-700 dark:text-gray-300"/>

        <!-- Колонны с капителями и основаниями -->
        <g stroke="currentColor" stroke-width="6" stroke-linecap="round" class="text-gray-700 dark:text-gray-300">
          <line x1="138" y1="102" x2="162" y2="102"/>
          <line x1="150" y1="110" x2="150" y2="186"/>
          <line x1="138" y1="194" x2="162" y2="194"/>

          <line x1="228" y1="102" x2="252" y2="102"/>
          <line x1="240" y1="110" x2="240" y2="186"/>
          <line x1="228" y1="194" x2="252" y2="194"/>

          <line x1="318" y1="102" x2="342" y2="102"/>
          <line x1="330" y1="110" x2="330" y2="186"/>
          <line x1="318" y1="194" x2="342" y2="194"/>

          <!-- Ступень -->
          <line x1="112" y1="202" x2="368" y2="202"/>
        </g>

        <!-- Маска комедии -->
        <g transform="translate(188 232) rotate(-8)">
          <path d="M-27 -22 Q0 -34 27 -22 Q33 4 21 21 Q0 33 -21 21 Q-33 4 -27 -22 Z"
                class="fill-white dark:fill-gray-800 text-blue-500 dark:text-blue-400" stroke="currentColor" stroke-width="4"/>
          <g class="text-blue-500 dark:text-blue-400" stroke="currentColor" stroke-width="4" stroke-linecap="round" fill="none">
            <circle cx="-10" cy="-5" r="3.5" fill="currentColor" stroke="none"/>
            <circle cx="10" cy="-5" r="3.5" fill="currentColor" stroke="none"/>
            <path d="M-12 6 Q0 19 12 6"/>
          </g>
        </g>

        <!-- Маска трагедии -->
        <g transform="translate(292 240) rotate(8)">
          <path d="M-27 -22 Q0 -34 27 -22 Q33 4 21 21 Q0 33 -21 21 Q-33 4 -27 -22 Z"
                class="fill-white dark:fill-gray-800 text-pink-500 dark:text-pink-400" stroke="currentColor" stroke-width="4"/>
          <g class="text-pink-500 dark:text-pink-400" stroke="currentColor" stroke-width="4" stroke-linecap="round" fill="none">
            <circle cx="-10" cy="-7" r="3.5" fill="currentColor" stroke="none"/>
            <circle cx="10" cy="-7" r="3.5" fill="currentColor" stroke="none"/>
            <path d="M-12 12 Q0 1 12 12"/>
          </g>
        </g>

        <!-- Тень на сцене -->
        <ellipse cx="240" cy="272" rx="150" ry="8" class="fill-gray-200 dark:fill-gray-700/60"/>
      </svg>

      <!-- Текст -->
      <p class="mt-6 text-6xl font-extrabold text-blue-500 dark:text-blue-400">404</p>
      <h1 class="mt-2 text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200">
        Страница не найдена
      </h1>
      <p class="mt-3 text-gray-500 dark:text-gray-400">
        Похоже, этой сцены нет в нашем репертуаре.<br class="hidden sm:inline">
        Возможно, ссылка устарела или страница была удалена.
      </p>

      <!-- Действия -->
      <div class="mt-8 flex flex-col sm:flex-row items-center justify-center gap-3">
        <button
          @click="goHome"
          class="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-medium transition-all duration-300 hover:shadow-lg hover:-translate-y-0.5"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1h-2z"/>
          </svg>
          На главную
        </button>
        <button
          @click="goBack"
          class="inline-flex items-center gap-2 px-6 py-3 rounded-xl border border-gray-300 dark:border-gray-600 text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 font-medium transition"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
          </svg>
          Назад
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  error: {
    type: Object,
    default: () => ({ statusCode: 404 })
  }
})

useHead({
  title: '404 — Страница не найдена | Центр Культуры'
})

// error.vue рендерится вне app.vue — применяем тему сами
onMounted(() => {
  if (localStorage.getItem('theme') === 'dark') {
    document.documentElement.classList.add('dark')
  }
})

const goHome = () => clearError({ redirect: '/' })

const goBack = () => {
  if (window.history.state?.back) {
    clearError()
    window.history.back()
  } else {
    clearError({ redirect: '/' })
  }
}
</script>
