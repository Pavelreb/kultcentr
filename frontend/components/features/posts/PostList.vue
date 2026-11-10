<!-- frontend/components/features/posts/PostList.vue -->
<template>
  <div ref="rootEl" class="scroll-mt-20">
    <!-- Заголовок списка -->
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-xl font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"/>
        </svg>
        <span>Все публикации</span>
        <span class="text-sm text-gray-400 dark:text-gray-500 bg-gray-100 dark:bg-gray-700 px-2.5 py-0.5 rounded-full">
          {{ totalItems }}
        </span>
      </h2>
    </div>
    
    <!-- Состояние загрузки -->
    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div 
        v-for="i in itemsPerPage" 
        :key="i" 
        class="bg-gray-200 dark:bg-gray-700 rounded-xl animate-pulse overflow-hidden"
      >
        <div class="aspect-video bg-gray-300 dark:bg-gray-600"></div>
        <div class="p-5 space-y-3">
          <div class="h-6 bg-gray-300 dark:bg-gray-600 rounded w-3/4"></div>
          <div class="h-4 bg-gray-300 dark:bg-gray-600 rounded w-full"></div>
          <div class="h-4 bg-gray-300 dark:bg-gray-600 rounded w-2/3"></div>
          <div class="flex gap-2 pt-2">
            <div class="h-6 bg-gray-300 dark:bg-gray-600 rounded-full w-16"></div>
            <div class="h-6 bg-gray-300 dark:bg-gray-600 rounded-full w-16"></div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Нет постов -->
    <div v-else-if="totalItems === 0" class="text-center py-12 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет публикаций</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>
    
    <!-- Список постов -->
    <div v-else>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <PostListItem 
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
  </div>
</template>

<script setup>
import PostListItem from './PostListItem.vue'
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
    default: 9
  },
  showDraftBadge: {
    type: Boolean,
    default: true
  }
})

const route = useRoute()
const router = useRouter()

// Номер страницы живёт в URL (?page=N): переживает «назад» и F5
const currentPage = ref(Number(route.query.page) || 1)

const totalItems = computed(() => props.posts.length)
const totalPages = computed(() => {
  return Math.ceil(totalItems.value / props.itemsPerPage)
})

const currentPageItems = computed(() => {
  const start = (currentPage.value - 1) * props.itemsPerPage
  const end = start + props.itemsPerPage
  return props.posts.slice(start, end)
})

const rootEl = ref(null)

const onPageChange = (page) => {
  if (page === currentPage.value) return
  currentPage.value = page
  router.replace({ query: { ...route.query, page: String(page) } })
  // Скролл — в watch на route.query.page ниже: он сработает после перерисовки DOM
}

// Реагируем на кнопки браузера «вперёд/назад» и на смену страницы:
// flush: 'post' — скроллим ПОСЛЕ перерисовки DOM (успевает скрыться «Главная новость»)
watch(() => route.query.page, (newPage) => {
  const page = Number(newPage) || 1
  if (page !== currentPage.value) {
    currentPage.value = page
  }
  // На первой странице цель — «Главная новость» наверху, иначе — начало списка
  if (page === 1) {
    smoothScrollTo(0)
  } else {
    smoothScrollToElement(rootEl.value)
  }
}, { flush: 'post' })

let initialLoad = true
watch(() => props.posts, () => {
  if (initialLoad) {
    initialLoad = false
    return
  }
  currentPage.value = 1
  router.replace({ query: { ...route.query, page: '1' } })
}, { deep: true })
</script>