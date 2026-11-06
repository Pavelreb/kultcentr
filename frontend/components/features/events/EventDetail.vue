<!-- frontend/components/features/events/EventDetail.vue -->
<template>
  <div v-if="event" class="max-w-6xl mx-auto">
    <!-- Основной блок -->
    <div class="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden shadow-xl border border-gray-100 dark:border-gray-700">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-0">
        <!-- Левая колонка: Изображение -->
        <div class="relative aspect-[9/16] md:aspect-auto md:min-h-[400px] lg:min-h-[500px] overflow-hidden bg-gradient-to-br from-blue-600 to-purple-700">
          <img 
            v-if="event.display_image" 
            :src="event.display_image" 
            :alt="event.title"
            class="w-full h-full object-cover"
          />
          <div v-else class="w-full h-full flex items-center justify-center">
            <svg class="w-24 h-24 text-white/30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
            </svg>
          </div>
          
          <!-- Бейдж "Черновик" (только если черновик) -->
          <div v-if="!event.is_published" class="absolute top-3 left-3 px-3 py-1 rounded-full text-xs font-semibold bg-yellow-500 text-black shadow-lg backdrop-blur-md">
            Черновик
          </div>
        </div>
        
        <!-- Правая колонка: Информация -->
        <div class="p-6 md:p-8 lg:p-10 flex flex-col justify-center">
          <!-- Заголовок -->
          <h1 class="text-2xl md:text-3xl lg:text-4xl font-bold text-gray-900 dark:text-white mb-4 leading-tight">
            {{ event.title }}
          </h1>
          
          <!-- Описание -->
          <div class="prose prose-sm dark:prose-invert max-w-none mb-6">
            <p class="text-gray-600 dark:text-gray-300 leading-relaxed whitespace-pre-wrap">
              {{ event.content }}
            </p>
          </div>
          
          <!-- Детали события (увеличенные) -->
          <div class="space-y-4 mb-6">
            <!-- Дата и время -->
            <div v-if="event.event_date" class="flex items-center gap-4 text-base text-gray-700 dark:text-gray-200">
              <div class="w-12 h-12 rounded-full bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Дата и время</span>
                <p class="font-semibold text-lg">{{ formatDateTime(event.event_date) }}</p>
              </div>
            </div>
            
            <!-- Место проведения -->
            <div v-if="event.location" class="flex items-center gap-4 text-base text-gray-700 dark:text-gray-200">
              <div class="w-12 h-12 rounded-full bg-emerald-100 dark:bg-emerald-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-emerald-600 dark:text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Место проведения</span>
                <p class="font-semibold text-lg">{{ event.location }}</p>
              </div>
            </div>
            
            <!-- Стоимость -->
            <div v-if="event.price" class="flex items-center gap-4 text-base text-gray-700 dark:text-gray-200">
              <div class="w-12 h-12 rounded-full bg-amber-100 dark:bg-amber-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-amber-600 dark:text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Стоимость</span>
                <p class="font-semibold text-lg text-green-600 dark:text-green-400">{{ event.price }}</p>
              </div>
            </div>
          </div>
          
          <!-- Кнопки действий -->
          <div class="flex flex-wrap gap-3">
            <!-- Кнопка "Купить билет" (основная) -->
            <NuxtLink 
              v-if="event.button_link"
              :to="event.button_link"
              class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"/>
              </svg>
              Купить билет
            </NuxtLink>
            
            <!-- Кнопка "Редактировать" (менее заметная) -->
            <button 
              v-if="canEdit"
              @click="editEvent"
              class="inline-flex items-center gap-2 px-4 py-2.5 text-sm font-medium text-gray-600 dark:text-gray-400 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 hover:text-gray-900 dark:hover:text-white transition-all duration-300"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
              </svg>
              Редактировать
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Состояние загрузки -->
  <div v-else-if="loading" class="text-center py-20">
    <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
    </svg>
    <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
  </div>
  
  <!-- Событие не найдено -->
  <div v-else class="text-center py-20">
    <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
    </svg>
    <p class="text-gray-500 dark:text-gray-400">Событие не найдено</p>
    <NuxtLink to="/events" class="mt-4 inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
      </svg>
      Вернуться к афише
    </NuxtLink>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const authStore = useAuthStore()

const props = defineProps({
  event: {
    type: Object,
    default: null
  },
  loading: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['delete'])

const router = useRouter()

const formatDateTime = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const canEdit = computed(() => {
  if (!props.event) return false
  const user = authStore.user
  if (!user) return false
  return user.role === 'editor' || user.username === props.event.author_name
})

const editEvent = () => {
  router.push(`/events/edit-${props.event.id}`)
}

const deleteEvent = () => {
  if (confirm(`Вы уверены, что хотите удалить событие "${props.event.title}"?`)) {
    emit('delete', props.event.id)
  }
}
</script>