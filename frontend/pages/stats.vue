<!-- frontend/pages/stats.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4">
    <!-- Заголовок -->
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-rose-500 dark:text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
        </svg>
        Статистика
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
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут просматривать статистику.</p>
    </div>

    <template v-else>
      <!-- Вкладки -->
      <div class="flex gap-2 mb-6">
        <button
          @click="tab = 'polls'"
          class="px-4 py-2 rounded-xl text-sm font-medium transition"
          :class="tab === 'polls'
            ? 'bg-blue-500 text-white shadow-lg shadow-blue-500/25'
            : 'bg-white dark:bg-gray-800 text-gray-600 dark:text-gray-300 border border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700'"
        >
          Голосования ({{ stats?.polls?.length || 0 }})
        </button>
        <button
          @click="tab = 'quizzes'"
          class="px-4 py-2 rounded-xl text-sm font-medium transition"
          :class="tab === 'quizzes'
            ? 'bg-emerald-500 text-white shadow-lg shadow-emerald-500/25'
            : 'bg-white dark:bg-gray-800 text-gray-600 dark:text-gray-300 border border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700'"
        >
          Тесты ({{ stats?.quizzes?.length || 0 }})
        </button>
      </div>

      <!-- Загрузка -->
      <div v-if="loading" class="text-center py-20">
        <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
        </svg>
        <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
      </div>

      <!-- ГОЛОСОВАНИЯ -->
      <div v-else-if="tab === 'polls'" class="space-y-4">
        <div v-if="!stats?.polls?.length" class="text-center py-16 text-gray-400 dark:text-gray-500">
          Пока нет ни одного голосования
        </div>

        <div
          v-for="poll in stats?.polls"
          :key="poll.id"
          class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-5"
        >
          <div class="flex flex-wrap items-start justify-between gap-2 mb-4">
            <div>
              <h3 class="font-semibold text-gray-900 dark:text-white">{{ poll.question }}</h3>
              <NuxtLink
                :to="`/posts/${poll.post_id}`"
                class="text-sm text-blue-600 dark:text-blue-400 hover:underline"
              >
                {{ poll.post_title }}
              </NuxtLink>
            </div>
            <span class="text-sm text-gray-400 dark:text-gray-500">
              Всего голосов: <span class="font-semibold text-gray-700 dark:text-gray-300">{{ poll.total_votes }}</span>
            </span>
          </div>

          <div class="space-y-3">
            <div v-for="opt in poll.options" :key="opt.id">
              <div class="flex items-center justify-between text-sm mb-1">
                <span class="text-gray-700 dark:text-gray-300">{{ opt.text }}</span>
                <span class="text-gray-500 dark:text-gray-400 tabular-nums">{{ percent(opt.votes, poll.total_votes) }}% · {{ opt.votes }}</span>
              </div>
              <div class="h-2 rounded-full bg-gray-200 dark:bg-gray-700 overflow-hidden">
                <div
                  class="h-full rounded-full bg-gradient-to-r from-blue-500 to-blue-600 transition-all duration-500"
                  :style="{ width: percent(opt.votes, poll.total_votes) + '%' }"
                ></div>
              </div>
              <!-- Кто голосовал -->
              <details v-if="opt.voters.length" class="mt-1.5">
                <summary class="text-xs text-gray-400 dark:text-gray-500 cursor-pointer hover:text-blue-500 transition select-none">
                  Проголосовали ({{ opt.voters.length }})
                </summary>
                <ul class="mt-1 space-y-0.5 pl-3 text-xs text-gray-500 dark:text-gray-400">
                  <li v-for="(v, i) in opt.voters" :key="i">
                    {{ v.name }} · {{ formatDateTime(v.voted_at) }}
                  </li>
                </ul>
              </details>
            </div>
          </div>
        </div>
      </div>

      <!-- ТЕСТЫ -->
      <div v-else class="space-y-4">
        <div v-if="!stats?.quizzes?.length" class="text-center py-16 text-gray-400 dark:text-gray-500">
          Пока нет ни одного теста
        </div>

        <div
          v-for="quiz in stats?.quizzes"
          :key="quiz.id"
          class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-5"
        >
          <div class="flex flex-wrap items-start justify-between gap-2 mb-4">
            <div>
              <h3 class="font-semibold text-gray-900 dark:text-white">{{ quiz.title }}</h3>
              <NuxtLink
                :to="`/posts/${quiz.post_id}`"
                class="text-sm text-blue-600 dark:text-blue-400 hover:underline"
              >
                {{ quiz.post_title }}
              </NuxtLink>
            </div>
            <div class="text-sm text-gray-400 dark:text-gray-500 text-right">
              <div>Вопросов: <span class="font-semibold text-gray-700 dark:text-gray-300">{{ quiz.questions_count }}</span></div>
              <div>Прохождений: <span class="font-semibold text-gray-700 dark:text-gray-300">{{ quiz.attempts_count }}</span></div>
              <div v-if="quiz.avg_percent !== null">
                Средний результат: <span class="font-semibold text-gray-700 dark:text-gray-300">{{ quiz.avg_percent }}%</span>
              </div>
            </div>
          </div>

          <div v-if="quiz.attempts.length" class="overflow-x-auto">
            <table class="w-full text-sm">
              <thead>
                <tr class="text-left text-xs text-gray-400 dark:text-gray-500 uppercase tracking-wide border-b border-gray-100 dark:border-gray-700">
                  <th class="py-2 pr-4 font-medium">Пользователь</th>
                  <th class="py-2 pr-4 font-medium">Результат</th>
                  <th class="py-2 pr-4 font-medium">Процент</th>
                  <th class="py-2 font-medium">Дата</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="(a, i) in quiz.attempts"
                  :key="i"
                  class="border-b border-gray-50 dark:border-gray-700/50 last:border-0"
                >
                  <td class="py-2 pr-4 text-gray-700 dark:text-gray-300">{{ a.name }}</td>
                  <td class="py-2 pr-4 text-gray-700 dark:text-gray-300 tabular-nums">{{ a.score }} / {{ a.total }}</td>
                  <td class="py-2 pr-4">
                    <span
                      class="inline-block px-2 py-0.5 rounded-full text-xs font-semibold"
                      :class="scoreBadgeClass(a.score, a.total)"
                    >
                      {{ Math.round((a.score / a.total) * 100) }}%
                    </span>
                  </td>
                  <td class="py-2 text-gray-400 dark:text-gray-500">{{ formatDateTime(a.created_at) }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p v-else class="text-sm text-gray-400 dark:text-gray-500">Тест ещё никто не проходил</p>
        </div>
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
  title: 'Статистика'
})

const authStore = useAuthStore()
const { apiFetch } = useApi()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const stats = ref(null)
const loading = ref(true)
const tab = ref('polls')

const percent = (votes, total) => (total ? Math.round((votes / total) * 100) : 0)

const scoreBadgeClass = (score, total) => {
  const pct = total ? score / total : 0
  if (pct >= 0.8) return 'bg-emerald-100 dark:bg-emerald-900/40 text-emerald-600 dark:text-emerald-400'
  if (pct >= 0.5) return 'bg-yellow-100 dark:bg-yellow-900/40 text-yellow-600 dark:text-yellow-400'
  return 'bg-red-100 dark:bg-red-900/40 text-red-600 dark:text-red-400'
}

const formatDateTime = (dateString) => {
  if (!dateString) return ''
  return new Date(dateString).toLocaleString('ru-RU', {
    day: 'numeric',
    month: 'short',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(async () => {
  authStore.restoreAuth()
  try {
    const res = await apiFetch(`${API_URL}/posts/stats/`)
    if (res.ok) {
      stats.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>
