<!-- frontend/components/features/events/EventCard.vue -->
<template>
  <NuxtLink 
    :to="`/events/${event.id}`" 
    class="group relative block bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden hover:-translate-y-1 aspect-[9/16]"
  >
    <!-- Изображение -->
    <div class="absolute inset-0">
      <img 
        v-if="event.display_image" 
        :src="event.display_image" 
        :alt="event.title"
        class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
        loading="lazy"
      />
      <div 
        v-else 
        class="w-full h-full bg-gradient-to-br from-purple-400 via-pink-400 to-blue-500 flex items-center justify-center"
      >
        <svg class="w-16 h-16 text-white/50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
        </svg>
      </div>
      
      <!-- Сложный градиент для лучшей читаемости -->
      <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 via-50% to-transparent"></div>
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black/20"></div>
    </div>
    
    <!-- Бейджи (сверху) -->
    <div class="absolute top-3 left-3 right-3 flex flex-wrap gap-2 z-10">
      <!-- Бейдж "Сегодня" или "Скоро" -->
      <div 
        v-if="isToday || isSoon" 
        class="px-3 py-1 rounded-full text-xs font-semibold shadow-lg backdrop-blur-md"
        :class="isToday ? 'bg-gradient-to-r from-rose-500 to-red-600 text-white' : 'bg-gradient-to-r from-amber-400 to-orange-500 text-white'"
      >
        <span class="flex items-center gap-1.5">
          <svg v-if="isToday" class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          <svg v-else class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 10V3L4 14h7v7l9-11h-7z"/>
          </svg>
          {{ isToday ? 'Сегодня' : 'Скоро' }}
        </span>
      </div>
      
      <!-- Бейдж "Черновик" -->
      <div 
        v-if="!event.is_published" 
        class="px-3 py-1 rounded-full text-xs font-semibold bg-gradient-to-r from-yellow-400 to-yellow-500 text-black shadow-lg backdrop-blur-md"
      >
        <span class="flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
          </svg>
          Черновик
        </span>
      </div>
    </div>
    
    <!-- Контент поверх изображения (снизу) -->
    <div class="absolute bottom-0 left-0 right-0 p-5 z-10">
      <!-- Заголовок -->
      <h3 class="text-lg md:text-xl font-bold text-white leading-tight line-clamp-2 group-hover:text-blue-300 transition-colors drop-shadow-lg">
        {{ event.title }}
      </h3>
      
      <!-- Описание -->
      <p class="text-sm text-white/80 mt-1.5 line-clamp-2 drop-shadow-md font-light">
        <RichText :text="event.excerpt || event.content || ''" compact />
      </p>
      
      <!-- Разделитель с градиентом -->
      <div class="my-3 h-px bg-gradient-to-r from-white/30 via-white/10 to-transparent"></div>
      
      <!-- Детали (дата и место) с современными цветами -->
      <div class="flex flex-wrap items-center gap-2 text-xs text-white">
        <!-- Дата -->
        <span 
          v-if="event.event_date" 
          class="flex items-center gap-1.5 px-3 py-1 rounded-full backdrop-blur-md border shadow-lg"
          :class="isToday 
            ? 'bg-gradient-to-r from-rose-500/40 to-red-600/40 border-rose-400/30 text-white' 
            : 'bg-gradient-to-r from-blue-500/40 to-indigo-600/40 border-blue-400/30 text-white'"
        >
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
          {{ formatDate(event.event_date) }}
        </span>
        
        <!-- Место -->
        <span 
          v-if="event.location" 
          class="flex items-center gap-1.5 px-3 py-1 rounded-full backdrop-blur-md border shadow-lg bg-gradient-to-r from-emerald-500/40 to-teal-600/40 border-emerald-400/30 text-white"
        >
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
          </svg>
          {{ event.location.length > 15 ? event.location.substring(0, 15) + '…' : event.location }}
        </span>
      </div>
      
      <!-- Индикатор "Подробнее" при наведении -->
      <div class="mt-3 flex items-center gap-2 text-xs font-medium text-white/60 group-hover:text-white transition-all duration-300 opacity-0 group-hover:opacity-100 translate-y-1 group-hover:translate-y-0">
        <span>Подробнее</span>
        <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
        </svg>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
import RichText from '~/components/common/RichText.vue'
const props = defineProps({
  event: {
    type: Object,
    required: true
  }
})

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'short'
  })
}

const isToday = computed(() => {
  if (!props.event.event_date) return false
  const eventDate = new Date(props.event.event_date)
  const today = new Date()
  return eventDate.toDateString() === today.toDateString()
})

const isSoon = computed(() => {
  if (!props.event.event_date || isToday.value) return false
  const eventDate = new Date(props.event.event_date)
  const today = new Date()
  const diffDays = Math.ceil((eventDate - today) / (1000 * 60 * 60 * 24))
  return diffDays > 0 && diffDays <= 3
})
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>