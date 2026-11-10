<!-- frontend/components/features/authors/AuthorSection.vue -->
<template>
  <section ref="rootEl" class="py-4 scroll-mt-20">
    <!-- Заголовок секции -->
    <div class="flex justify-between items-center mb-6">
      <div class="flex items-center gap-3">
        <div class="w-1 h-8 bg-purple-500 rounded-full"></div>
        <NuxtLink to="/authors" class="hover:opacity-75 transition-opacity">
        <h2 class="text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2">
          <svg class="w-8 h-8 text-purple-500 dark:text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
          </svg>
          Авторы
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
        to="/authors" 
        class="group hidden min-[460px]:inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-purple-600 dark:text-purple-400 bg-purple-50 dark:bg-purple-900/20 rounded-xl hover:bg-purple-100 dark:hover:bg-purple-900/30 transition-all duration-300 hover:shadow-md hover:-translate-y-0.5"
      >
        <span>Все авторы</span>
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
    <div v-if="loading" class="grid grid-cols-2 max-[420px]:grid-cols-1 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4">
      <div 
        v-for="i in perPage" 
        :key="i" 
        class="bg-gray-200 dark:bg-gray-700 rounded-xl animate-pulse p-5 text-center"
      >
        <div class="w-20 h-20 mx-auto rounded-full bg-gray-300 dark:bg-gray-600"></div>
        <div class="h-4 bg-gray-300 dark:bg-gray-600 rounded w-24 mx-auto mt-3"></div>
        <div class="h-3 bg-gray-300 dark:bg-gray-600 rounded w-20 mx-auto mt-1"></div>
        <div class="flex justify-center gap-4 mt-3 pt-3">
          <div class="text-center">
            <div class="h-3 bg-gray-300 dark:bg-gray-600 rounded w-8 mx-auto"></div>
            <div class="h-2 bg-gray-300 dark:bg-gray-600 rounded w-12 mx-auto mt-1"></div>
          </div>
          <div class="text-center">
            <div class="h-3 bg-gray-300 dark:bg-gray-600 rounded w-8 mx-auto"></div>
            <div class="h-2 bg-gray-300 dark:bg-gray-600 rounded w-12 mx-auto mt-1"></div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Нет авторов -->
    <div v-else-if="totalItems === 0" class="text-center py-12 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет авторов</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>
    
    <!-- Сетка авторов (карусель при пагинации) -->
    <div v-else class="relative carousel-viewport">
      <Transition :name="slideName">
        <div :key="currentPage" class="grid grid-cols-2 max-[420px]:grid-cols-1 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4 md:gap-5">
          <AuthorCard
            v-for="author in currentPageItems"
            :key="author.id"
            :author="author"
          />
        </div>
      </Transition>
      
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
import AuthorCard from './AuthorCard.vue'
import Pagination from '~/components/ui/Pagination.vue'

const props = defineProps({
  authors: {
    type: Array,
    default: () => []
  },
  loading: {
    type: Boolean,
    default: false
  },
  itemsPerPage: {
    type: Number,
    default: 6
  }
})

const currentPage = ref(1)

// Направление карусели: вперёд — влево, назад — вправо
const slideName = ref('slide-left')

const totalItems = computed(() => props.authors.length)
// Адаптивное количество: <420px — 2, 420–639px — 2, 640–767px — 3, 768–1023px — 4, ≥1024px — itemsPerPage
const tier = ref(4)
onMounted(() => {
  const update = () => {
    const w = window.innerWidth
    tier.value = w >= 1024 ? 4 : w >= 768 ? 3 : w >= 640 ? 2 : w >= 420 ? 1 : 0
  }
  update()
  window.addEventListener('resize', update)
})
const perPage = computed(() => [2, 2, 3, 4, props.itemsPerPage][tier.value])
watch(perPage, () => { currentPage.value = 1 })

const totalPages = computed(() => {
  return Math.ceil(totalItems.value / perPage.value)
})

const currentPageItems = computed(() => {
  const start = (currentPage.value - 1) * perPage.value
  const end = start + perPage.value
  return props.authors.slice(start, end)
})

const rootEl = ref(null)

const onPageChange = (page) => {
  if (page === currentPage.value) return
  slideName.value = page > currentPage.value ? 'slide-left' : 'slide-right'
  currentPage.value = page
  // Мягкий скролл к началу списка при смене страницы
  smoothScrollToElement(rootEl.value)
}

watch(() => props.authors, () => {
  currentPage.value = 1
}, { deep: true })
</script>