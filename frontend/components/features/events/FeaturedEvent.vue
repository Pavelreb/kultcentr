<!-- frontend/components/features/events/FeaturedEvent.vue -->
<template>
  <div v-if="event" class="mb-10">
    <div class="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden shadow-xl border border-gray-100 dark:border-gray-700">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-0">
        <!-- Левая колонка: Изображение как афиша -->
        <div class="relative flex items-center justify-center p-4 md:p-6 bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-800 dark:to-gray-900">
          <div class="relative aspect-[9/16] w-full max-w-[320px] md:max-w-[360px] rounded-2xl overflow-hidden shadow-2xl ring-1 ring-black/5 dark:ring-white/5">
            <img 
              v-if="event.display_image" 
              :src="event.display_image" 
              :alt="event.title"
              class="w-full h-full object-cover"
            />
            <div v-else class="w-full h-full flex items-center justify-center bg-gradient-to-br from-blue-600 to-purple-700">
              <svg class="w-24 h-24 text-white/30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
              </svg>
            </div>
            
            <!-- Бейджи поверх афиши -->
            <div class="absolute top-3 left-3 right-3 flex flex-wrap gap-2 z-10">
              <div class="px-3 py-1 rounded-full text-xs font-semibold bg-gradient-to-r from-amber-400 to-yellow-500 text-black shadow-lg backdrop-blur-md">
                <span class="flex items-center gap-1.5">
                  <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/>
                  </svg>
                  ГЛАВНОЕ СОБЫТИЕ
                </span>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Правая колонка: Информация -->
        <div class="p-6 md:p-8 lg:p-10 flex flex-col justify-center">
          <!-- Заголовок -->
          <h2 class="text-2xl md:text-3xl lg:text-4xl font-bold text-gray-900 dark:text-white mb-3 leading-tight">
            {{ event.title }}
          </h2>
          
          <!-- Описание -->
          <p class="text-gray-600 dark:text-gray-300 text-sm md:text-base leading-relaxed mb-4 line-clamp-3">
            <RichText :text="event.excerpt || event.content || ''" compact />
          </p>
          
          <!-- Детали события -->
          <div class="space-y-3 mb-6">
            <div v-if="event.event_date" class="flex items-center gap-3 text-sm text-gray-600 dark:text-gray-300">
              <div class="w-8 h-8 rounded-full bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-4 h-4 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Дата и время</span>
                <p class="font-medium">{{ formatDate(event.event_date) }}</p>
              </div>
            </div>
            
            <div v-if="event.location" class="flex items-center gap-3 text-sm text-gray-600 dark:text-gray-300">
              <div class="w-8 h-8 rounded-full bg-emerald-100 dark:bg-emerald-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-4 h-4 text-emerald-600 dark:text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Место проведения</span>
                <p class="font-medium">{{ event.location }}</p>
              </div>
            </div>
            
            <div v-if="event.price" class="flex items-center gap-3 text-sm text-gray-600 dark:text-gray-300">
              <div class="w-8 h-8 rounded-full bg-amber-100 dark:bg-amber-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-4 h-4 text-amber-600 dark:text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Стоимость</span>
                <p class="font-medium text-green-600 dark:text-green-400">{{ event.price }}</p>
              </div>
            </div>
          </div>
          
          <!-- Кнопки -->
          <div class="flex flex-wrap gap-3">
            <NuxtLink 
              :to="`/events/${event.id}`" 
              class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5"
            >
              Подробнее о событии
              <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
              </svg>
            </NuxtLink>
            
            <NuxtLink 
              v-if="event.button_link"
              :to="event.button_link"
              class="inline-flex items-center gap-2 px-6 py-3 bg-transparent border-2 border-blue-500 text-blue-600 dark:text-blue-400 rounded-xl hover:bg-blue-50 dark:hover:bg-blue-900/20 transition-all duration-300 font-medium hover:-translate-y-0.5"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"/>
              </svg>
              Купить билет
            </NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import RichText from '~/components/common/RichText.vue'
const props = defineProps({
  event: {
    type: Object,
    default: null
  }
})

const formatDate = (dateString) => {
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
</script>