<!-- frontend/components/common/NotificationBell.vue -->
<!-- Колокольчик с количеством непрочитанных уведомлений -->
<template>
  <NuxtLink
    v-if="authStore.isAuthenticated"
    to="/notifications"
    class="relative p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition text-gray-600 dark:text-gray-300"
    aria-label="Уведомления"
    title="Уведомления"
  >
    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>
    </svg>
    <span
      v-if="unread > 0"
      class="absolute -top-0.5 -right-0.5 min-w-[18px] h-[18px] px-1 rounded-full bg-red-500 text-white text-[10px] font-bold flex items-center justify-center"
    >
      {{ unread > 99 ? '99+' : unread }}
    </span>
  </NuxtLink>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const authStore = useAuthStore()
const { apiFetch } = useApi()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const unread = ref(0)
let timer = null

const fetchUnread = async () => {
  if (!authStore.isAuthenticated) return
  try {
    const res = await apiFetch(`${API_URL}/notifications/unread-count/`)
    if (res.ok) {
      unread.value = (await res.json()).unread_count || 0
    }
  } catch (e) {
    // тихо игнорируем — бейдж не критичен
  }
}

onMounted(() => {
  authStore.restoreAuth()
  fetchUnread()
  timer = setInterval(fetchUnread, 60000)
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
})
</script>
