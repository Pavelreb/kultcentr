<!-- frontend/components/features/posts/PostDetail.vue -->
<template>
  <div v-if="post" class="max-w-4xl mx-auto">
    <!-- Основной блок -->
    <div class="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden shadow-xl border border-gray-100 dark:border-gray-700">
      <!-- Изображение 16:9 с кнопкой лайка -->
      <div class="relative aspect-video overflow-hidden bg-gradient-to-r from-gray-200 to-gray-300 dark:from-gray-700 dark:to-gray-600 group/image">
        <img 
          v-if="post.display_image" 
          :src="post.display_image" 
          :alt="post.title"
          class="w-full h-full object-cover transition-transform duration-700 group-hover/image:scale-105"
        />
        <div v-else class="w-full h-full flex items-center justify-center">
          <svg class="w-24 h-24 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9"/>
          </svg>
        </div>
        
        <!-- Кнопка лайка по центру (появляется при наведении) -->
        <button 
          v-if="authStore.isAuthenticated"
          @click="toggleLike"
          class="absolute inset-0 flex items-center justify-center opacity-0 group-hover/image:opacity-100 transition-all duration-300"
        >
          <div 
            class="p-5 rounded-full bg-white/10 backdrop-blur-sm hover:bg-white/20 transition-all duration-300 scale-90 group-hover/image:scale-100"
            :class="{ 'animate-like': isLiking }"
          >
            <svg 
              class="w-14 h-14 transition-all duration-300 drop-shadow-lg"
              :class="post.user_has_liked ? 'text-red-500 fill-red-500' : 'text-white fill-none hover:text-red-400'"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
          </div>
        </button>
        
        <!-- Бейдж "Черновик" -->
        <div v-if="!post.is_published" class="absolute top-3 left-3 px-3 py-1 rounded-full text-xs font-semibold bg-yellow-500 text-black shadow-lg backdrop-blur-md">
          Черновик
        </div>
        
        <!-- Бейдж "Новое" -->
        <div v-if="isNew" class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-semibold bg-blue-500 text-white shadow-lg backdrop-blur-md">
          Новое
        </div>
        
        <!-- Счётчик лайков на изображении -->
        <div class="absolute bottom-3 right-3 px-3 py-1.5 rounded-full bg-black/50 backdrop-blur-md text-white text-sm flex items-center gap-1.5">
          <svg class="w-4 h-4" :class="post.user_has_liked ? 'text-red-500 fill-red-500' : 'text-white'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
          </svg>
          <span>{{ post.likes_count || 0 }}</span>
        </div>
      </div>
      
      <!-- Контент -->
      <div class="p-6 md:p-8 lg:p-10">
        <!-- Заголовок -->
        <h1 class="text-2xl md:text-3xl lg:text-4xl font-bold text-gray-900 dark:text-white mb-4 leading-tight">
          {{ post.title }}
        </h1>
        
        <!-- Автор и дата -->
        <div class="flex flex-wrap items-center gap-3 text-sm text-gray-500 dark:text-gray-400 mb-6 pb-6 border-b border-gray-100 dark:border-gray-700">
          <div class="flex items-center gap-2">
            <img 
              v-if="post.author_avatar" 
              :src="post.author_avatar" 
              :alt="post.author_name"
              class="w-8 h-8 rounded-full object-cover border border-gray-200 dark:border-gray-600"
            >
            <div 
              v-else
              class="w-8 h-8 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-xs font-bold flex-shrink-0"
            >
              {{ getInitials(getAuthorFullName()) }}
            </div>
            <div class="flex flex-col">
              <span class="font-medium text-gray-700 dark:text-gray-300">
                {{ getAuthorFullName() }}
              </span>
              <span class="text-xs text-gray-400 dark:text-gray-500">
                {{ post.author_role === 'editor' ? 'Главный редактор' : 'Автор' }}
              </span>
            </div>
          </div>
          
          <span class="text-gray-300 dark:text-gray-600">•</span>
          
          <div class="flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            <span>{{ formatDate(post.created_at) }}</span>
          </div>
          
          <span class="text-gray-300 dark:text-gray-600">•</span>
          
          <div class="flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
            </svg>
            <span>{{ post.views || 0 }} просмотров</span>
          </div>
        </div>
        
        <!-- Контент поста -->
        <div class="prose prose-lg dark:prose-invert max-w-none">
          <div class="text-gray-700 dark:text-gray-300 leading-relaxed whitespace-pre-wrap">
            {{ post.content }}
          </div>
        </div>
        
        <!-- Статистика -->
        <div class="mt-6 pt-6 border-t border-gray-100 dark:border-gray-700 flex flex-wrap gap-4 text-sm text-gray-500 dark:text-gray-400">
          <span class="flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
            </svg>
            {{ post.comments?.length || 0 }} комментариев
          </span>
          <span class="flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            {{ post.likes_count || 0 }} лайков
          </span>
        </div>
        
        <!-- Кнопки действий -->
        <div v-if="canEdit" class="mt-6 pt-6 border-t border-gray-100 dark:border-gray-700 flex flex-wrap gap-3">
          <button 
            @click="editPost"
            class="inline-flex items-center gap-2 px-4 py-2.5 text-sm font-medium text-gray-600 dark:text-gray-400 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 hover:text-gray-900 dark:hover:text-white transition-all duration-300"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
            </svg>
            Редактировать
          </button>
        </div>
      </div>
    </div>
    
    <!-- ========================================== -->
    <!-- КОММЕНТАРИИ                                 -->
    <!-- ========================================== -->
    <PostComments 
      :post-id="post.id"
      :comments="post.comments || []"
      @comment-added="onCommentAdded"
      @comment-deleted="onCommentDeleted"
      @comment-updated="onCommentUpdated"
    />
    
    <!-- Навигация: Назад к списку -->
    <div class="mt-6">
      <NuxtLink to="/posts" class="inline-flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 transition">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
        </svg>
        Назад к публикациям
      </NuxtLink>
    </div>
  </div>
  
  <!-- Состояние загрузки -->
  <div v-else-if="loading" class="text-center py-20">
    <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
    </svg>
    <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
  </div>
  
  <!-- Пост не найден -->
  <div v-else class="text-center py-20">
    <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9"/>
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
    </svg>
    <p class="text-gray-500 dark:text-gray-400">Пост не найден</p>
    <NuxtLink to="/posts" class="mt-4 inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
      </svg>
      Вернуться к публикациям
    </NuxtLink>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import PostComments from '~/components/features/posts/PostComments.vue'

