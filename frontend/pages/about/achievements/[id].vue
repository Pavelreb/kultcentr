<!-- frontend/pages/about/achievements/[id].vue -->
<template>
  <div class="max-w-4xl mx-auto mt-10 px-4 pb-16">
    <Breadcrumb :items="breadcrumbItems" />

    <div v-if="loading" class="bg-white dark:bg-gray-800 rounded-xl shadow-md h-96 animate-pulse"></div>

    <div v-else-if="!achievement" class="text-center py-20 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700">
      <p class="text-gray-500 dark:text-gray-400 mb-4">Достижение не найдено</p>
      <NuxtLink to="/about/achievements" class="text-amber-600 dark:text-amber-400 hover:underline">Все достижения</NuxtLink>
    </div>

    <article v-else class="bg-white dark:bg-gray-800 rounded-xl shadow-md overflow-hidden border border-gray-100 dark:border-gray-700">
      <div class="p-4 bg-gradient-to-br from-amber-50 to-gray-50 dark:from-gray-700/50 dark:to-gray-800">
        <div class="aspect-video rounded-lg overflow-hidden bg-gray-200 dark:bg-gray-700">
          <img
            v-if="achievement.display_image"
            :src="achievement.display_image"
            :alt="achievement.title"
            class="w-full h-full object-cover"
          />
          <div v-else class="w-full h-full flex items-center justify-center text-gray-400 dark:text-gray-500">
            <svg class="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/>
            </svg>
          </div>
        </div>
      </div>

      <div class="p-6 md:p-8">
        <div class="flex items-center gap-3 mb-3">
          <span v-if="achievement.date" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-amber-50 dark:bg-amber-900/30 text-amber-700 dark:text-amber-300 rounded-lg text-sm">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            {{ formattedDate }}
          </span>
        </div>

        <h1 class="text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200 mb-4">{{ achievement.title }}</h1>

        <div class="text-gray-700 dark:text-gray-300 leading-relaxed whitespace-pre-wrap">{{ achievement.content }}</div>
      </div>
    </article>
  </div>
</template>

<script setup>
const route = useRoute()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'
const { apiFetch } = useApi()

const achievement = ref(null)
const loading = ref(true)

const breadcrumbItems = computed(() => [
  { label: 'Об учреждении', to: '/about' },
  { label: 'Достижения', to: '/about/achievements' },
  { label: achievement.value?.title || '...' }
])

const formattedDate = computed(() => {
  if (!achievement.value?.date) return ''
  return new Date(achievement.value.date).toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })
})

useHead(() => ({
  title: achievement.value ? achievement.value.title : 'Достижение'
}))

onMounted(async () => {
  try {
    const res = await apiFetch(`${API_URL}/about/achievements/${route.params.id}/`)
    if (res.ok) achievement.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки:', e)
  } finally {
    loading.value = false
  }
})
</script>
