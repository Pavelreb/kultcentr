<!-- frontend/pages/about/clubs/index.vue -->
<template>
  <div class="max-w-6xl mx-auto mt-10 px-4 pb-16">
    <Breadcrumb :items="breadcrumbItems" />

    <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3 mb-8">
      <svg class="w-8 h-8 text-teal-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
      </svg>
      Клубные формирования
    </h1>

    <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <div v-for="n in 6" :key="n" class="bg-white dark:bg-gray-800 rounded-xl shadow-md h-64 animate-pulse"></div>
    </div>

    <div v-else-if="clubs.length === 0" class="text-center py-20 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700">
      <p class="text-gray-500 dark:text-gray-400">Клубные формирования скоро появятся</p>
    </div>

    <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <ClubCard v-for="c in clubs" :key="c.id" :club="c" />
    </div>
  </div>
</template>

<script setup>
import ClubCard from '~/components/features/about/ClubCard.vue'

useSeoMeta({
  title: 'Клубные формирования',
  description: 'Кружки и клубные формирования Центра Культуры.'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'
const { apiFetch } = useApi()

const clubs = ref([])
const loading = ref(true)

const breadcrumbItems = [
  { label: 'Об учреждении', to: '/about' },
  { label: 'Клубные формирования' }
]

onMounted(async () => {
  try {
    const res = await apiFetch(`${API_URL}/about/clubs/`)
    if (res.ok) clubs.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки:', e)
  } finally {
    loading.value = false
  }
})
</script>
