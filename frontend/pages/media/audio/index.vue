<!-- frontend/pages/media/audio/index.vue -->
<template>
  <div class="container mx-auto p-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-teal-500 dark:text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/>
        </svg>
        Аудиозаписи
      </h1>
      <NuxtLink
        v-if="authStore.isEditor"
        to="/settings/audio"
        class="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-teal-600 dark:text-teal-400 bg-teal-50 dark:bg-teal-900/20 rounded-xl hover:bg-teal-100 dark:hover:bg-teal-900/30 transition-all duration-300"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
        </svg>
        Управление
      </NuxtLink>
    </div>

    <div v-if="loading" class="text-center py-20">
      <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>

    <div v-else-if="audios.length === 0" class="text-center py-20 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет аудиозаписей</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>

    <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-5">
      <AudioCard v-for="item in audios" :key="item.id" :audio="item" />
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import AudioCard from '~/components/features/media/AudioCard.vue'

useSeoMeta({
  title: 'Аудиозаписи',
  description: 'Аудиозаписи центра культуры: концерты, лекции, выступления.'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()

const audios = ref([])
const loading = ref(true)

onMounted(async () => {
  authStore.restoreAuth()
  try {
    const res = await fetch(`${API_URL}/medialib/audio/`)
    if (res.ok) {
      audios.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка загрузки аудиозаписей:', e)
  } finally {
    loading.value = false
  }
})
</script>