const authStore = useAuthStore()

const props = defineProps({
  post: {
    type: Object,
    default: null
  },
  loading: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['delete', 'like-updated'])

const router = useRouter()
const config = useRuntimeConfig()

const isLiking = ref(false)

// ============================================
// ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
// ============================================
const getAuthorFullName = () => {
  if (!props.post) return 'Автор'
  
  if (props.post.author_first_name || props.post.author_last_name) {
    const parts = []
    if (props.post.author_last_name) parts.push(props.post.author_last_name)
    if (props.post.author_first_name) parts.push(props.post.author_first_name)
    if (parts.length > 0) return parts.join(' ')
  }
  if (props.post.author_full_name) {
    return props.post.author_full_name
  }
  return props.post.author_name || 'Автор'
}

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

const isNew = computed(() => {
  if (!props.post?.created_at) return false
  const postDate = new Date(props.post.created_at)
  const today = new Date()
  return postDate.toDateString() === today.toDateString()
})

// ============================================
// ЛАЙК С АНИМАЦИЕЙ
// ============================================
const toggleLike = async () => {
  if (!authStore.isAuthenticated) {
    router.push('/auth/login')
    return
  }
  
  isLiking.value = true
  
  try {
    const res = await fetch(`${config.public.apiBase}/likes/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify({
        post: props.post.id
      })
    })
    
    if (res.ok) {
      const data = await res.json()
      
      if (data.action === 'liked') {
        props.post.likes_count = (props.post.likes_count || 0) + 1
        props.post.user_has_liked = true
      } else if (data.action === 'unliked') {
        props.post.likes_count = (props.post.likes_count || 0) - 1
        props.post.user_has_liked = false
      }
      
      emit('like-updated', {
        likesCount: props.post.likes_count,
        isLiked: props.post.user_has_liked
      })
      
      // Анимация лайка
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
// РЕДАКТИРОВАНИЕ
// ============================================
const canEdit = computed(() => {
  if (!props.post) return false
  const user = authStore.user
  if (!user) return false
  return user.role === 'editor' || user.username === props.post.author_name
})

const editPost = () => {
  router.push(`/posts/edit-${props.post.id}`)
}

// ============================================
// СОБЫТИЯ ОТ КОМПОНЕНТА КОММЕНТАРИЕВ
// ============================================
const onCommentAdded = (comment) => {
  console.log('Комментарий добавлен:', comment)
}

const onCommentDeleted = (commentId) => {
  console.log('Комментарий удалён:', commentId)
}

const onCommentUpdated = (comment) => {
  console.log('Комментарий обновлён:', comment)
}
</script>

<style scoped>
/* ========================================== */
/* АНИМАЦИЯ ЛАЙКА                            */
/* ========================================== */

@keyframes likeAnimation {
  0% {
    transform: scale(1);
  }
  25% {
    transform: scale(1.3);
  }
  50% {
    transform: scale(0.9);
  }
  75% {
    transform: scale(1.15);
  }
  100% {
    transform: scale(1);
  }
}

.animate-like {
  animation: likeAnimation 0.6s ease forwards;
}

/* Анимация сердечка при лайке */
@keyframes heartPop {
  0% {
    transform: scale(1);
  }
  30% {
    transform: scale(1.4);
    opacity: 1;
  }
  60% {
    transform: scale(0.9);
  }
  100% {
    transform: scale(1);
  }
}

.heart-pop {
  animation: heartPop 0.5s ease forwards;
}
</style>