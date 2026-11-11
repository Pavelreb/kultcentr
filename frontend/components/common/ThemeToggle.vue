<!-- frontend/components/common/ThemeToggle.vue -->
<!-- Выпадающее меню выбора оформления: светлая/тёмная + темы для слабовидящих -->
<template>
  <div class="relative" ref="menuRef">
    <button
      @click="open = !open"
      class="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition text-gray-600 dark:text-gray-300"
      title="Оформление"
      aria-label="Выбор оформления"
    >
      <!-- Иконка: глаз -->
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
      </svg>
    </button>

    <div
      v-if="open"
      class="absolute right-0 top-full mt-2 w-64 bg-white dark:bg-gray-800 rounded-lg shadow-xl border border-gray-200 dark:border-gray-700 py-2 z-50"
      @click.stop
    >
      <div class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
        Оформление
      </div>
      <button
        v-for="t in baseThemes"
        :key="t.id"
        @click="choose(t.id)"
        class="w-full flex items-center justify-between px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition text-left"
      >
        <span>{{ t.label }}</span>
        <svg v-if="themeStore.mode === t.id" class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/>
        </svg>
      </button>

      <div class="border-t border-gray-200 dark:border-gray-700 my-1"></div>
      <div class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
        Цветовое зрение
      </div>
      <button
        v-for="t in colorblindThemes"
        :key="t.id"
        @click="choose(t.id)"
        class="w-full flex items-center justify-between px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition text-left"
      >
        <span>{{ t.label }}</span>
        <svg v-if="themeStore.mode === t.id" class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/>
        </svg>
      </button>

      <div class="border-t border-gray-200 dark:border-gray-700 my-1"></div>
      <div class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
        Для слабовидящих
      </div>
      <button
        v-for="t in accessThemes"
        :key="t.id"
        @click="choose(t.id)"
        class="w-full flex items-center justify-between px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition text-left"
      >
        <span>{{ t.label }}</span>
        <svg v-if="themeStore.mode === t.id" class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/>
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
import { useThemeStore, THEMES } from '~/store/theme'

const themeStore = useThemeStore()

const open = ref(false)
const menuRef = ref(null)

const baseThemes = THEMES.filter(t => t.group === 'base')
const colorblindThemes = THEMES.filter(t => t.group === 'colorblind')
const accessThemes = THEMES.filter(t => t.group === 'access')

const choose = (id) => {
  themeStore.setTheme(id)
  open.value = false
}

const handleClickOutside = (event) => {
  if (menuRef.value && !menuRef.value.contains(event.target)) {
    open.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>
