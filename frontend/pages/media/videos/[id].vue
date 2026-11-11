<!-- frontend/pages/media/videos/[id].vue -->
<template>
  <div class="container mx-auto p-4 max-w-4xl">
    <div v-if="loading" class="text-center py-20">
      <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>

    <div v-else-if="!video" class="text-center py-20 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <p class="text-gray-500 dark:text-gray-400">Видеоролик не найден</p>
      <NuxtLink to="/media/videos" class="text-rose-500 hover:underline text-sm mt-2 inline-block">Все видеоролики</NuxtLink>
    </div>

    <template v-else>
      <!-- Кнопка назад -->
      <button
        @click="$router.back()"
        class="inline-flex items-center gap-2 mb-4 px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
        </svg>
        Назад
      </button>

      <!-- Плеер -->
      <div class="rounded-2xl overflow-hidden shadow-xl bg-black">
        <VideoPlayer :src="video.file_display" :poster="video.thumbnail_display || ''" />
      </div>

      <!-- Информация -->
      <div class="mt-6 bg-white dark:bg-gray-800 rounded-xl shadow-md p-6">
        <h1 class="text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200">
          {{ video.title }}
        </h1>
        <div class="flex items-center gap-4 mt-2 text-sm text-gray-400 dark:text-gray-500">
          <span class="inline-flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V7m-9 4h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            {{ formatDate(video.created_at) }}
          </span>
          <span v-if="video.duration" class="inline-flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            {{ formatDuration(video.duration) }}
          </span>
        </div>
        <div v-if="video.description" class="mt-4 text-gray-700 dark:text-gray-300">
          <RichText :text="video.description" />
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import RichText from '~/components/common/RichText.vue'
import VideoPlayer from '~/components/common/VideoPlayer.vue'

const route = useRoute()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const video = ref(null)
const loading = ref(true)

const formatDuration = (sec) => {
  const m = Math.floor(sec / 60)
  const s = sec % 60
  return `${m}:${String(s).padStart(2, '0')}`
}

const formatDate = (iso) => {
  if (!iso) return ''
  return new Date(iso).toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })
}

onMounted(async () => {
  try {
    const res = await fetch(`${API_URL}/medialib/videos/${route.params.id}/`)
    if (res.ok) {
      video.value = await res.json()
      useSeoMeta({
        title: video.value.title,
        description: (video.value.description || 'Видеоролик центра культуры').slice(0, 160)
      })
    }
  } catch (e) {
    console.error('Ошибка загрузки видеоролика:', e)
  } finally {
    loading.value = false
  }
})
</script>
