<!-- frontend/pages/settings/featured-event.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-purple-500 dark:text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        </svg>
        Главная афиша
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
      <p class="text-sm text-gray-500 dark:text-gray-400 mb-4">
        Выбранное событие будет закреплено наверху страницы «Афиша».
        Показаны только опубликованные события.
      </p>

      <div v-if="loading" class="text-center py-10 text-gray-500 dark:text-gray-400">
        Загрузка…
      </div>

      <template v-else>
        <!-- Автоматический режим -->
        <label
          class="flex items-center gap-3 p-4 mb-3 rounded-xl border cursor-pointer transition-all duration-300"
          :class="selected === 'auto'
            ? 'border-purple-500 bg-purple-50 dark:bg-purple-900/20'
            : 'border-gray-200 dark:border-gray-700 hover:border-purple-300 dark:hover:border-purple-700'"
        >
          <input type="radio" v-model="selected" value="auto" class="w-4 h-4 text-purple-600" />
          <div>
            <div class="font-medium text-gray-800 dark:text-gray-200">Автоматически</div>
            <div class="text-xs text-gray-400 dark:text-gray-500">Главной становится ближайшая по дате афиша</div>
          </div>
        </label>

        <div v-if="events.length === 0" class="text-center py-6 text-gray-500 dark:text-gray-400">
          Нет опубликованных событий.
        </div>

        <div v-else class="space-y-3 max-h-[60vh] overflow-y-auto pr-1">
          <label
            v-for="event in events"
            :key="event.id"
            class="flex items-center gap-3 p-4 rounded-xl border cursor-pointer transition-all duration-300"
            :class="selected === event.id
              ? 'border-purple-500 bg-purple-50 dark:bg-purple-900/20'
              : 'border-gray-200 dark:border-gray-700 hover:border-purple-300 dark:hover:border-purple-700'"
          >
            <input type="radio" v-model="selected" :value="event.id" class="w-4 h-4 text-purple-600 flex-shrink-0" />
            <img
              v-if="event.display_image"
              :src="event.display_image"
              :alt="event.title"
              class="w-10 h-16 object-cover rounded-lg flex-shrink-0"
            />
            <div class="min-w-0">
              <div class="font-medium text-gray-800 dark:text-gray-200 truncate">{{ event.title }}</div>
              <div class="text-xs text-gray-400 dark:text-gray-500">
                {{ formatDate(event.event_date) }}<template v-if="event.location"> · {{ event.location }}</template>
                <span v-if="event.is_featured" class="ml-1 text-purple-600 dark:text-purple-400 font-medium">· сейчас главная</span>
              </div>
            </div>
          </label>
        </div>

        <div class="mt-6 flex items-center gap-4">
          <button
            @click="save"
            :disabled="saving"
            class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-purple-500 to-purple-600 text-white rounded-xl hover:from-purple-600 hover:to-purple-700 transition-all duration-300 font-medium shadow-lg shadow-purple-500/25 hover:shadow-xl hover:shadow-purple-500/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0"
          >
            {{ saving ? 'Сохранение…' : 'Сохранить' }}
          </button>
          <span v-if="message" class="text-sm" :class="messageError ? 'text-red-500' : 'text-green-600 dark:text-green-400'">
            {{ message }}
          </span>
        </div>
      </template>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: ['auth', 'editor']
})

useSeoMeta({
  title: 'Главная афиша'
})

const authStore = useAuthStore()
const { apiFetch } = useApi()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const events = ref([])
const loading = ref(true)
const saving = ref(false)
const selected = ref('auto')
const message = ref('')
const messageError = ref(false)

const formatDate = (dateStr) => {
  if (!dateStr) return 'Дата не указана'
  return new Date(dateStr).toLocaleDateString('ru-RU', {
    day: 'numeric', month: 'long', year: 'numeric'
  })
}

const loadEvents = async () => {
  loading.value = true
  try {
    const res = await apiFetch(`${API_URL}/events/`)
    events.value = await res.json()
    const current = events.value.find(e => e.is_featured)
    selected.value = current ? current.id : 'auto'
  } catch (e) {
    console.error('Ошибка загрузки событий:', e)
  } finally {
    loading.value = false
  }
}

const save = async () => {
  saving.value = true
  message.value = ''
  try {
    const url = selected.value === 'auto'
      ? `${API_URL}/events/unfeature/`
      : `${API_URL}/events/${selected.value}/feature/`
    const res = await apiFetch(url, { method: 'POST' })
    if (!res.ok) {
      const data = await res.json().catch(() => ({}))
      throw new Error(data.detail || 'Ошибка сохранения')
    }
    messageError.value = false
    message.value = 'Сохранено'
    await loadEvents()
  } catch (e) {
    messageError.value = true
    message.value = e.message || 'Ошибка сохранения'
  } finally {
    saving.value = false
  }
}

onMounted(() => {
  authStore.restoreAuth()
  loadEvents()
})
</script>
