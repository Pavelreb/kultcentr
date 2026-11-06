<!-- frontend/components/Lightbox.vue -->
<template>
  <Teleport to="body">
    <div 
      v-if="isOpen" 
      class="fixed inset-0 z-[9999] bg-black/95 backdrop-blur-lg transition-opacity duration-300 flex flex-col overflow-hidden"
      @click="closeOnBackdrop"
    >
      <!-- Верхняя панель -->
      <div class="flex-shrink-0 flex items-center justify-between px-4 py-3 md:px-6 md:py-4 z-20">
        <div class="flex items-center gap-3">
          <span class="px-3 py-1 rounded-full bg-white/10 backdrop-blur-md text-white text-sm font-medium border border-white/10">
            {{ currentIndex + 1 }} / {{ photos.length }}
          </span>
        </div>
        
        <button 
          @click="closeLightbox"
          class="p-2 rounded-full bg-white/10 hover:bg-white/20 text-white transition-all duration-300 hover:scale-110"
          aria-label="Закрыть"
        >
          <svg class="w-6 h-6 md:w-7 md:h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>

      <!-- Основной контент - фото -->
      <div class="flex-1 flex items-center justify-center relative px-4 md:px-8 overflow-hidden min-h-0">
        <!-- Кнопка "Назад" -->
        <button 
          v-if="photos.length > 1"
          @click="prevPhoto"
          class="absolute left-2 md:left-6 z-20 p-2 md:p-3 rounded-full bg-white/10 hover:bg-white/20 text-white transition-all duration-300 hover:scale-110 group"
          aria-label="Предыдущее фото"
        >
          <svg class="w-6 h-6 md:w-8 md:h-8 group-hover:-translate-x-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"/>
          </svg>
        </button>

        <!-- Изображение -->
        <div class="relative max-w-full max-h-full flex items-center justify-center group/image">
          <img 
            :src="currentPhoto?.image_url || currentPhoto?.thumbnail_url" 
            :alt="currentPhoto?.caption || 'Фотография'"
            class="max-w-full max-h-[65vh] md:max-h-[72vh] object-contain rounded-lg shadow-2xl transition-opacity duration-300 select-none"
            :class="isLoading ? 'opacity-0' : 'opacity-100'"
            @load="isLoading = false"
            draggable="false"
          />
          
          <!-- Лоадер -->
          <div v-if="isLoading" class="absolute inset-0 flex items-center justify-center">
            <svg class="w-12 h-12 text-white/40 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
            </svg>
          </div>
          
          <!-- Кнопка лайка по центру -->
          <button 
            v-if="authStore.isAuthenticated"
            @click="toggleLike"
            class="absolute inset-0 flex items-center justify-center opacity-0 group-hover/image:opacity-100 transition-all duration-300"
          >
            <div 
              class="p-4 md:p-5 rounded-full bg-white/10 backdrop-blur-sm hover:bg-white/20 transition-all duration-300 scale-90 group-hover/image:scale-100"
              :class="{ 'animate-like': isLiking }"
            >
              <svg 
                class="w-12 h-12 md:w-16 md:h-16 transition-all duration-300 drop-shadow-lg"
                :class="currentPhoto?.user_has_liked ? 'text-red-500 fill-red-500' : 'text-white fill-none hover:text-red-400'"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
              </svg>
            </div>
          </button>
          
          <!-- Счётчик лайков -->
          <div class="absolute bottom-3 right-3 md:bottom-4 md:right-4 px-3 py-1.5 rounded-full bg-black/50 backdrop-blur-md text-white text-sm flex items-center gap-1.5 border border-white/10">
            <svg class="w-4 h-4" :class="currentPhoto?.user_has_liked ? 'text-red-500 fill-red-500' : 'text-white'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <span>{{ currentPhoto?.likes_count || 0 }}</span>
          </div>
        </div>

        <!-- Кнопка "Вперёд" -->
        <button 
          v-if="photos.length > 1"
          @click="nextPhoto"
          class="absolute right-2 md:right-6 z-20 p-2 md:p-3 rounded-full bg-white/10 hover:bg-white/20 text-white transition-all duration-300 hover:scale-110 group"
          aria-label="Следующее фото"
        >
          <svg class="w-6 h-6 md:w-8 md:h-8 group-hover:translate-x-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"/>
          </svg>
        </button>
      </div>

      <!-- Нижняя панель -->
      <div class="flex-shrink-0 px-4 py-3 md:px-6 md:py-4 z-20 bg-gradient-to-t from-black/80 via-black/40 to-transparent max-h-[45vh] overflow-y-auto custom-scroll">
        <!-- Индикаторы точек -->
        <div v-if="photos.length > 1" class="flex justify-center gap-2 mb-3 sticky top-0 bg-black/20 backdrop-blur-sm py-2 -mx-4 px-4">
          <button
            v-for="(_, index) in photos"
            :key="index"
            @click="goToPhoto(index)"
            class="transition-all duration-300 rounded-full"
            :class="index === currentIndex 
              ? 'w-8 h-2 bg-white' 
              : 'w-2 h-2 bg-white/40 hover:bg-white/60'"
            :aria-label="`Перейти к фото ${index + 1}`"
          />
        </div>

        <!-- Блок с подписью и комментариями -->
        <div class="max-w-2xl mx-auto w-full">
          <!-- Подпись -->
          <div v-if="currentPhoto?.caption" class="text-center text-white/80 text-sm mb-3">
            {{ currentPhoto.caption }}
          </div>
          
          <!-- Комментарии -->
          <div class="bg-white/5 backdrop-blur-md rounded-2xl border border-white/10 overflow-hidden">
            <!-- Заголовок комментариев -->
            <div class="flex items-center justify-between px-4 py-2.5 border-b border-white/5 bg-white/5">
              <span class="text-white/60 text-xs font-medium flex items-center gap-1.5">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
                </svg>
                Комментарии ({{ currentPhoto?.comments?.length || 0 }})
              </span>
            </div>
            
            <!-- Список комментариев -->
            <div class="max-h-[140px] overflow-y-auto custom-scroll px-3 py-2 space-y-2">
              <div v-if="!currentPhoto?.comments || currentPhoto.comments.length === 0" class="text-center text-white/30 text-sm py-4">
                Нет комментариев. Будьте первым!
              </div>
              <div 
                v-for="comment in currentPhoto.comments" 
                :key="comment.id"
                class="group/comment flex items-start gap-2.5 text-sm p-2.5 rounded-xl hover:bg-white/5 transition-colors"
              >
                <img 
                  v-if="comment.user_avatar" 
                  :src="comment.user_avatar" 
                  :alt="comment.user_name"
                  class="w-8 h-8 rounded-full object-cover flex-shrink-0 border border-white/10"
                >
                <div 
                  v-else
                  class="w-8 h-8 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-[10px] font-bold flex-shrink-0"
                >
                  {{ getInitials(getAuthorFullName(comment)) }}
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center gap-2 flex-wrap">
                    <!-- ✅ Полное имя автора комментария -->
                    <span class="font-semibold text-white text-xs">{{ getAuthorFullName(comment) }}</span>
                    <span class="text-white/30 text-[10px]">{{ formatTime(comment.created_at) }}</span>
                    
                    <!-- Кнопки редактирования и удаления -->
                    <div class="flex items-center gap-0.5 ml-auto opacity-0 group-hover/comment:opacity-100 transition-opacity">
                      <button 
                        v-if="comment.can_edit"
                        @click="startEditComment(comment)"
                        class="text-white/40 hover:text-white/80 transition p-1 rounded hover:bg-white/10"
                        title="Редактировать"
                      >
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
                        </svg>
                      </button>
                      <button 
                        v-if="comment.can_delete"
                        @click="deleteComment(comment.id)"
                        class="text-white/40 hover:text-red-400 transition p-1 rounded hover:bg-white/10"
                        title="Удалить"
                      >
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                        </svg>
                      </button>
                    </div>
                  </div>
                  
                  <!-- Редактирование комментария -->
                  <div v-if="editingCommentId === comment.id" class="mt-1.5 flex gap-1.5">
                    <input 
                      v-model="editCommentContent"
                      type="text"
                      class="flex-1 bg-white/10 border border-white/10 rounded-lg px-2.5 py-1.5 text-white text-sm placeholder-white/40 focus:outline-none focus:ring-1 focus:ring-blue-500/50"
                      @keydown.enter="saveEditComment(comment.id)"
                      @keydown.escape="cancelEditComment"
                    />
                    <button 
                      @click="saveEditComment(comment.id)"
                      :disabled="savingEdit"
                      class="px-3 py-1.5 bg-blue-500/80 hover:bg-blue-600/80 text-white rounded-lg text-xs transition disabled:opacity-50"
                    >
                      {{ savingEdit ? '...' : 'Сохранить' }}
                    </button>
                    <button 
                      @click="cancelEditComment"
                      class="px-3 py-1.5 bg-white/10 hover:bg-white/20 text-white/60 rounded-lg text-xs transition"
                    >
                      Отмена
                    </button>
                  </div>
                  
                  <p v-else class="text-white/80 text-sm break-words leading-relaxed">{{ comment.content }}</p>
                </div>
              </div>
            </div>
            
            <!-- Форма добавления комментария -->
            <div v-if="authStore.isAuthenticated" class="border-t border-white/5 p-3 bg-white/5">
              <div class="flex gap-2">
                <input 
                  v-model="newComment"
                  type="text"
                  placeholder="Написать комментарий..."
                  class="flex-1 bg-white/10 border border-white/10 rounded-xl px-3 py-2 text-white text-sm placeholder-white/40 focus:outline-none focus:ring-2 focus:ring-blue-500/50 transition"
                  @keydown.enter="submitComment"
                />
                <button 
                  @click="submitComment"
                  :disabled="submitting || !newComment.trim()"
                  class="px-4 py-2 bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white rounded-xl transition-all duration-300 text-sm font-medium shadow-lg shadow-blue-500/25 disabled:opacity-50 disabled:cursor-not-allowed flex-shrink-0"
                >
                  {{ submitting ? '...' : 'Отправить' }}
                </button>
              </div>
            </div>
            <div v-else class="text-center text-white/40 text-sm py-3 border-t border-white/5">
              <NuxtLink to="/auth/login" class="text-blue-400 hover:text-blue-300 transition">Войдите</NuxtLink>, чтобы оставить комментарий
            </div>
          </div>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const authStore = useAuthStore()

