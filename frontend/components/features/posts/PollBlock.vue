<!-- frontend/components/features/posts/PollBlock.vue -->
<!-- Блок голосования на странице поста -->
<template>
  <div v-if="poll" class="mt-6 p-5 rounded-xl border border-blue-100 dark:border-blue-900/40 bg-blue-50/50 dark:bg-blue-900/10">
    <div class="flex items-start justify-between gap-3 mb-4">
      <h3 class="font-semibold text-gray-900 dark:text-white flex items-center gap-2">
        <svg class="w-5 h-5 text-blue-500 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
        </svg>
        {{ poll.question }}
      </h3>
      <button
        v-if="poll.can_manage && authStore.isEditor"
        @click="removePoll"
        :disabled="removing"
        class="p-1.5 text-gray-400 hover:text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition flex-shrink-0 disabled:opacity-50"
        title="Удалить голосование"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
        </svg>
      </button>
    </div>

    <!-- Не авторизован: приглашение войти -->
    <div v-if="!authStore.isAuthenticated" class="text-sm text-gray-500 dark:text-gray-400">
      <p class="mb-3">Войдите, чтобы проголосовать.</p>
      <NuxtLink to="/auth/login" class="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-white bg-gradient-to-r from-blue-500 to-blue-600 rounded-xl hover:from-blue-600 hover:to-blue-700 transition">
        Войти
      </NuxtLink>
    </div>

    <!-- Форма голосования -->
    <div v-else-if="poll.user_vote === null || poll.user_vote === undefined" class="space-y-2">
      <button
        v-for="opt in poll.options"
        :key="opt.id"
        @click="vote(opt.id)"
        :disabled="voting"
        class="w-full text-left px-4 py-2.5 rounded-xl border border-gray-200 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:border-blue-400 dark:hover:border-blue-500 hover:text-blue-600 dark:hover:text-blue-400 transition disabled:opacity-50 text-sm font-medium"
      >
        {{ opt.text }}
      </button>
      <p v-if="voteError" class="text-sm text-red-500 mt-2">{{ voteError }}</p>
    </div>

    <!-- Результаты -->
    <div v-else class="space-y-2.5">
      <div v-for="opt in poll.options" :key="opt.id">
        <div class="flex items-center justify-between text-sm mb-1">
          <span class="text-gray-700 dark:text-gray-300 flex items-center gap-1.5">
            {{ opt.text }}
            <svg v-if="opt.id === poll.user_vote" class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
            </svg>
          </span>
          <span class="text-gray-500 dark:text-gray-400 tabular-nums">{{ percent(opt) }}% · {{ opt.votes }}</span>
        </div>
        <div class="h-2 rounded-full bg-gray-200 dark:bg-gray-700 overflow-hidden">
          <div
            class="h-full rounded-full transition-all duration-500"
            :class="opt.id === poll.user_vote ? 'bg-gradient-to-r from-blue-500 to-blue-600' : 'bg-gray-400 dark:bg-gray-500'"
            :style="{ width: percent(opt) + '%' }"
          ></div>
        </div>
      </div>
      <p class="text-xs text-gray-400 dark:text-gray-500 pt-1">Всего голосов: {{ poll.total_votes }}</p>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const props = defineProps({
  postId: {
    type: [Number, String],
    required: true
  },
  poll: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['updated', 'deleted'])

const authStore = useAuthStore()
const { apiFetch } = useApi()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const voting = ref(false)
const removing = ref(false)
const voteError = ref('')

const percent = (opt) => {
  if (!props.poll?.total_votes) return 0
  return Math.round((opt.votes / props.poll.total_votes) * 100)
}

const vote = async (optionId) => {
  voting.value = true
  voteError.value = ''
  try {
    const res = await apiFetch(`${API_URL}/posts/${props.postId}/poll/vote/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ option_id: optionId })
    })
    if (res.ok) {
      const data = await res.json()
      emit('updated', data)
    } else {
      const data = await res.json().catch(() => ({}))
      voteError.value = data.detail || 'Не удалось проголосовать'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    voteError.value = 'Ошибка подключения к серверу'
  } finally {
    voting.value = false
  }
}

const removePoll = async () => {
  if (!confirm('Удалить голосование? Все голоса будут потеряны.')) return
  removing.value = true
  try {
    const res = await apiFetch(`${API_URL}/posts/${props.postId}/`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ poll: null })
    })
    if (res.ok) {
      emit('deleted')
    } else {
      alert('Не удалось удалить голосование')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    removing.value = false
  }
}
</script>
