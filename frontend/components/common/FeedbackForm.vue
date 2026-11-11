<!-- frontend/components/common/FeedbackForm.vue -->
<!-- Форма обратной связи: email и текст обязательны, Ф.И.О. — по желанию. Отправить может любой посетитель -->
<template>
  <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-6">
    <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 mb-2">
      <svg class="w-6 h-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
      </svg>
      Обратная связь
    </h2>
    <p class="text-sm text-gray-500 dark:text-gray-400 mb-5">
      Есть вопрос, предложение или замечание? Напишите нам — регистрация не требуется.
    </p>

    <!-- Успешная отправка -->
    <div v-if="sent" class="text-center py-8">
      <svg class="w-16 h-16 mx-auto text-emerald-500 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
      <p class="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-1">Сообщение отправлено!</p>
      <p class="text-sm text-gray-500 dark:text-gray-400 mb-4">Спасибо за обращение. Мы ответим на указанную почту.</p>
      <button
        @click="reset"
        class="text-sm text-blue-600 dark:text-blue-400 hover:underline"
      >
        Отправить ещё одно сообщение
      </button>
    </div>

    <form v-else @submit.prevent="submit" class="space-y-4">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-1.5 text-sm font-medium">
            Электронная почта <span class="text-red-500">*</span>
          </label>
          <input
            v-model="email"
            type="email"
            placeholder="you@example.com"
            required
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
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
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          />
        </div>
      </div>

      <div>
        <label class="block text-gray-700 dark:text-gray-300 mb-1.5 text-sm font-medium">
          Текст сообщения <span class="text-red-500">*</span>
        </label>
        <textarea
          v-model="text"
          placeholder="Ваш вопрос, предложение или замечание..."
          rows="5"
          required
          class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
        ></textarea>
      </div>

      <button
        type="submit"
        :disabled="submitting"
        class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/>
        </svg>
        {{ submitting ? 'Отправка...' : 'Отправить' }}
      </button>

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
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const email = ref('')
const fullName = ref('')
const text = ref('')
const submitting = ref(false)
const sent = ref(false)
const error = ref('')

const submit = async () => {
  submitting.value = true
  error.value = ''
  try {
    const res = await fetch(`${API_URL}/feedback/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: email.value.trim(),
        full_name: fullName.value.trim(),
        text: text.value.trim()
      })
    })
    if (res.ok) {
      sent.value = true
    } else {
      const data = await res.json().catch(() => ({}))
      error.value = data.detail || data.email?.[0] || data.text?.[0] || 'Не удалось отправить сообщение'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}

const reset = () => {
  email.value = ''
  fullName.value = ''
  text.value = ''
  sent.value = false
}
</script>
