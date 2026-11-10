<!-- frontend/pages/about/index.vue -->
<template>
  <div class="pb-16">
    <!-- Хироу-баннер: Общая информация -->
    <section class="relative overflow-hidden">
      <div
        class="absolute inset-0 bg-cover bg-center"
        :style="info?.background_display ? { backgroundImage: `url(${info.background_display})` } : {}"
        :class="!info?.background_display ? 'bg-gradient-to-br from-blue-600 via-indigo-600 to-purple-700' : ''"
      ></div>
      <div class="absolute inset-0 bg-black/50"></div>

      <div class="relative max-w-5xl mx-auto px-4 py-16 md:py-24 text-center text-white">
        <div v-if="info?.logo_display" class="w-24 h-24 md:w-28 md:h-28 mx-auto rounded-full bg-white/10 backdrop-blur-sm p-1.5 shadow-xl mb-5 overflow-hidden">
          <img :src="info.logo_display" :alt="info.name" class="w-full h-full object-cover rounded-full bg-white" />
        </div>
        <div v-else class="w-24 h-24 md:w-28 md:h-28 mx-auto rounded-full bg-white/10 backdrop-blur-sm flex items-center justify-center shadow-xl mb-5">
          <svg class="w-12 h-12 text-white/80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5v-9a2 2 0 00-2-2H9a2 2 0 00-2 2v9m12 0H3"/>
          </svg>
        </div>
        <h1 class="text-3xl md:text-5xl font-bold drop-shadow-lg">{{ info?.name || 'Центр Культуры' }}</h1>
        <p v-if="info?.description" class="mt-4 max-w-2xl mx-auto text-white/90 text-sm md:text-base leading-relaxed whitespace-pre-wrap drop-shadow">
          {{ info.description }}
        </p>
      </div>
    </section>

    <div class="max-w-6xl mx-auto px-4">
      <!-- Наши сотрудники -->
      <section class="mt-12">
        <div class="flex items-center justify-between mb-5">
          <NuxtLink to="/about/staff" class="group">
            <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
              <svg class="w-7 h-7 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
              </svg>
              Наши сотрудники
            </h2>
          </NuxtLink>
          <NuxtLink
            v-if="staff.length > 0"
            to="/about/staff"
            class="inline-flex items-center gap-1.5 px-4 py-2 text-sm font-medium text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-900/20 rounded-xl hover:bg-blue-100 dark:hover:bg-blue-900/40 transition"
          >
            Все сотрудники
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
            </svg>
          </NuxtLink>
        </div>
        <div v-if="loading" class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div v-for="n in 4" :key="n" class="bg-white dark:bg-gray-800 rounded-xl shadow-md h-52 animate-pulse"></div>
        </div>
        <div v-else-if="staff.length === 0" class="text-center py-8 bg-white dark:bg-gray-800 rounded-xl border border-gray-100 dark:border-gray-700 text-gray-400 dark:text-gray-500 text-sm">
          Информация о сотрудниках скоро появится
        </div>
        <div v-else class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <StaffCard v-for="m in staff.slice(0, 8)" :key="m.id" :member="m" />
        </div>
      </section>

      <!-- Клубные формирования -->
      <section class="mt-12">
        <div class="flex items-center justify-between mb-5">
          <NuxtLink to="/about/clubs" class="group">
            <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 group-hover:text-teal-600 dark:group-hover:text-teal-400 transition-colors">
              <svg class="w-7 h-7 text-teal-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
              </svg>
              Клубные формирования
            </h2>
          </NuxtLink>
          <NuxtLink
            v-if="clubs.length > 0"
            to="/about/clubs"
            class="inline-flex items-center gap-1.5 px-4 py-2 text-sm font-medium text-teal-600 dark:text-teal-400 bg-teal-50 dark:bg-teal-900/20 rounded-xl hover:bg-teal-100 dark:hover:bg-teal-900/40 transition"
          >
            Все формирования
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
            </svg>
          </NuxtLink>
        </div>
        <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <div v-for="n in 3" :key="n" class="bg-white dark:bg-gray-800 rounded-xl shadow-md h-64 animate-pulse"></div>
        </div>
        <div v-else-if="clubs.length === 0" class="text-center py-8 bg-white dark:bg-gray-800 rounded-xl border border-gray-100 dark:border-gray-700 text-gray-400 dark:text-gray-500 text-sm">
          Информация о клубных формированиях скоро появится
        </div>
        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <ClubCard v-for="c in clubs.slice(0, 6)" :key="c.id" :club="c" />
        </div>
      </section>

      <!-- Достижения -->
      <section class="mt-12">
        <div class="flex items-center justify-between mb-5">
          <NuxtLink to="/about/achievements" class="group">
            <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 group-hover:text-amber-600 dark:group-hover:text-amber-400 transition-colors">
              <svg class="w-7 h-7 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/>
              </svg>
              Достижения
            </h2>
          </NuxtLink>
          <NuxtLink
            v-if="achievements.length > 0"
            to="/about/achievements"
            class="inline-flex items-center gap-1.5 px-4 py-2 text-sm font-medium text-amber-600 dark:text-amber-400 bg-amber-50 dark:bg-amber-900/20 rounded-xl hover:bg-amber-100 dark:hover:bg-amber-900/40 transition"
          >
            Все достижения
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
            </svg>
          </NuxtLink>
        </div>
        <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <div v-for="n in 3" :key="n" class="bg-white dark:bg-gray-800 rounded-xl shadow-md h-64 animate-pulse"></div>
        </div>
        <div v-else-if="achievements.length === 0" class="text-center py-8 bg-white dark:bg-gray-800 rounded-xl border border-gray-100 dark:border-gray-700 text-gray-400 dark:text-gray-500 text-sm">
          Информация о достижениях скоро появится
        </div>
        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <AchievementCard v-for="a in achievements.slice(0, 6)" :key="a.id" :achievement="a" />
        </div>
      </section>

      <!-- Документы -->
      <section class="mt-12">
        <div class="flex items-center justify-between mb-5">
          <NuxtLink to="/about/documents" class="group">
            <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors">
              <svg class="w-7 h-7 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
              </svg>
              Документы
            </h2>
          </NuxtLink>
          <NuxtLink
            v-if="documents.length > 0"
            to="/about/documents"
            class="inline-flex items-center gap-1.5 px-4 py-2 text-sm font-medium text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-900/20 rounded-xl hover:bg-indigo-100 dark:hover:bg-indigo-900/40 transition"
          >
            Все документы
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
            </svg>
          </NuxtLink>
        </div>
        <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          <div v-for="n in 3" :key="n" class="bg-white dark:bg-gray-800 rounded-xl shadow-md h-16 animate-pulse"></div>
        </div>
        <div v-else-if="documents.length === 0" class="text-center py-8 bg-white dark:bg-gray-800 rounded-xl border border-gray-100 dark:border-gray-700 text-gray-400 dark:text-gray-500 text-sm">
          Документы скоро появятся
        </div>
        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          <DocumentCard v-for="d in documents.slice(0, 6)" :key="d.id" :doc="d" />
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import StaffCard from '~/components/features/about/StaffCard.vue'
import ClubCard from '~/components/features/about/ClubCard.vue'
import AchievementCard from '~/components/features/about/AchievementCard.vue'
import DocumentCard from '~/components/features/about/DocumentCard.vue'

useSeoMeta({
  title: 'Об учреждении',
  description: 'Общая информация, сотрудники, клубные формирования, достижения и документы Центра Культуры.'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'
const { apiFetch } = useApi()

const info = ref(null)
const staff = ref([])
const clubs = ref([])
const achievements = ref([])
const documents = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const [infoRes, staffRes, clubsRes, achRes, docsRes] = await Promise.all([
      apiFetch(`${API_URL}/about/info/`),
      apiFetch(`${API_URL}/about/staff/`),
      apiFetch(`${API_URL}/about/clubs/`),
      apiFetch(`${API_URL}/about/achievements/`),
      apiFetch(`${API_URL}/about/documents/`)
    ])
    if (infoRes.ok) info.value = await infoRes.json()
    if (staffRes.ok) staff.value = await staffRes.json()
    if (clubsRes.ok) clubs.value = await clubsRes.json()
    if (achRes.ok) achievements.value = await achRes.json()
    if (docsRes.ok) documents.value = await docsRes.json()
  } catch (e) {
    console.error('Ошибка загрузки:', e)
  } finally {
    loading.value = false
  }
})
</script>