const props = defineProps({
  photos: {
    type: Array,
    required: true,
    default: () => []
  },
  albumId: {
    type: [Number, String],
    default: null
  },
  initialIndex: {
    type: Number,
    default: 0
  },
  isOpen: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['close', 'photo-updated'])

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const currentIndex = ref(props.initialIndex || 0)
const isLoading = ref(true)
const isLiking = ref(false)
const newComment = ref('')
const submitting = ref(false)
const editingCommentId = ref(null)
const editCommentContent = ref('')
const savingEdit = ref(false)

// Текущее фото
const currentPhoto = computed(() => {
  return props.photos[currentIndex.value] || null
})

// ============================================
// ПОЛНОЕ ИМЯ АВТОРА КОММЕНТАРИЯ
// ============================================
const getAuthorFullName = (comment) => {
  if (!comment) return 'Пользователь'
  
  // Если есть first_name и last_name
  if (comment.user_first_name || comment.user_last_name) {
    const parts = []
    if (comment.user_last_name) parts.push(comment.user_last_name)
    if (comment.user_first_name) parts.push(comment.user_first_name)
    if (parts.length > 0) return parts.join(' ')
  }
  // Если есть full_name
  if (comment.user_full_name) {
    return comment.user_full_name
  }
  // Fallback - username
  return comment.user_name || 'Пользователь'
}

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

// ============================================
// ЗАКРЫТИЕ И НАВИГАЦИЯ
// ============================================
const closeLightbox = () => {
  emit('close')
  document.body.style.overflow = ''
}

const closeOnBackdrop = (event) => {
  if (event.target === event.currentTarget) {
    closeLightbox()
  }
}

const nextPhoto = () => {
  if (currentIndex.value < props.photos.length - 1) {
    currentIndex.value++
    isLoading.value = true
  }
}

const prevPhoto = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--
    isLoading.value = true
  }
}

