<!-- frontend/pages/about/achievements/index.vue -->
<template>
  <div class="max-w-6xl mx-auto mt-10 px-4 pb-16">
    <Breadcrumb :items="breadcrumbItems" />

    <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3 mb-8">
      <svg class="w-8 h-8 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/>
      </svg>
      Достижения
    </h1>

    <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <div v-for="n in 6" :key="n" class="bg-white dark:bg-gray-800 rounded-xl shadow-md h-64 animate-pulse"></div>
    </div>

    <div v-else-if="achievements.length === 0" class="text-center py-20 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700">
      <p class="text-gray-500 dark:text-gray-400">Достижения скоро появятся</p>
    </div>

    <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <AchievementCard v-for="a in achievements" :key="a.id" :achievement="a" />
    </div>
  </div>
</template>

<script setup>
import AchievementCard from '~/components/features/about/AchievementCard.vue'

useSeoMeta({
  title: 'Достижения',
  description: 'Награды и достижения Центра Культуры.'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'
const { apiFetch } = useApi()

const achievements = ref([])
const loading = ref(true)

const breadcrumbItems = [
  { label: 'Об учреждении', to: '/about' },
  { label: 'Достижения' }
]

onMounted(async () => {
  try {
    const res = await apiFetch(`${API_URL}/about/achievements/`)
    if (res.ok) achievements.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки:', e)
  } finally {
    loading.value = false
  }
})
</script>
