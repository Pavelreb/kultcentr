<!-- frontend/pages/notifications.vue -->
<template>
  <div class="max-w-3xl mx-auto mt-10 px-4 pb-16">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>
        </svg>
        Уведомления
      </h1>
      <button
        v-if="unreadCount > 0"
        @click="markAllRead"
        class="text-sm text-blue-600 dark:text-blue-400 hover:underline"
      >
        Прочитать все
      </button>
    </div>

    <div v-if="loading" class="text-center py-20">
      <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>

    <div v-else-if="!notifications.length" class="text-center py-20 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700">
      <svg class="w-16 h-16 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Уведомлений пока нет</p>
    </div>

    <div v-else class="space-y-2">
      <component
        :is="n.link ? 'NuxtLink' : 'div'"
        v-for="n in notifications"
        :key="n.id"
        :to="n.link || undefined"
        @click="markRead(n)"
        class="flex items-start gap-3 p-4 rounded-xl border transition cursor-pointer"
        :class="n.is_read
          ? 'bg-white dark:bg-gray-800 border-gray-100 dark:border-gray-700'
          : 'bg-blue-50 dark:bg-blue-900/20 border-blue-200 dark:border-blue-800 hover:bg-blue-100 dark:hover:bg-blue-900/30'"
      >
        <!-- Иконка по типу -->
        <div
          class="w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0"
          :class="iconBgClass(n.type)"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="n.type === 'subscription'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/>
            <path v-else-if="n.type === 'comment'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
            <path v-else-if="n.type === 'like'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            <path v-else-if="n.type === 'new_post'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6"/>
          </svg>
        </div>

        <div class="flex-1 min-w-0">
          <p class="text-sm" :class="n.is_read ? 'text-gray-600 dark:text-gray-400' : 'text-gray-900 dark:text-white font-medium'">
            {{ n.text }}
          </p>
          <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">
            {{ n.type_display }} · {{ formatDateTime(n.created_at) }}
          </p>
        </div>

        <span v-if="!n.is_read" class="w-2.5 h-2.5 rounded-full bg-blue-500 flex-shrink-0 mt-1.5"></span>
      </component>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: 'auth'
})

useSeoMeta({
  title: 'Уведомления'
})

const authStore = useAuthStore()
const { apiFetch } = useApi()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const notifications = ref([])
const unreadCount = ref(0)
const loading = ref(true)

const iconBgClass = (type) => {
  switch (type) {
    case 'subscription': return 'bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400'
    case 'comment': return 'bg-blue-100 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400'
    case 'like': return 'bg-red-100 dark:bg-red-900/30 text-red-500 dark:text-red-400'
    case 'new_post': return 'bg-green-100 dark:bg-green-900/30 text-green-600 dark:text-green-400'
    default: return 'bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400'
  }
}

const formatDateTime = (dateString) => {
  if (!dateString) return ''
  return new Date(dateString).toLocaleString('ru-RU', {
    day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit'
  })
}

const markRead = async (n) => {
  if (n.is_read) return
  n.is_read = true
  unreadCount.value = Math.max(0, unreadCount.value - 1)
  apiFetch(`${API_URL}/notifications/${n.id}/read/`, { method: 'POST' }).catch(() => {})
}

const markAllRead = async () => {
  notifications.value.forEach((n) => { n.is_read = true })
  unreadCount.value = 0
  apiFetch(`${API_URL}/notifications/read-all/`, { method: 'POST' }).catch(() => {})
}

onMounted(async () => {
  authStore.restoreAuth()
  try {
    const res = await apiFetch(`${API_URL}/notifications/`)
    if (res.ok) {
      const data = await res.json()
      notifications.value = data.results || []
      unreadCount.value = data.unread_count || 0
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>