const goToPhoto = (index) => {
  if (index !== currentIndex.value) {
    currentIndex.value = index
    isLoading.value = true
  }
}

// ============================================
// ЛАЙК
// ============================================
const toggleLike = async () => {
  if (!authStore.isAuthenticated || !currentPhoto.value) return
  
  isLiking.value = true
  
  try {
    const res = await fetch(`${API_URL}/albums/${props.albumId}/photos/${currentPhoto.value.id}/like/`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      const data = await res.json()
      
      const photoIndex = props.photos.findIndex(p => p.id === currentPhoto.value.id)
      if (photoIndex !== -1) {
        props.photos[photoIndex].likes_count = data.likes_count
        props.photos[photoIndex].user_has_liked = data.action === 'liked'
        emit('photo-updated', props.photos[photoIndex])
      }
      
      setTimeout(() => {
        isLiking.value = false
      }, 600)
    }
  } catch (e) {
    console.error('Ошибка:', e)
    isLiking.value = false
  }
}

// ============================================
// КОММЕНТАРИИ
// ============================================
const submitComment = async () => {
  if (!newComment.value.trim() || submitting.value || !currentPhoto.value) return
  
  submitting.value = true
  
  try {
    const res = await fetch(`${API_URL}/photo-comments/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify({
        photo: currentPhoto.value.id,
        content: newComment.value.trim()
      })
    })
    
    if (res.ok) {
      const comment = await res.json()
      
      if (!currentPhoto.value.comments) {
        currentPhoto.value.comments = []
      }
      currentPhoto.value.comments.push(comment)
      
      newComment.value = ''
    } else {
      const error = await res.json()
      console.error('Ошибка:', error)
      alert('Ошибка при отправке комментария')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    submitting.value = false
  }
}

const startEditComment = (comment) => {
  editingCommentId.value = comment.id
  editCommentContent.value = comment.content
}

const cancelEditComment = () => {
  editingCommentId.value = null
  editCommentContent.value = ''
}

const saveEditComment = async (commentId) => {
  if (!editCommentContent.value.trim() || savingEdit.value) return
  
  savingEdit.value = true
  
  try {
    const res = await fetch(`${API_URL}/photo-comments/${commentId}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify({
        content: editCommentContent.value.trim()
      })
    })
    
    if (res.ok) {
      const updatedComment = await res.json()
      
      const commentIndex = currentPhoto.value.comments.findIndex(c => c.id === commentId)
      if (commentIndex !== -1) {
        currentPhoto.value.comments[commentIndex] = updatedComment
      }
      
      cancelEditComment()
    } else {
      const error = await res.json()
      console.error('Ошибка:', error)
      alert('Ошибка при редактировании комментария')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    savingEdit.value = false
  }
}

