<!-- frontend/pages/events/[id].vue -->
<template>
  <div class="container mx-auto p-4">
    <!-- Хлебные крошки -->
    <Breadcrumbs 
      :items="breadcrumbItems" 
      :current-page-name="event?.title || 'Загрузка...'"
      class="mb-6"
    />
    
    <!-- Детальная страница события -->
    <EventDetail 
      :event="event" 
      :loading="loading"
      @delete="handleDelete"
    />
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import Breadcrumbs from '~/components/common/Breadcrumbs.vue'
import EventDetail from '~/components/features/events/EventDetail.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const { apiFetch } = useApi()

const event = ref(null)
const loading = ref(true)

// Хлебные крошки: Афиша → Название события
const breadcrumbItems = [
  { label: 'Афиша', to: '/events' }
]

const handleDelete = async (eventId) => {
  try {
    const res = await apiFetch(`${API_URL}/events/${eventId}/`, {
      method: 'DELETE',
    })
    
    if (res.ok) {
      router.push('/events')
    } else {
      alert('Ошибка при удалении события')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  }
}

onMounted(() => {
  authStore.restoreAuth()
})

onMounted(async () => {
  try {
    const id = route.params.id
    const res = await apiFetch(`${API_URL}/events/${id}/`)
    
    if (res.ok) {
      event.value = await res.json()
    } else {
      router.push('/events')
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>