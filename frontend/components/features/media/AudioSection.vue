<!-- frontend/components/features/media/AudioSection.vue -->
<template>
  <section ref="rootEl" class="py-4 scroll-mt-20">
    <!-- Заголовок секции -->
    <div class="flex justify-between items-center mb-6">
      <div class="flex items-center gap-3">
        <div class="w-1 h-8 bg-teal-500 rounded-full"></div>
        <NuxtLink to="/media/audio" class="hover:opacity-75 transition-opacity">
        <h2 class="text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2">
          <svg class="w-8 h-8 text-teal-500 dark:text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/>
          </svg>
          Аудиозаписи
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
        to="/media/audio"
        class="group hidden min-[460px]:inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-teal-600 dark:text-teal-400 bg-teal-50 dark:bg-teal-900/20 rounded-xl hover:bg-teal-100 dark:hover:bg-teal-900/30 transition-all duration-300 hover:shadow-md hover:-translate-y-0.5"
      >
        <span>Все аудио</span>
        <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
        </svg>
      </NuxtLink>
    </div>

    <!-- Состояние загрузки -->
    <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <div v-for="i in perPage" :key="i" class="bg-white dark:bg-gray-800 rounded-xl shadow-md p-4 animate-pulse">
        <div class="flex items-center gap-3 mb-3">
          <div class="w-12 h-12 rounded-lg bg-gray-200 dark:bg-gray-700"></div>
          <div class="flex-1 space-y-2">
            <div class="h-3 bg-gray-200 dark:bg-gray-700 rounded"></div>
            <div class="h-2 w-1/2 bg-gray-200 dark:bg-gray-700 rounded"></div>
          </div>
        </div>
        <div class="h-2 bg-gray-200 dark:bg-gray-700 rounded-full"></div>
      </div>
    </div>

    <!-- Нет аудио -->
    <div v-else-if="totalItems === 0" class="text-center py-12 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет аудиозаписей</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>

    <!-- Сетка аудио (карусель при пагинации) -->
    <div v-else class="relative carousel-viewport">
      <Transition :name="slideName">
        <div :key="currentPage" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-5">
          <AudioCard
            v-for="item in currentPageItems"
            :key="item.id"
            :audio="item"
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
import AudioCard from './AudioCard.vue'
import Pagination from '~/components/ui/Pagination.vue'

const props = defineProps({
  audios: {
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
const slideName = ref('slide-left')

const totalItems = computed(() => props.audios.length)
// Адаптивное количество: <640px — 4, 640–1023px — 4, ≥1024px — itemsPerPage
const tier = ref(2)
onMounted(() => {
  const update = () => {
    const w = window.innerWidth
    tier.value = w >= 1024 ? 2 : w >= 640 ? 1 : 0
  }
  update()
  window.addEventListener('resize', update)
})
const perPage = computed(() => [4, 4, props.itemsPerPage][tier.value])
watch(perPage, () => { currentPage.value = 1 })

const totalPages = computed(() => Math.ceil(totalItems.value / perPage.value))

const currentPageItems = computed(() => {
  const start = (currentPage.value - 1) * perPage.value
  return props.audios.slice(start, start + perPage.value)
})

const rootEl = ref(null)

const onPageChange = (page) => {
  if (page === currentPage.value) return
  slideName.value = page > currentPage.value ? 'slide-left' : 'slide-right'
  currentPage.value = page
  smoothScrollToElement(rootEl.value)
}

watch(() => props.audios, () => {
  currentPage.value = 1
}, { deep: true })
</script>
