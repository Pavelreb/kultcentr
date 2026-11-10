<!-- frontend/pages/about/documents.vue -->
<template>
  <div class="max-w-4xl mx-auto mt-10 px-4 pb-16">
    <Breadcrumb :items="breadcrumbItems" />

    <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3 mb-8">
      <svg class="w-8 h-8 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
      </svg>
      Документы
    </h1>

    <div v-if="loading" class="space-y-3">
      <div v-for="n in 5" :key="n" class="bg-white dark:bg-gray-800 rounded-xl shadow-md h-20 animate-pulse"></div>
    </div>

    <div v-else-if="documents.length === 0" class="text-center py-20 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700">
      <p class="text-gray-500 dark:text-gray-400">Документы скоро появятся</p>
    </div>

    <div v-else class="space-y-3">
      <a
        v-for="doc in documents"
        :key="doc.id"
        :href="doc.file_display"
        target="_blank"
        rel="noopener"
        class="group flex items-center gap-4 bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 hover:-translate-y-0.5 p-4 border border-gray-100 dark:border-gray-700"
      >
        <div
          class="w-12 h-12 rounded-lg flex items-center justify-center flex-shrink-0 text-white text-[11px] font-bold uppercase tracking-wide"
          :class="extColor(doc.file_ext)"
        >
          {{ doc.file_ext || 'doc' }}
        </div>
        <div class="flex-1 min-w-0">
          <p class="font-semibold text-gray-800 dark:text-gray-200 group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors">
            {{ doc.title }}
          </p>
          <p v-if="doc.description" class="text-sm text-gray-500 dark:text-gray-400 truncate">{{ doc.description }}</p>
          <p class="text-xs text-gray-400 dark:text-gray-500 mt-0.5">
            <span class="uppercase">{{ doc.file_ext || 'файл' }}</span>
            <template v-if="doc.file_size"> · {{ formatSize(doc.file_size) }}</template>
            · {{ formatDate(doc.created_at) }}
          </p>
        </div>
        <svg class="w-5 h-5 text-gray-300 dark:text-gray-600 group-hover:text-indigo-500 dark:group-hover:text-indigo-400 transition-colors flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
        </svg>
      </a>
    </div>
  </div>
</template>

<script setup>
useSeoMeta({
  title: 'Документы',
  description: 'Официальные документы Центра Культуры.'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'
const { apiFetch } = useApi()

const documents = ref([])
const loading = ref(true)

const breadcrumbItems = [
  { label: 'Об учреждении', to: '/about' },
  { label: 'Документы' }
]

const extColor = (ext) => {
  if (ext === 'pdf') return 'bg-red-500'
  if (ext === 'doc' || ext === 'docx') return 'bg-blue-500'
  if (ext === 'xls' || ext === 'xlsx') return 'bg-green-600'
  if (ext === 'ppt' || ext === 'pptx') return 'bg-orange-500'
  return 'bg-gray-500'
}

const formatSize = (bytes) => {
  if (bytes < 1024) return bytes + ' Б'
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(0) + ' КБ'
  return (bytes / (1024 * 1024)).toFixed(1) + ' МБ'
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })
}

onMounted(async () => {
  try {
    const res = await apiFetch(`${API_URL}/about/documents/`)
    if (res.ok) documents.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки:', e)
  } finally {
    loading.value = false
  }
})
</script>
