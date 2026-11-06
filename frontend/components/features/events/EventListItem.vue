<!-- frontend/components/features/events/EventListItem.vue -->
<template>
  <NuxtLink 
    :to="`/events/${event.id}`" 
    class="group bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden hover:-translate-y-1 block"
  >
    <div class="grid grid-cols-1 sm:grid-cols-3">
      <!-- Левая колонка: Изображение (вертикальное) с минимальной высотой -->
      <div class="relative aspect-[9/16] sm:aspect-auto sm:min-h-[280px] md:min-h-[320px] lg:min-h-[360px] overflow-hidden bg-gradient-to-br from-blue-600 to-purple-700">
        <img 
          v-if="event.display_image" 
          :src="event.display_image" 
          :alt="event.title" 
          class="w-full h-full object-cover group-hover:scale-105 transition duration-500"
          loading="lazy"
        />
        <div v-else class="w-full h-full flex items-center justify-center">
          <svg class="w-16 h-16 text-white/30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
          </svg>
        </div>
        
        <!-- Бейджи поверх изображения -->
        <div class="absolute top-2 left-2 right-2 flex flex-wrap gap-1.5 z-10">
          <span 
            v-if="!event.is_published && showDraftBadge"
            class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-yellow-400 text-black shadow-lg backdrop-blur-md"
          >
            Черновик
          </span>
        </div>
      </div>
      
      <!-- Правая колонка: Информация -->
      <div class="col-span-2 p-5 flex flex-col justify-center">
        <!-- Заголовок -->
        <h2 class="text-xl font-bold text-gray-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400 transition line-clamp-2">
          {{ event.title }}
        </h2>
        
        <!-- Описание -->
        <p class="text-gray-600 dark:text-gray-300 text-sm mt-1.5 line-clamp-2">
          {{ event.excerpt || event.content?.substring(0, 120) }}...
        </p>
        
        <!-- Детали -->
        <div class="flex flex-wrap gap-2 mt-3 text-sm text-gray-500 dark:text-gray-400">
          <!-- Дата -->
          <span v-if="event.event_date" class="flex items-center gap-1.5 bg-gray-50 dark:bg-gray-700/50 px-2.5 py-1 rounded-full">
            <svg class="w-3.5 h-3.5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            {{ formatDate(event.event_date) }}
          </span>
          
          <!-- Место -->
          <span v-if="event.location" class="flex items-center gap-1.5 bg-gray-50 dark:bg-gray-700/50 px-2.5 py-1 rounded-full">
            <svg class="w-3.5 h-3.5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
            </svg>
            {{ event.location }}
          </span>
          
          <!-- Цена -->
          <span v-if="event.price" class="flex items-center gap-1.5 bg-green-50 dark:bg-green-900/20 px-2.5 py-1 rounded-full text-green-600 dark:text-green-400">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            {{ event.price }}
          </span>
        </div>
        
        <!-- ❌ УБРАЛИ: автора и бейдж "Опубликовано" -->
        
        <!-- Индикатор "Подробнее" при наведении -->
        <div class="mt-3 flex items-center gap-2 text-sm font-medium text-blue-600 dark:text-blue-400 opacity-0 group-hover:opacity-100 transition-all duration-300">
          <span>Подробнее</span>
          <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
          </svg>
        </div>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
const props = defineProps({
  event: {
    type: Object,
    required: true
  },
  showDraftBadge: {
    type: Boolean,
    default: true
  }
})

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'short',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>