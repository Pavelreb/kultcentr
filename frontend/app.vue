<template>
  <div class="flex flex-col min-h-screen">
    <!-- HEADER -->
    <AppHeader />

    <!-- MAIN -->
    <main class="flex-1">
      <NuxtPage />
    </main>

    <!-- FOOTER -->
    <AppFooter />

    <!-- Кнопка плавной прокрутки наверх -->
    <ScrollToTop />

    <!-- Скрытые SVG-фильтры дальтонизации для тем цветового зрения.
         Матрицы разводят цвета по линии конфликта через третий канал:
         красно-зелёный конфликт (протанопия/дейтеранопия) уходит в синий,
         сине-жёлтый (тританопия) — в красный. -->
    <svg width="0" height="0" style="position: absolute" aria-hidden="true" focusable="false">
      <defs>
        <filter id="daltonize-protanopia">
          <feColorMatrix type="matrix" values="1.2 0 0 0 0  0 1 0 0 0  0.75 -0.75 1 0 0  0 0 0 1 0" />
        </filter>
        <filter id="daltonize-deuteranopia">
          <feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0.7 -0.7 1 0 0  0 0 0 1 0" />
        </filter>
        <filter id="daltonize-tritanopia">
          <feColorMatrix type="matrix" values="1 0.7 -0.7 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 1 0" />
        </filter>
      </defs>
    </svg>
  </div>
</template>

<script setup>
import AppHeader from '~/components/layout/AppHeader.vue'
import AppFooter from '~/components/layout/AppFooter.vue'
import ScrollToTop from '~/components/ScrollToTop.vue'
import { useThemeStore } from '~/store/theme'

const themeStore = useThemeStore()

// Восстанавливаем тему из localStorage при каждой загрузке приложения
onMounted(() => {
  themeStore.loadTheme()
})
</script>