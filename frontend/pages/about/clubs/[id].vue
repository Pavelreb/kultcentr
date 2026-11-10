<!-- frontend/pages/about/clubs/[id].vue -->
<template>
  <div class="max-w-4xl mx-auto mt-10 px-4 pb-16">
    <Breadcrumb :items="breadcrumbItems" />

    <div v-if="loading" class="bg-white dark:bg-gray-800 rounded-xl shadow-md h-96 animate-pulse"></div>

    <div v-else-if="!club" class="text-center py-20 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700">
      <p class="text-gray-500 dark:text-gray-400 mb-4">Клубное формирование не найдено</p>
      <NuxtLink to="/about/clubs" class="text-teal-600 dark:text-teal-400 hover:underline">Все клубные формирования</NuxtLink>
    </div>

    <article v-else class="bg-white dark:bg-gray-800 rounded-xl shadow-md overflow-hidden border border-gray-100 dark:border-gray-700">
      <div class="p-4 bg-gradient-to-br from-teal-50 to-gray-50 dark:from-gray-700/50 dark:to-gray-800">
        <div class="aspect-video rounded-lg overflow-hidden bg-gray-200 dark:bg-gray-700">
          <img
            v-if="club.display_image"
            :src="club.display_image"
            :alt="club.title"
            class="w-full h-full object-cover"
          />
          <div v-else class="w-full h-full flex items-center justify-center text-gray-400 dark:text-gray-500">
            <svg class="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
            </svg>
          </div>
        </div>
      </div>

      <div class="p-6 md:p-8">
        <h1 class="text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200 mb-4">{{ club.title }}</h1>

        <div class="flex flex-wrap gap-2 mb-6">
          <span v-if="club.leader_name" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-teal-50 dark:bg-teal-900/30 text-teal-700 dark:text-teal-300 rounded-lg text-sm">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
            </svg>
            {{ club.leader_name }}
          </span>
          <span v-if="club.schedule" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 rounded-lg text-sm">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            {{ club.schedule }}
          </span>
          <span v-if="club.age" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-purple-50 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 rounded-lg text-sm">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/>
            </svg>
            {{ club.age }}
          </span>
        </div>

        <div class="text-gray-700 dark:text-gray-300 leading-relaxed whitespace-pre-wrap">{{ club.content }}</div>
      </div>
    </article>
  </div>
</template>

<script setup>
const route = useRoute()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'
const { apiFetch } = useApi()

const club = ref(null)
const loading = ref(true)

const breadcrumbItems = computed(() => [
  { label: 'Об учреждении', to: '/about' },
  { label: 'Клубные формирования', to: '/about/clubs' },
  { label: club.value?.title || '...' }
])

useHead(() => ({
  title: club.value ? club.value.title : 'Клубное формирование'
}))

onMounted(async () => {
  try {
    const res = await apiFetch(`${API_URL}/about/clubs/${route.params.id}/`)
    if (res.ok) club.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки:', e)
  } finally {
    loading.value = false
  }
})
</script>
