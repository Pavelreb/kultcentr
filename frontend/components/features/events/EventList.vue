<!-- frontend/components/features/events/EventList.vue -->
<template>
  <div>
    <!-- Заголовок списка -->
    <h2 class="text-xl font-semibold text-gray-700 dark:text-gray-300 mb-4 flex items-center gap-2">
      <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"/>
      </svg>
      <span>Все события</span>
      <span class="text-sm text-gray-400 dark:text-gray-500 bg-gray-100 dark:bg-gray-700 px-2.5 py-0.5 rounded-full">
        {{ events.length }}
      </span>
    </h2>
    
    <!-- Состояние загрузки -->
    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div 
        v-for="i in 4" 
        :key="i" 
        class="bg-gray-200 dark:bg-gray-700 rounded-xl animate-pulse overflow-hidden"
      >
        <div class="h-48 bg-gray-300 dark:bg-gray-600"></div>
        <div class="p-5 space-y-3">
          <div class="h-6 bg-gray-300 dark:bg-gray-600 rounded w-3/4"></div>
          <div class="h-4 bg-gray-300 dark:bg-gray-600 rounded w-full"></div>
          <div class="h-4 bg-gray-300 dark:bg-gray-600 rounded w-2/3"></div>
          <div class="flex gap-2 pt-2">
            <div class="h-6 bg-gray-300 dark:bg-gray-600 rounded-full w-20"></div>
            <div class="h-6 bg-gray-300 dark:bg-gray-600 rounded-full w-20"></div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Нет событий -->
    <div v-else-if="events.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-lg shadow">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Остальные события скоро появятся</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>
    
    <!-- Список событий - 2 колонки -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <EventListItem 
        v-for="event in events" 
        :key="event.id" 
        :event="event"
        :show-draft-badge="showDraftBadge"
      />
    </div>
  </div>
</template>

<script setup>
import EventListItem from './EventListItem.vue'

const props = defineProps({
  events: {
    type: Array,
    default: () => []
  },
  loading: {
    type: Boolean,
    default: false
  },
  showDraftBadge: {
    type: Boolean,
    default: true
  }
})
</script>