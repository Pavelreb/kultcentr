<!-- frontend/components/features/albums/AlbumDetail.vue -->
<template>
  <div v-if="album">
    <!-- Основной блок -->
    <div class="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden shadow-xl border border-gray-100 dark:border-gray-700">
      <!-- Верхняя часть: обложка слева, информация справа -->
      <div class="flex flex-col md:flex-row">
        <!-- Левая колонка: Обложка как плакат -->
        <div class="relative w-full md:w-[280px] lg:w-[320px] flex-shrink-0 aspect-[9/16] md:aspect-auto md:min-h-[400px] overflow-hidden bg-gradient-to-br from-pink-400 via-purple-400 to-blue-500">
          <img 
            v-if="album.cover_image_url" 
            :src="album.cover_image_url" 
            :alt="album.title"
            class="w-full h-full object-cover"
          />
          <div v-else class="w-full h-full flex items-center justify-center">
            <svg class="w-24 h-24 text-white/30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
          </div>
          
          <!-- Бейджи на обложке -->
          <div v-if="!album.is_published" class="absolute top-3 left-3 px-3 py-1 rounded-full text-xs font-semibold bg-yellow-500 text-black shadow-lg backdrop-blur-md">
            Черновик
          </div>
        </div>
        
        <!-- Правая колонка: Информация -->
        <div class="flex-1 p-6 md:p-8 lg:p-10 flex flex-col justify-center">
          <h1 class="text-2xl md:text-3xl lg:text-4xl font-bold text-gray-900 dark:text-white mb-3">
            {{ album.title }}
          </h1>
          
          <p v-if="album.description" class="text-gray-600 dark:text-gray-400 mb-6 text-base leading-relaxed">
            {{ album.description }}
          </p>
          
          <div class="space-y-4">
            <div class="flex items-center gap-4 text-sm text-gray-600 dark:text-gray-300">
              <div class="w-12 h-12 rounded-full bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Дата события</span>
                <p class="font-semibold text-base">{{ formatDate(album.date) }}</p>
              </div>
            </div>
            
            <div class="flex items-center gap-4 text-sm text-gray-600 dark:text-gray-300">
              <div class="w-12 h-12 rounded-full bg-pink-100 dark:bg-pink-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-pink-600 dark:text-pink-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Количество фото</span>
                <p class="font-semibold text-base">{{ album.photos_count || 0 }} фотографий</p>
              </div>
            </div>
            
            <div v-if="album.created_at" class="flex items-center gap-4 text-sm text-gray-600 dark:text-gray-300">
              <div class="w-12 h-12 rounded-full bg-green-100 dark:bg-green-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Создан</span>
                <p class="font-semibold text-base">{{ formatDate(album.created_at) }}</p>
              </div>
            </div>
          </div>
          
          <!-- Кнопки действий (только "Редактировать альбом") -->
          <div v-if="authStore.isEditor" class="mt-8 pt-6 border-t border-gray-100 dark:border-gray-700">
            <NuxtLink 
              :to="`/gallery/edit-${album.id}`" 
              class="inline-flex items-center gap-2 px-5 py-2.5 text-sm font-medium text-gray-600 dark:text-gray-400 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 hover:text-gray-900 dark:hover:text-white transition-all duration-300"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
              </svg>
              Редактировать альбом
            </NuxtLink>
          </div>
        </div>
      </div>
      
      <!-- Сетка фотографий (без кнопки удаления) -->
      <div v-if="album.photos && album.photos.length > 0" class="p-6 md:p-8 border-t border-gray-100 dark:border-gray-700">
        <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4 flex items-center gap-2">
          <svg class="w-5 h-5 text-pink-500 dark:text-pink-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
          Фотографии
        </h2>
        
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
          <div 
            v-for="(photo, index) in album.photos" 
            :key="photo.id"
            class="relative aspect-square bg-gray-200 dark:bg-gray-700 rounded-lg overflow-hidden cursor-pointer group"
            @click="openLightbox(index)"
          >
            <img 
              :src="photo.thumbnail_url || photo.image_url" 
              :alt="photo.caption || 'Фотография'"
              class="w-full h-full object-cover group-hover:scale-105 transition duration-500"
              loading="lazy"
            />
            
            <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/70 to-transparent p-2 opacity-0 group-hover:opacity-100 transition">
              <div class="flex items-center gap-3 text-white text-xs">
                <span class="flex items-center gap-1">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                  </svg>
                  {{ photo.views || 0 }}
                </span>
                <span class="flex items-center gap-1">
                  <svg class="w-3.5 h-3.5" :class="photo.user_has_liked ? 'text-red-500 fill-red-500' : ''" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                  </svg>
                  {{ photo.likes_count || 0 }}
                </span>
                <span class="flex items-center gap-1">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
                  </svg>
                  {{ photo.comments_count || 0 }}
                </span>
              </div>
            </div>
            
            <!-- ❌ УБРАЛИ кнопку удаления фотографии -->
            
            <div v-if="photo.caption" class="absolute bottom-0 left-0 right-0 bg-black bg-opacity-60 text-white text-xs p-2 truncate">
              {{ photo.caption }}
            </div>
          </div>
        </div>
      </div>
      
      <div v-else class="p-6 md:p-8 text-center border-t border-gray-100 dark:border-gray-700">
        <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
        </svg>
        <p class="text-gray-500 dark:text-gray-400">В этом альбоме пока нет фотографий</p>
      </div>
    </div>
    
    <!-- Навигация: Назад к списку -->
    <div class="mt-6 px-4">
      <NuxtLink to="/gallery" class="inline-flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 transition">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
        </svg>
        Назад к альбомам
      </NuxtLink>
    </div>
    
    <!-- Lightbox -->
    <Lightbox 
      v-if="album.photos && album.photos.length > 0"
      :photos="album.photos"
      :album-id="album.id"
      :initial-index="lightboxIndex"
      :is-open="lightboxOpen"
      @close="closeLightbox"
      @photo-updated="onPhotoUpdated"
    />
  </div>
  
  <!-- Состояние загрузки -->
  <div v-else-if="loading" class="text-center py-20">
    <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
    </svg>
    <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
  </div>
  
  <!-- Альбом не найден -->
  <div v-else class="text-center py-20">
    <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
    </svg>
    <p class="text-gray-500 dark:text-gray-400">Альбом не найден</p>
    <NuxtLink to="/gallery" class="mt-4 inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-pink-500 to-pink-600 text-white rounded-xl hover:from-pink-600 hover:to-pink-700 transition-all duration-300 font-medium shadow-lg shadow-pink-500/25 hover:shadow-xl hover:shadow-pink-500/40 hover:-translate-y-0.5">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
      </svg>
      Вернуться к альбомам
    </NuxtLink>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import Lightbox from '~/components/Lightbox.vue'

const authStore = useAuthStore()

const props = defineProps({
  album: {
    type: Object,
    default: null
  },
  loading: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['delete'])

const router = useRouter()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

// Lightbox state
const lightboxOpen = ref(false)
const lightboxIndex = ref(0)

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

const openLightbox = (index) => {
  lightboxIndex.value = index
  lightboxOpen.value = true
  document.body.style.overflow = 'hidden'
}

const closeLightbox = () => {
  lightboxOpen.value = false
  document.body.style.overflow = ''
}

const onPhotoUpdated = (updatedPhoto) => {
  const photoIndex = props.album.photos.findIndex(p => p.id === updatedPhoto.id)
  if (photoIndex !== -1) {
    props.album.photos[photoIndex] = updatedPhoto
  }
}
</script>