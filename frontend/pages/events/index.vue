<!-- frontend/pages/events/index.vue -->
<template>
  <div class="container mx-auto p-4">
    <!-- Хлебные крошки -->
    <Breadcrumbs 
      :items="breadcrumbItems" 
      class="mb-6"
    />
    
    <!-- ========================================== -->
    <!-- ГЛАВНОЕ СОБЫТИЕ                           -->
    <!-- ========================================== -->
    <FeaturedEvent :event="featuredEvent" />
    
    <!-- ========================================== -->
    <!-- СПИСОК ВСЕХ СОБЫТИЙ                       -->
    <!-- ========================================== -->
    <EventList 
      :events="remainingEvents" 
      :loading="loading"
    />
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import Breadcrumbs from '~/components/common/Breadcrumbs.vue'

useSeoMeta({
  title: 'Афиша',
  description: 'Афиша мероприятий центра культуры: концерты, спектакли, выставки, мастер-классы.'
})
import FeaturedEvent from '~/components/features/events/FeaturedEvent.vue'
import EventList from '~/components/features/events/EventList.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()
const events = ref([])
const loading = ref(true)

// Хлебные крошки — на странице афиши последняя крошка "Афиша"
const breadcrumbItems = [
  { label: 'Афиша' }
]

// Главная афиша: выбранная редактором, иначе — самое ближайшее событие
const featuredEvent = computed(() => {
  if (events.value.length === 0) return null

  const manual = events.value.find(e => e.is_featured && e.is_published)
  if (manual) return manual

  const sorted = [...events.value]
    .filter(e => e.is_published)
    .sort((a, b) => {
      if (!a.event_date) return 1
      if (!b.event_date) return -1
      return new Date(a.event_date) - new Date(b.event_date)
    })

  return sorted.length > 0 ? sorted[0] : events.value[0]
})

// Список событий без главного
const remainingEvents = computed(() => {
  if (!featuredEvent.value) return events.value
  return events.value.filter(e => e.id !== featuredEvent.value.id)
})

onMounted(() => {
  authStore.restoreAuth()
})

onMounted(async () => {
  try {
    const res = await apiFetch(`${API_URL}/events/`)
    events.value = await res.json()
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>