const deleteComment = async (commentId) => {
  if (!confirm('Удалить этот комментарий?')) return
  
  try {
    const res = await fetch(`${API_URL}/photo-comments/${commentId}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      currentPhoto.value.comments = currentPhoto.value.comments.filter(c => c.id !== commentId)
    } else {
      const error = await res.json()
      console.error('Ошибка:', error)
      alert('Ошибка при удалении комментария')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  }
}

const formatTime = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleTimeString('ru-RU', {
    hour: '2-digit',
    minute: '2-digit'
  })
}

// ============================================
// КЛАВИАТУРНАЯ НАВИГАЦИЯ
// ============================================
const handleKeydown = (event) => {
  if (!props.isOpen) return
  
  switch (event.key) {
    case 'Escape':
      closeLightbox()
      break
    case 'ArrowRight':
      event.preventDefault()
      nextPhoto()
      break
    case 'ArrowLeft':
      event.preventDefault()
      prevPhoto()
      break
  }
}

// ============================================
// ЖИЗНЕННЫЙ ЦИКЛ
// ============================================
watch(() => props.isOpen, (newVal) => {
  if (newVal) {
    currentIndex.value = props.initialIndex || 0
    isLoading.value = true
    document.body.style.overflow = 'hidden'
    document.addEventListener('keydown', handleKeydown)
  } else {
    document.removeEventListener('keydown', handleKeydown)
    document.body.style.overflow = ''
  }
}, { immediate: true })

watch(currentIndex, () => {
  if (currentPhoto.value?.id && props.albumId) {
    incrementViews(currentPhoto.value.id)
  }
})

const incrementViews = async (photoId) => {
  try {
    await fetch(`${API_URL}/albums/${props.albumId}/photos/${photoId}/view/`, {
      method: 'POST'
    })
  } catch (e) {
    console.error('Ошибка увеличения просмотров:', e)
  }
}

onUnmounted(() => {
  document.removeEventListener('keydown', handleKeydown)
  document.body.style.overflow = ''
})
</script>

<style scoped>
/* Анимация лайка */
@keyframes likeAnimation {
  0% { transform: scale(1); }
  25% { transform: scale(1.3); }
  50% { transform: scale(0.9); }
  75% { transform: scale(1.15); }
  100% { transform: scale(1); }
}

.animate-like {
  animation: likeAnimation 0.6s ease forwards;
}

/* Кастомный скролл */
.custom-scroll::-webkit-scrollbar {
  width: 4px;
}

.custom-scroll::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 4px;
}

.custom-scroll::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 4px;
}

.custom-scroll::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.3);
}

img {
  transition: opacity 0.3s ease;
}

.fixed {
  overscroll-behavior: none;
}

.sticky {
  position: sticky;
  top: 0;
  z-index: 5;
}
</style>