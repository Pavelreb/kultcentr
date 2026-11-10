<!-- frontend/components/features/posts/PostSection.vue -->
<template>
  <section class="py-4">
    <!-- Заголовок секции -->
    <div class="flex justify-between items-center mb-6">
      <div class="flex items-center gap-3">
        <div class="w-1 h-8 bg-green-500 rounded-full"></div>
        <NuxtLink to="/posts" class="hover:opacity-75 transition-opacity">
        <h2 class="text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2">
          <svg class="w-8 h-8 text-green-500 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
          </svg>
          Публикации
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
        to="/posts" 
        class="group inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-green-600 dark:text-green-400 bg-green-50 dark:bg-green-900/20 rounded-xl hover:bg-green-100 dark:hover:bg-green-900/30 transition-all duration-300 hover:shadow-md hover:-translate-y-0.5"
      >
        <span>Все публикации</span>
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
    <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-5">
      <SkeletonCard v-for="i in itemsPerPage" :key="i" />
    </div>
    
    <!-- Нет публикаций -->
    <div v-else-if="totalItems === 0" class="text-center py-12 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет публикаций</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>
    
    <!-- Сетка карточек -->
    <div v-else>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-5">
        <PostCard 
          v-for="post in currentPageItems" 
          :key="post.id" 
          :post="post"
          :show-draft-badge="showDraftBadge"
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
import PostCard from './PostCard.vue'
import SkeletonCard from '~/components/ui/SkeletonCard.vue'
import Pagination from '~/components/ui/Pagination.vue'

const props = defineProps({
  posts: {
    type: Array,
    default: () => []
  },
  loading: {
    type: Boolean,
    default: false
  },
  itemsPerPage: {
    type: Number,
    default: 4
  },
  showDraftBadge: {
    type: Boolean,
    default: true
  }
})

const currentPage = ref(1)

// Только опубликованные посты
const publishedPosts = computed(() => {
  return props.posts.filter(p => p.is_published)
})

const totalItems = computed(() => publishedPosts.value.length)
const totalPages = computed(() => {
  return Math.ceil(totalItems.value / props.itemsPerPage)
})

const currentPageItems = computed(() => {
  const start = (currentPage.value - 1) * props.itemsPerPage
  const end = start + props.itemsPerPage
  return publishedPosts.value.slice(start, end)
})

const onPageChange = (page) => {
  if (page === currentPage.value) return
  currentPage.value = page
}

watch(() => props.posts, () => {
  currentPage.value = 1
}, { deep: true })
</script>