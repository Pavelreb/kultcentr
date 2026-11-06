<!-- frontend/components/features/albums/AlbumCard.vue -->
<template>
  <NuxtLink 
    :to="`/gallery/${album.id}`" 
    class="group relative block bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden hover:-translate-y-1 aspect-square"
  >
    <!-- Изображение -->
    <div class="absolute inset-0">
      <img 
        v-if="album.cover_image_url" 
        :src="album.cover_image_url" 
        :alt="album.title"
        class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
        loading="lazy"
      />
      <div v-else class="w-full h-full flex items-center justify-center bg-gradient-to-br from-pink-400 via-purple-400 to-blue-500">
        <svg class="w-16 h-16 text-white/50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        </svg>
      </div>
      
      <!-- Градиентное затемнение -->
      <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 via-40% to-transparent"></div>
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black/20"></div>
    </div>
    
    <!-- Бейджи (сверху) -->
    <div class="absolute top-3 left-3 right-3 flex flex-wrap gap-2 z-10">
      <!-- Бейдж "Новый" -->
      <div 
        v-if="isNew" 
        class="px-3 py-1 rounded-full text-xs font-semibold bg-gradient-to-r from-blue-500 to-indigo-600 text-white shadow-lg backdrop-blur-md"
      >
        <span class="flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          Новый
        </span>
      </div>
      
      <!-- Бейдж "Черновик" -->
      <div 
        v-if="!album.is_published" 
        class="px-3 py-1 rounded-full text-xs font-semibold bg-gradient-to-r from-yellow-400 to-yellow-500 text-black shadow-lg backdrop-blur-md"
      >
        <span class="flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
          </svg>
          Черновик
        </span>
      </div>
    </div>
    
    <!-- Количество фото (снизу справа) -->
    <div class="absolute bottom-3 right-3 z-10">
      <span class="flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-black/50 backdrop-blur-md border border-white/10 text-white shadow-lg">
        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        </svg>
        {{ album.photos_count || 0 }}
      </span>
    </div>
    
    <!-- Контент поверх изображения (снизу) -->
    <div class="absolute bottom-0 left-0 right-0 p-4 z-10">
      <!-- Заголовок -->
      <h3 class="text-base font-bold text-white leading-tight line-clamp-1 group-hover:text-pink-300 transition-colors drop-shadow-lg">
        {{ album.title }}
      </h3>
      
      <!-- Дата с иконкой -->
      <div class="flex items-center gap-1.5 mt-1.5 text-xs text-white/80">
        <svg class="w-3.5 h-3.5 text-white/60" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        </svg>
        {{ formatDate(album.date) }}
      </div>
      
      <!-- Описание (если есть) -->
      <p v-if="album.description" class="text-xs text-white/60 mt-1.5 line-clamp-1 drop-shadow-md">
        {{ album.description }}
      </p>
      
      <!-- Индикатор "Открыть альбом" при наведении -->
      <div class="mt-2 flex items-center gap-2 text-xs font-medium text-white/60 group-hover:text-white transition-all duration-300 opacity-0 group-hover:opacity-100 translate-y-1 group-hover:translate-y-0">
        <span>Открыть альбом</span>
        <svg class="w-3.5 h-3.5 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
        </svg>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
const props = defineProps({
  album: {
    type: Object,
    required: true
  }
})

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'short',
    year: 'numeric'
  })
}

// Проверяем, создан ли альбом сегодня
const isNew = computed(() => {
  if (!props.album.created_at) return false
  const albumDate = new Date(props.album.created_at)
  const today = new Date()
  return albumDate.toDateString() === today.toDateString()
})
</script>

<style scoped>
.line-clamp-1 {
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>