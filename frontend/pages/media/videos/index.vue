<!-- frontend/pages/media/videos/index.vue -->
<template>
  <div class="container mx-auto p-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-rose-500 dark:text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/>
        </svg>
        Видеоролики
      </h1>
      <NuxtLink
        v-if="authStore.isEditor"
        to="/settings/videos"
        class="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-900/20 rounded-xl hover:bg-rose-100 dark:hover:bg-rose-900/30 transition-all duration-300"
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

    <div v-else-if="videos.length === 0" class="text-center py-20 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет видеороликов</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>

    <div v-else>
      <div class="grid grid-cols-2 max-[420px]:grid-cols-1 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 md:gap-5">
        <VideoCard v-for="video in videos" :key="video.id" :video="video" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import VideoCard from '~/components/features/media/VideoCard.vue'

useSeoMeta({
  title: 'Видеоролики',
  description: 'Видеоролики центра культуры: мероприятия, концерты, мастер-классы.'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()

const videos = ref([])
const loading = ref(true)

onMounted(async () => {
  authStore.restoreAuth()
  try {
    const res = await fetch(`${API_URL}/medialib/videos/`)
    if (res.ok) {
      videos.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка загрузки видеороликов:', e)
  } finally {
    loading.value = false
  }
})
</script>
