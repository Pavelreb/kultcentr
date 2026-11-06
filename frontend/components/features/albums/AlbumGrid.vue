<!-- frontend/components/features/albums/AlbumGrid.vue -->
<template>
  <div>
    <!-- Заголовок списка -->
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-xl font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"/>
        </svg>
        <span>Все альбомы</span>
        <span class="text-sm text-gray-400 dark:text-gray-500 bg-gray-100 dark:bg-gray-700 px-2.5 py-0.5 rounded-full">
          {{ totalItems }}
        </span>
      </h2>
    </div>
    
    <!-- Состояние загрузки - 15 скелетонов (3 ряда × 5) -->
    <div v-if="loading" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
      <div 
        v-for="i in 15" 
        :key="i" 
        class="bg-gray-200 dark:bg-gray-700 rounded-xl animate-pulse overflow-hidden aspect-square"
      >
        <div class="w-full h-full bg-gray-300 dark:bg-gray-600"></div>
      </div>
    </div>
    
    <!-- Нет альбомов -->
    <div v-else-if="totalItems === 0" class="text-center py-12 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет альбомов</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>
    
    <!-- Сетка альбомов -->
    <div v-else>
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
        <GalleryAlbumCard 
          v-for="album in currentPageItems" 
          :key="album.id" 
          :album="album" 
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
import GalleryAlbumCard from './GalleryAlbumCard.vue'
import Pagination from '~/components/ui/Pagination.vue'

const props = defineProps({
  albums: {
    type: Array,
    default: () => []
  },
  loading: {
    type: Boolean,
    default: false
  },
  itemsPerPage: {
    type: Number,
    default: 15
  }
})

const currentPage = ref(1)

const totalItems = computed(() => props.albums.length)
const totalPages = computed(() => {
  return Math.ceil(totalItems.value / props.itemsPerPage)
})

const currentPageItems = computed(() => {
  const start = (currentPage.value - 1) * props.itemsPerPage
  const end = start + props.itemsPerPage
  return props.albums.slice(start, end)
})

const onPageChange = (page) => {
  if (page === currentPage.value) return
  currentPage.value = page
}

watch(() => props.albums, () => {
  currentPage.value = 1
}, { deep: true })
</script>