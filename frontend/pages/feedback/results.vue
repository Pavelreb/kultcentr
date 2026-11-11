<!-- frontend/pages/feedback/results.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4">
    <!-- Заголовок -->
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-indigo-500 dark:text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
        </svg>
        Обратная связь
      </h1>
      <NuxtLink 
        to="/" 
        class="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 hover:-translate-y-0.5"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
        </svg>
        На главную
      </NuxtLink>
    </div>

    <div v-if="!authStore.isEditor" class="bg-white dark:bg-gray-800 p-8 rounded-lg shadow text-center py-20">
      <svg class="w-24 h-24 mx-auto text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
      </svg>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут просматривать обратную связь.</p>
    </div>

    <template v-else>
      <!-- Вкладки -->
      <div class="flex gap-2 mb-6">
        <button
          @click="tab = 'messages'"
          class="px-4 py-2 rounded-xl text-sm font-medium transition"
          :class="tab === 'messages'
            ? 'bg-blue-500 text-white shadow-lg shadow-blue-500/25'
            : 'bg-white dark:bg-gray-800 text-gray-600 dark:text-gray-300 border border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700'"
        >
          Сообщения ({{ messages.length }})
        </button>
        <button
          @click="tab = 'assessments'"
          class="px-4 py-2 rounded-xl text-sm font-medium transition"
          :class="tab === 'assessments'
            ? 'bg-amber-500 text-white shadow-lg shadow-amber-500/25'
            : 'bg-white dark:bg-gray-800 text-gray-600 dark:text-gray-300 border border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700'"
        >
          Оценки учреждения ({{ assessment?.total || 0 }})
        </button>
      </div>

      <div v-if="loading" class="text-center py-20">
        <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
        </svg>
        <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
      </div>

      <!-- СООБЩЕНИЯ -->
      <div v-else-if="tab === 'messages'" class="space-y-4">
        <div v-if="!messages.length" class="text-center py-16 text-gray-400 dark:text-gray-500">
          Сообщений пока нет
        </div>
        <div
          v-for="m in messages"
          :key="m.id"
          class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-5"
        >
          <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
            <div class="flex items-center gap-2">
              <span class="font-semibold text-gray-900 dark:text-white">{{ m.full_name || 'Без имени' }}</span>
              <a :href="`mailto:${m.email}`" class="text-sm text-blue-600 dark:text-blue-400 hover:underline">{{ m.email }}</a>
            </div>
            <span class="text-xs text-gray-400 dark:text-gray-500">{{ formatDateTime(m.created_at) }}</span>
          </div>
          <p class="text-sm text-gray-700 dark:text-gray-300 whitespace-pre-wrap">{{ m.text }}</p>
        </div>
      </div>

      <!-- ОЦЕНКИ -->
      <div v-else class="space-y-4">
        <div v-if="!assessment || !assessment.total" class="text-center py-16 text-gray-400 dark:text-gray-500">
          Ответов на опрос пока нет
        </div>

        <template v-else>
          <!-- Сводка -->
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-5">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
              <h3 class="font-semibold text-gray-900 dark:text-white">Средние оценки</h3>
              <span class="text-sm text-gray-500 dark:text-gray-400">
                Общая оценка:
                <span class="text-lg font-bold" :class="scoreTextClass(assessment.overall_average)">{{ assessment.overall_average }}</span>
                / 5
              </span>
            </div>
            <div class="space-y-3">
              <div v-for="a in assessment.averages" :key="a.key">
                <div class="flex items-center justify-between text-sm mb-1">
                  <span class="text-gray-700 dark:text-gray-300">{{ a.text }}</span>
                  <span class="font-semibold tabular-nums" :class="scoreTextClass(a.average)">{{ a.average }}</span>
                </div>
                <div class="h-2 rounded-full bg-gray-200 dark:bg-gray-700 overflow-hidden">
                  <div
                    class="h-full rounded-full bg-gradient-to-r from-amber-400 to-amber-500 transition-all duration-500"
                    :style="{ width: (a.average / 5 * 100) + '%' }"
                  ></div>
                </div>
              </div>
            </div>
          </div>

          <!-- Отдельные ответы -->
          <details
            v-for="r in assessment.responses"
            :key="r.id"
            class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-5"
          >
            <summary class="cursor-pointer select-none flex flex-wrap items-center justify-between gap-2">
              <span class="flex items-center gap-2">
                <span class="font-semibold text-gray-900 dark:text-white">{{ r.full_name || 'Без имени' }}</span>
                <span class="text-sm text-blue-600 dark:text-blue-400">{{ r.email }}</span>
              </span>
              <span class="text-xs text-gray-400 dark:text-gray-500">{{ formatDateTime(r.created_at) }}</span>
            </summary>
            <div class="mt-3 space-y-1.5">
              <div
                v-for="q in questions"
                :key="q.key"
                class="flex items-center justify-between text-sm"
              >
                <span class="text-gray-600 dark:text-gray-400">{{ q.text }}</span>
                <span
                  class="px-2 py-0.5 rounded-full text-xs font-semibold"
                  :class="scoreBadgeClass(r.ratings[q.key])"
                >
                  {{ r.ratings[q.key] }} / 5
                </span>
              </div>
              <p class="mt-3 pt-3 border-t border-gray-100 dark:border-gray-700 text-sm text-gray-700 dark:text-gray-300 whitespace-pre-wrap">
                {{ r.text }}
              </p>
            </div>
          </details>
        </template>
      </div>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: ['auth', 'editor']
})

useSeoMeta({
  title: 'Обратная связь — результаты'
})

const authStore = useAuthStore()
const { apiFetch } = useApi()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const tab = ref('messages')
const loading = ref(true)
const messages = ref([])
const assessment = ref(null)
const questions = ref([])

const formatDateTime = (dateString) => {
  if (!dateString) return ''
  return new Date(dateString).toLocaleString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const scoreTextClass = (avg) => {
  if (avg >= 4) return 'text-emerald-600 dark:text-emerald-400'
  if (avg >= 3) return 'text-yellow-600 dark:text-yellow-400'
  return 'text-red-600 dark:text-red-400'
}

const scoreBadgeClass = (score) => {
  if (score >= 4) return 'bg-emerald-100 dark:bg-emerald-900/40 text-emerald-600 dark:text-emerald-400'
  if (score >= 3) return 'bg-yellow-100 dark:bg-yellow-900/40 text-yellow-600 dark:text-yellow-400'
  return 'bg-red-100 dark:bg-red-900/40 text-red-600 dark:text-red-400'
}

onMounted(async () => {
  authStore.restoreAuth()
  try {
    const [mRes, aRes, qRes] = await Promise.all([
      apiFetch(`${API_URL}/feedback/`),
      apiFetch(`${API_URL}/assessment/`),
      fetch(`${API_URL}/assessment/questions/`)
    ])
    if (mRes.ok) messages.value = await mRes.json()
    if (aRes.ok) assessment.value = await aRes.json()
    if (qRes.ok) questions.value = await qRes.json()
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>
