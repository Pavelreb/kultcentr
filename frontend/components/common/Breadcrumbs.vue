<!-- frontend/components/common/Breadcrumbs.vue -->
<template>
  <nav class="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400" aria-label="Хлебные крошки">
    <!-- Главная -->
    <NuxtLink 
      to="/" 
      class="flex items-center gap-1.5 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
    >
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1h-2z"/>
      </svg>
      <span class="hidden sm:inline">Главная</span>
    </NuxtLink>
    
    <!-- Если есть items, отображаем их все -->
    <template v-if="items && items.length > 0">
      <template v-for="(item, index) in items" :key="index">
        <!-- Разделитель перед каждым элементом (кроме первого) -->
        <svg 
          v-if="index === 0"
          class="w-4 h-4 flex-shrink-0 text-gray-400 dark:text-gray-600" 
          fill="none" 
          stroke="currentColor" 
          viewBox="0 0 24 24"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
        
        <!-- Ссылка -->
        <NuxtLink 
          v-if="item.to"
          :to="item.to" 
          class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors truncate"
        >
          {{ item.label }}
        </NuxtLink>
        
        <!-- Текст без ссылки -->
        <span 
          v-else
          class="truncate"
        >
          {{ item.label }}
        </span>
        
        <!-- Разделитель после элемента (кроме последнего, если есть currentPageName) -->
        <svg 
          v-if="index < items.length - 1 || (index === items.length - 1 && currentPageName)"
          class="w-4 h-4 flex-shrink-0 text-gray-400 dark:text-gray-600" 
          fill="none" 
          stroke="currentColor" 
          viewBox="0 0 24 24"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </template>
    </template>
    
    <!-- Если есть currentPageName, отображаем его как последнюю крошку -->
    <span 
      v-if="currentPageName"
      class="text-gray-700 dark:text-gray-300 font-medium truncate"
    >
      {{ currentPageName }}
    </span>
  </nav>
</template>

<script setup>
const props = defineProps({
  items: {
    type: Array,
    default: () => []
  },
  currentPageName: {
    type: String,
    default: ''
  }
})
</script>