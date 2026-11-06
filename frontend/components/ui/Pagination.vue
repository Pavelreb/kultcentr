<!-- frontend/components/ui/Pagination.vue -->
<template>
  <div v-if="totalPages > 1" class="flex items-center justify-center gap-1 mt-6">
    <!-- Кнопка "Назад" -->
    <button
      @click="goToPage(currentPage - 1)"
      :disabled="currentPage === 1"
      class="px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200 disabled:opacity-40 disabled:cursor-not-allowed"
      :class="currentPage === 1 
        ? 'text-gray-400 dark:text-gray-600 bg-gray-100 dark:bg-gray-800' 
        : 'text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white'"
    >
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
      </svg>
    </button>
    
    <!-- Номера страниц -->
    <div class="flex gap-1">
      <button
        v-if="showFirstDots"
        @click="goToPage(1)"
        class="px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white"
      >
        1
      </button>
      
      <span v-if="showFirstDots" class="px-2 py-2 text-gray-400 dark:text-gray-600">…</span>
      
      <button
        v-for="page in visiblePages"
        :key="page"
        @click="goToPage(page)"
        class="px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200"
        :class="page === currentPage
          ? 'bg-gradient-to-r from-blue-500 to-blue-600 text-white shadow-lg shadow-blue-500/25 scale-105'
          : 'text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white'"
      >
        {{ page }}
      </button>
      
      <span v-if="showLastDots" class="px-2 py-2 text-gray-400 dark:text-gray-600">…</span>
      
      <button
        v-if="showLastDots"
        @click="goToPage(totalPages)"
        class="px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white"
      >
        {{ totalPages }}
      </button>
    </div>
    
    <!-- Кнопка "Вперёд" -->
    <button
      @click="goToPage(currentPage + 1)"
      :disabled="currentPage === totalPages"
      class="px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200 disabled:opacity-40 disabled:cursor-not-allowed"
      :class="currentPage === totalPages 
        ? 'text-gray-400 dark:text-gray-600 bg-gray-100 dark:bg-gray-800' 
        : 'text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white'"
    >
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
      </svg>
    </button>
  </div>
</template>

<script setup>
const props = defineProps({
  currentPage: {
    type: Number,
    required: true,
    default: 1
  },
  totalPages: {
    type: Number,
    required: true,
    default: 1
  },
  maxVisible: {
    type: Number,
    default: 5
  }
})

const emit = defineEmits(['page-change'])

const showFirstDots = computed(() => {
  return props.currentPage > Math.ceil(props.maxVisible / 2) + 1
})

const showLastDots = computed(() => {
  return props.currentPage < props.totalPages - Math.ceil(props.maxVisible / 2)
})

const visiblePages = computed(() => {
  const total = props.totalPages
  const current = props.currentPage
  const maxVisible = props.maxVisible
  
  if (total <= maxVisible) {
    return Array.from({ length: total }, (_, i) => i + 1)
  }
  
  let start = Math.max(1, current - Math.floor(maxVisible / 2))
  let end = Math.min(total, start + maxVisible - 1)
  
  if (end - start + 1 < maxVisible) {
    start = Math.max(1, end - maxVisible + 1)
  }
  
  return Array.from({ length: end - start + 1 }, (_, i) => start + i)
})

const goToPage = (page) => {
  if (page < 1 || page > props.totalPages || page === props.currentPage) return
  emit('page-change', page)
}
</script>