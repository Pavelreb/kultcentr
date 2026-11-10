<!-- frontend/components/features/events/EventSection.vue -->
<template>
  <section class="py-4">
    <!-- Заголовок секции -->
    <div class="flex justify-between items-center mb-6">
      <div class="flex items-center gap-3">
        <div class="w-1 h-8 bg-blue-500 rounded-full"></div>
        <NuxtLink to="/events" class="hover:opacity-75 transition-opacity">
        <h2 class="text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2">
          <svg class="w-8 h-8 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
          </svg>
          Афиша
        </h2>
        </NuxtLink>
        <span 
          v-if="totalItems > 0" 
          class="text-sm text-gray-400 dark:text-gray-500 bg-gray-100 dark:bg-gray-700 px-2.5 py-0.5 rounded-full"
        >
          {{ totalItems }}
        </span>
      </div>
      
      <NuxtLink 
        to="/events" 
        class="group inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-900/20 rounded-xl hover:bg-blue-100 dark:hover:bg-blue-900/30 transition-all duration-300 hover:shadow-md hover:-translate-y-0.5"
      >
        <span>Все события</span>
        <svg 
          class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" 
          fill="none" 
          stroke="currentColor" 
          viewBox="0 0 24 24"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
        </svg>
      </NuxtLink>
    </div>
    
    <!-- Состояние загрузки -->
    <div v-if="loading" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
      <SkeletonCard v-for="i in itemsPerPage" :key="i" />
    </div>
    
    <!-- Нет событий -->
    <div v-else-if="totalItems === 0" class="text-center py-12 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет событий</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>
    
    <!-- Сетка карточек -->
    <div v-else>
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 md:gap-5">
        <EventCard 
          v-for="event in currentPageItems" 
          :key="event.id" 
          :event="event" 
        />
      </div>
      
      <!-- Пагинация -->
      <Pagination
        :current-page="currentPage"
        :total-pages="totalPages"
        :max-visible="5"
        @page-change="onPageChange"
      />
    </div>
  </section>
</template>

<script setup>
import EventCard from './EventCard.vue'
import SkeletonCard from '~/components/ui/SkeletonCard.vue'
import Pagination from '~/components/ui/Pagination.vue'

const props = defineProps({
  events: {
    type: Array,
    default: () => []
  },
  loading: {
    type: Boolean,
    default: false
  },
  itemsPerPage: {
    type: Number,
    default: 5
  }
})

const currentPage = ref(1)

const totalItems = computed(() => props.events.length)
const totalPages = computed(() => {
  return Math.ceil(totalItems.value / props.itemsPerPage)
})

const currentPageItems = computed(() => {
  const start = (currentPage.value - 1) * props.itemsPerPage
  const end = start + props.itemsPerPage
  return props.events.slice(start, end)
})

const onPageChange = (page) => {
  if (page === currentPage.value) return
  currentPage.value = page
}

watch(() => props.events, () => {
  currentPage.value = 1
}, { deep: true })
</script>