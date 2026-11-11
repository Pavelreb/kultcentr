<!-- frontend/components/features/posts/QuizBlock.vue -->
<!-- Блок теста на странице поста -->
<template>
  <div v-if="quiz" class="mt-6 p-5 rounded-xl border border-emerald-100 dark:border-emerald-900/40 bg-emerald-50/50 dark:bg-emerald-900/10">
    <div class="flex items-start justify-between gap-3 mb-4">
      <div>
        <h3 class="font-semibold text-gray-900 dark:text-white flex items-center gap-2">
          <svg class="w-5 h-5 text-emerald-500 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/>
          </svg>
          {{ quiz.title }}
        </h3>
        <p v-if="quiz.description" class="text-sm text-gray-500 dark:text-gray-400 mt-1">{{ quiz.description }}</p>
      </div>
      <button
        v-if="quiz.can_manage && authStore.isEditor"
        @click="removeQuiz"
        :disabled="removing"
        class="p-1.5 text-gray-400 hover:text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition flex-shrink-0 disabled:opacity-50"
        title="Удалить тест"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
        </svg>
      </button>
    </div>

    <!-- Не авторизован -->
    <div v-if="!authStore.isAuthenticated" class="text-sm text-gray-500 dark:text-gray-400">
      <p class="mb-3">Войдите, чтобы пройти тест. Вопросов: {{ quiz.questions_count }}.</p>
      <NuxtLink to="/auth/login" class="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-white bg-gradient-to-r from-emerald-500 to-emerald-600 rounded-xl hover:from-emerald-600 hover:to-emerald-700 transition">
        Войти
      </NuxtLink>
    </div>

    <!-- Результат (тест пройден) -->
    <div v-else-if="quiz.attempted" class="space-y-4">
      <div class="flex items-center gap-3 p-4 rounded-xl bg-white dark:bg-gray-800 border border-emerald-200 dark:border-emerald-800">
        <div
          class="w-12 h-12 rounded-full flex items-center justify-center text-lg font-bold flex-shrink-0"
          :class="scoreClass"
        >
          {{ Math.round((quiz.score / quiz.total) * 100) }}%
        </div>
        <div>
          <p class="font-semibold text-gray-900 dark:text-white">Результат: {{ quiz.score }} из {{ quiz.total }}</p>
          <p class="text-xs text-gray-400 dark:text-gray-500">Тест можно пройти только один раз</p>
        </div>
      </div>

      <!-- Разбор ответов -->
      <div class="space-y-3">
        <div
          v-for="(q, qi) in quiz.questions"
          :key="q.id"
          class="p-4 rounded-xl bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-600"
        >
          <p class="text-sm font-medium text-gray-900 dark:text-white mb-2">{{ qi + 1 }}. {{ q.text }}</p>
          <div class="space-y-1.5">
            <div
              v-for="a in q.answers"
              :key="a.id"
              class="flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm"
              :class="answerClass(q, a)"
            >
              <svg v-if="a.is_correct" class="w-4 h-4 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
              </svg>
              <svg v-else-if="isMyAnswer(q, a)" class="w-4 h-4 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
              <span v-else class="w-4 flex-shrink-0"></span>
              {{ a.text }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Форма прохождения -->
    <div v-else class="space-y-4">
      <div
        v-for="(q, qi) in quiz.questions"
        :key="q.id"
        class="p-4 rounded-xl bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-600"
      >
        <p class="text-sm font-medium text-gray-900 dark:text-white mb-2">{{ qi + 1 }}. {{ q.text }}</p>
        <div class="space-y-1.5">
          <label
            v-for="a in q.answers"
            :key="a.id"
            class="flex items-center gap-2 px-3 py-2 rounded-lg cursor-pointer text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700/50 transition"
            :class="{ 'bg-emerald-50 dark:bg-emerald-900/20 ring-1 ring-emerald-300 dark:ring-emerald-700': answers[q.id] === a.id }"
          >
            <input
              type="radio"
              :name="`quiz-${quiz.id}-q-${q.id}`"
              :value="a.id"
              v-model="answers[q.id]"
              class="w-4 h-4 text-emerald-500 flex-shrink-0"
            />
            {{ a.text }}
          </label>
        </div>
      </div>

      <button
        @click="submit"
        :disabled="submitting || !allAnswered"
        class="inline-flex items-center gap-2 px-5 py-2.5 text-sm font-medium text-white bg-gradient-to-r from-emerald-500 to-emerald-600 rounded-xl hover:from-emerald-600 hover:to-emerald-700 transition disabled:opacity-50 disabled:cursor-not-allowed shadow-lg shadow-emerald-500/25"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
        {{ submitting ? 'Отправка...' : 'Завершить тест' }}
      </button>
      <p v-if="!allAnswered" class="text-xs text-gray-400 dark:text-gray-500">Ответьте на все вопросы, чтобы завершить тест.</p>
      <p v-if="submitError" class="text-sm text-red-500">{{ submitError }}</p>
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
  quiz: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['updated', 'deleted'])

const authStore = useAuthStore()
const { apiFetch } = useApi()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const answers = ref({})
const submitting = ref(false)
const removing = ref(false)
const submitError = ref('')

const allAnswered = computed(() => {
  if (!props.quiz?.questions?.length) return false
  return props.quiz.questions.every((q) => answers.value[q.id])
})

const scoreClass = computed(() => {
  const pct = props.quiz.total ? props.quiz.score / props.quiz.total : 0
  if (pct >= 0.8) return 'bg-emerald-100 dark:bg-emerald-900/40 text-emerald-600 dark:text-emerald-400'
  if (pct >= 0.5) return 'bg-yellow-100 dark:bg-yellow-900/40 text-yellow-600 dark:text-yellow-400'
  return 'bg-red-100 dark:bg-red-900/40 text-red-600 dark:text-red-400'
})

const isMyAnswer = (q, a) => {
  return String(props.quiz.my_answers?.[q.id]) === String(a.id)
}

const answerClass = (q, a) => {
  if (a.is_correct) {
    return 'bg-emerald-50 dark:bg-emerald-900/20 text-emerald-700 dark:text-emerald-300'
  }
  if (isMyAnswer(q, a)) {
    return 'bg-red-50 dark:bg-red-900/20 text-red-700 dark:text-red-300'
  }
  return 'text-gray-600 dark:text-gray-400'
}

const submit = async () => {
  submitting.value = true
  submitError.value = ''
  try {
    const res = await apiFetch(`${API_URL}/posts/${props.postId}/quiz/submit/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ answers: answers.value })
    })
    if (res.ok) {
      const data = await res.json()
      emit('updated', data)
    } else {
      const data = await res.json().catch(() => ({}))
      submitError.value = data.detail || 'Не удалось отправить ответы'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    submitError.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}

const removeQuiz = async () => {
  if (!confirm('Удалить тест? Все результаты прохождений будут потеряны.')) return
  removing.value = true
  try {
    const res = await apiFetch(`${API_URL}/posts/${props.postId}/`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ quiz: null })
    })
    if (res.ok) {
      emit('deleted')
    } else {
      alert('Не удалось удалить тест')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    removing.value = false
  }
}
</script>
