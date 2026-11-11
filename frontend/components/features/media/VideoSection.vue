<!-- frontend/components/features/media/VideoSection.vue -->
<template>
  <section ref="rootEl" class="py-4 scroll-mt-20">
    <!-- Заголовок секции -->
    <div class="flex justify-between items-center mb-6">
      <div class="flex items-center gap-3">
        <div class="w-1 h-8 bg-rose-500 rounded-full"></div>
        <NuxtLink to="/media/videos" class="hover:opacity-75 transition-opacity">
        <h2 class="text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2">
          <svg class="w-8 h-8 text-rose-500 dark:text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/>
          </svg>
          Видеоролики
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
        to="/media/videos"
        class="group hidden min-[460px]:inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-900/20 rounded-xl hover:bg-rose-100 dark:hover:bg-rose-900/30 transition-all duration-300 hover:shadow-md hover:-translate-y-0.5"
      >
        <span>Все видео</span>
        <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
        </svg>
      </NuxtLink>
    </div>

    <!-- Состояние загрузки -->
    <div v-if="loading" class="grid grid-cols-2 max-[420px]:grid-cols-1 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
      <div v-for="i in perPage" :key="i" class="bg-white dark:bg-gray-800 rounded-xl shadow-md overflow-hidden animate-pulse">
        <div class="aspect-video bg-gray-200 dark:bg-gray-700"></div>
        <div class="p-3 space-y-2">
          <div class="h-3 bg-gray-200 dark:bg-gray-700 rounded"></div>
          <div class="h-2 w-1/2 bg-gray-200 dark:bg-gray-700 rounded"></div>
        </div>
      </div>
    </div>

    <!-- Нет видео -->
    <div v-else-if="totalItems === 0" class="text-center py-12 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет видеороликов</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>

    <!-- Сетка видео (карусель при пагинации) -->
    <div v-else class="relative carousel-viewport">
      <Transition :name="slideName">
        <div :key="currentPage" class="grid grid-cols-2 max-[420px]:grid-cols-1 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 md:gap-5">
          <VideoCard
            v-for="video in currentPageItems"
            :key="video.id"
            :video="video"
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
import VideoCard from './VideoCard.vue'
import Pagination from '~/components/ui/Pagination.vue'

const props = defineProps({
  videos: {
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
const slideName = ref('slide-left')

const totalItems = computed(() => props.videos.length)
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

const totalPages = computed(() => Math.ceil(totalItems.value / perPage.value))

const currentPageItems = computed(() => {
  const start = (currentPage.value - 1) * perPage.value
  return props.videos.slice(start, start + perPage.value)
})

const rootEl = ref(null)

const onPageChange = (page) => {
  if (page === currentPage.value) return
  slideName.value = page > currentPage.value ? 'slide-left' : 'slide-right'
  currentPage.value = page
  smoothScrollToElement(rootEl.value)
}

watch(() => props.videos, () => {
  currentPage.value = 1
}, { deep: true })
</script>
