<!-- frontend/pages/about/staff.vue -->
<template>
  <div class="max-w-6xl mx-auto mt-10 px-4 pb-16">
    <Breadcrumb :items="breadcrumbItems" />

    <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3 mb-8">
      <svg class="w-8 h-8 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
      </svg>
      Наши сотрудники
    </h1>

    <div v-if="loading" class="text-center py-20 text-gray-500 dark:text-gray-400">Загрузка…</div>

    <div v-else-if="staff.length === 0" class="text-center py-20 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700">
      <p class="text-gray-500 dark:text-gray-400">Информация о сотрудниках скоро появится</p>
    </div>

    <template v-else>
      <section v-for="group in groupedStaff" :key="group.key" class="mb-10">
        <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 mb-4 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full" :class="group.dotClass"></span>
          {{ group.title }}
          <span class="text-sm font-normal text-gray-400 dark:text-gray-500">({{ group.members.length }})</span>
        </h2>
        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
          <StaffCard v-for="m in group.members" :key="m.id" :member="m" />
        </div>
      </section>
    </template>
  </div>
</template>

<script setup>
import StaffCard from '~/components/features/about/StaffCard.vue'

useSeoMeta({
  title: 'Наши сотрудники',
  description: 'Сотрудники Центра Культуры: администрация, основной, технический и вспомогательный персонал.'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'
const { apiFetch } = useApi()

const staff = ref([])
const loading = ref(true)

const breadcrumbItems = [
  { label: 'Об учреждении', to: '/about' },
  { label: 'Наши сотрудники' }
]

const CATEGORY_META = {
  aup: { title: 'Административно-управленческий персонал', dotClass: 'bg-yellow-500' },
  main: { title: 'Основной персонал', dotClass: 'bg-green-500' },
  technical: { title: 'Технический персонал', dotClass: 'bg-blue-500' },
  auxiliary: { title: 'Вспомогательный персонал', dotClass: 'bg-gray-500' }
}

const groupedStaff = computed(() => {
  return Object.entries(CATEGORY_META)
    .map(([key, meta]) => ({
      key,
      ...meta,
      members: staff.value.filter(m => m.category === key)
    }))
    .filter(g => g.members.length > 0)
})

onMounted(async () => {
  try {
    const res = await apiFetch(`${API_URL}/about/staff/`)
    if (res.ok) staff.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки сотрудников:', e)
  } finally {
    loading.value = false
  }
})
</script>
