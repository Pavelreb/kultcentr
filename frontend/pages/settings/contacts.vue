<!-- frontend/pages/settings/contacts.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-orange-500 dark:text-orange-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
        </svg>
        Контакты
      </h1>
      <NuxtLink
        to="/settings"
        class="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 hover:-translate-y-0.5"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
        </svg>
        Все настройки
      </NuxtLink>
    </div>

    <div v-if="!authStore.isEditor" class="bg-white dark:bg-gray-800 p-8 rounded-lg shadow text-center py-20">
      <svg class="w-24 h-24 mx-auto text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
      </svg>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут управлять настройками сайта.</p>
    </div>

    <div v-else class="bg-white dark:bg-gray-800 rounded-xl shadow-md p-6 border border-gray-100 dark:border-gray-700">
      <p class="text-sm text-gray-500 dark:text-gray-400 mb-6">
        Эти данные отображаются на странице «Контакты» и в подвале сайта.
      </p>

      <div v-if="loading" class="text-center py-10 text-gray-500 dark:text-gray-400">
        Загрузка…
      </div>

      <form v-else @submit.prevent="save" class="space-y-5">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Адрес</label>
            <input v-model="form.address" type="text" required
              class="w-full px-4 py-2.5 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 focus:ring-2 focus:ring-orange-500 focus:border-transparent transition" />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Телефон</label>
            <input v-model="form.phone" type="text" required
              class="w-full px-4 py-2.5 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 focus:ring-2 focus:ring-orange-500 focus:border-transparent transition" />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Email</label>
            <input v-model="form.email" type="email" required
              class="w-full px-4 py-2.5 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 focus:ring-2 focus:ring-orange-500 focus:border-transparent transition" />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Часы работы</label>
            <input v-model="form.work_hours" type="text" required
              class="w-full px-4 py-2.5 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 focus:ring-2 focus:ring-orange-500 focus:border-transparent transition" />
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Описание</label>
          <textarea v-model="form.description" rows="3"
            class="w-full px-4 py-2.5 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 focus:ring-2 focus:ring-orange-500 focus:border-transparent transition"></textarea>
        </div>

        <div class="border-t border-gray-200 dark:border-gray-700 pt-5">
          <h3 class="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">Социальные сети (необязательно)</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">ВКонтакте</label>
              <input v-model="form.vk" type="url" placeholder="https://vk.com/…"
                class="w-full px-4 py-2.5 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 focus:ring-2 focus:ring-orange-500 focus:border-transparent transition" />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">MAX</label>
              <input v-model="form.max" type="url" placeholder="https://max.ru/…"
                class="w-full px-4 py-2.5 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 focus:ring-2 focus:ring-orange-500 focus:border-transparent transition" />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Одноклассники</label>
              <input v-model="form.ok" type="url" placeholder="https://ok.ru/…"
                class="w-full px-4 py-2.5 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 focus:ring-2 focus:ring-orange-500 focus:border-transparent transition" />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">RuTube</label>
              <input v-model="form.rutube" type="url" placeholder="https://rutube.ru/…"
                class="w-full px-4 py-2.5 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 focus:ring-2 focus:ring-orange-500 focus:border-transparent transition" />
            </div>
          </div>
        </div>

        <div class="flex items-center gap-4 pt-2">
          <button
            type="submit"
            :disabled="saving"
            class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-orange-500 to-orange-600 text-white rounded-xl hover:from-orange-600 hover:to-orange-700 transition-all duration-300 font-medium shadow-lg shadow-orange-500/25 hover:shadow-xl hover:shadow-orange-500/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0"
          >
            {{ saving ? 'Сохранение…' : 'Сохранить' }}
          </button>
          <span v-if="message" class="text-sm" :class="messageError ? 'text-red-500' : 'text-green-600 dark:text-green-400'">
            {{ message }}
          </span>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: ['auth', 'editor']
})

useSeoMeta({
  title: 'Настройки контактов'
})

const authStore = useAuthStore()
const { apiFetch } = useApi()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const loading = ref(true)
const saving = ref(false)
const message = ref('')
const messageError = ref(false)

const form = ref({
  address: '',
  phone: '',
  email: '',
  work_hours: '',
  description: '',
  vk: '',
  max: '',
  ok: '',
  rutube: ''
})

const loadContacts = async () => {
  loading.value = true
  try {
    const res = await apiFetch(`${API_URL}/contact-info/`)
    if (res.ok) {
      const data = await res.json()
      form.value = {
        address: data.address || '',
        phone: data.phone || '',
        email: data.email || '',
        work_hours: data.work_hours || '',
        description: data.description || '',
        vk: data.vk || '',
        max: data.max || '',
        ok: data.ok || '',
        rutube: data.rutube || ''
      }
    }
  } catch (e) {
    console.error('Ошибка загрузки контактов:', e)
  } finally {
    loading.value = false
  }
}

const save = async () => {
  saving.value = true
  message.value = ''
  try {
    const res = await apiFetch(`${API_URL}/contact-info/update/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form.value)
    })
    if (!res.ok) {
      const data = await res.json().catch(() => ({}))
      throw new Error(data.detail || 'Ошибка сохранения')
    }
    messageError.value = false
    message.value = 'Сохранено'
    // Обновляем контакты в подвале сайта
    window.dispatchEvent(new Event('contacts-updated'))
  } catch (e) {
    messageError.value = true
    message.value = e.message || 'Ошибка сохранения'
  } finally {
    saving.value = false
  }
}

onMounted(() => {
  authStore.restoreAuth()
  loadContacts()
})
</script>
