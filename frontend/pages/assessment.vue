<!-- frontend/pages/assessment.vue -->
<template>
  <div class="max-w-2xl mx-auto mt-10 px-4">
    <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3 mb-2">
      <svg class="w-8 h-8 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/>
      </svg>
      Оценка учреждения
    </h1>
    <p class="text-sm text-gray-500 dark:text-gray-400 mb-6">
      Оцените работу нашего учреждения по шкале от 1 (плохо) до 5 (отлично). Опрос анонимный по желанию — достаточно электронной почты. Регистрация не требуется.
    </p>

    <!-- Загрузка вопросов -->
    <div v-if="loading" class="text-center py-16">
      <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>

    <!-- Успешная отправка -->
    <div v-else-if="sent" class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-8 text-center">
      <svg class="w-16 h-16 mx-auto text-emerald-500 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
      <p class="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-1">Спасибо за участие!</p>
      <p class="text-sm text-gray-500 dark:text-gray-400">Ваша оценка поможет нам стать лучше.</p>
    </div>

    <form v-else @submit.prevent="submit" class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-6 space-y-6">
      <!-- Вопросы с оценками 1–5 -->
      <div
        v-for="(q, qi) in questions"
        :key="q.key"
        class="pb-5 border-b border-gray-100 dark:border-gray-700 last:border-0 last:pb-0"
      >
        <p class="text-sm font-medium text-gray-800 dark:text-gray-200 mb-3">{{ qi + 1 }}. {{ q.text }}</p>
        <div class="flex gap-2">
          <label
            v-for="n in 5"
            :key="n"
            class="flex-1 cursor-pointer"
          >
            <input
              type="radio"
              :name="`q-${q.key}`"
              :value="n"
              v-model.number="ratings[q.key]"
              class="sr-only"
            />
            <span
              class="flex items-center justify-center h-10 rounded-xl border text-sm font-semibold transition"
              :class="ratings[q.key] === n
                ? 'bg-amber-500 border-amber-500 text-white shadow-lg shadow-amber-500/25'
                : 'border-gray-300 dark:border-gray-600 text-gray-500 dark:text-gray-400 hover:border-amber-400 hover:text-amber-500'"
            >
              {{ n }}
            </span>
          </label>
        </div>
      </div>

      <!-- Контактные поля -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-1.5 text-sm font-medium">
            Электронная почта <span class="text-red-500">*</span>
          </label>
          <input
            v-model="email"
            type="email"
            placeholder="you@example.com"
            required
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-amber-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          />
        </div>
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-1.5 text-sm font-medium">
            Ф.И.О. <span class="text-xs font-normal text-gray-400 dark:text-gray-500">(по желанию)</span>
          </label>
          <input
            v-model="fullName"
            type="text"
            placeholder="Иванов Иван Иванович"
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-amber-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          />
        </div>
      </div>

      <div>
        <label class="block text-gray-700 dark:text-gray-300 mb-1.5 text-sm font-medium">
          Комментарий <span class="text-red-500">*</span>
        </label>
        <textarea
          v-model="text"
          placeholder="Расскажите подробнее: что понравилось, что можно улучшить..."
          rows="4"
          required
          class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-amber-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
        ></textarea>
      </div>

      <button
        type="submit"
        :disabled="submitting || !allRated"
        class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-amber-500 to-orange-500 text-white rounded-xl hover:from-amber-600 hover:to-orange-600 transition-all duration-300 font-medium shadow-lg shadow-amber-500/25 hover:shadow-xl hover:shadow-amber-500/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/>
        </svg>
        {{ submitting ? 'Отправка...' : 'Отправить оценку' }}
      </button>
      <p v-if="!allRated" class="text-xs text-gray-400 dark:text-gray-500">Поставьте оценку на каждый вопрос.</p>

      <p v-if="error" class="text-red-500 text-sm flex items-center gap-1.5">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
        </svg>
        {{ error }}
      </p>
    </form>
  </div>
</template>

<script setup>
useSeoMeta({
  title: 'Оценка учреждения',
  description: 'Независимая оценка качества работы учреждения культуры: оцените нас по шкале от 1 до 5.'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const questions = ref([])
const ratings = ref({})
const email = ref('')
const fullName = ref('')
const text = ref('')
const loading = ref(true)
const submitting = ref(false)
const sent = ref(false)
const error = ref('')

const allRated = computed(() =>
  questions.value.length > 0 && questions.value.every((q) => ratings.value[q.key] >= 1)
)

onMounted(async () => {
  try {
    const res = await fetch(`${API_URL}/assessment/questions/`)
    if (res.ok) {
      questions.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})

const submit = async () => {
  submitting.value = true
  error.value = ''
  try {
    const res = await fetch(`${API_URL}/assessment/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: email.value.trim(),
        full_name: fullName.value.trim(),
        text: text.value.trim(),
        ratings: ratings.value
      })
    })
    if (res.ok) {
      sent.value = true
    } else {
      const data = await res.json().catch(() => ({}))
      error.value = data.detail || data.ratings?.[0] || data.email?.[0] || data.text?.[0] || 'Не удалось отправить оценку'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}
</script>
