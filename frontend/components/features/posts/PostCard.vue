<!-- frontend/components/features/posts/PostCard.vue -->
<template>
  <NuxtLink 
    :to="`/posts/${post.id}`" 
    class="group bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden flex flex-col h-full hover:-translate-y-1"
  >
    <!-- Изображение - соотношение 16:9 -->
    <div class="relative aspect-video overflow-hidden flex-shrink-0 bg-gradient-to-r from-gray-200 to-gray-300 dark:from-gray-600 dark:to-gray-700">
      <img 
        v-if="post.display_image" 
        :src="post.display_image" 
        :alt="post.title"
        class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
        loading="lazy"
      />
      <div 
        v-else 
        class="w-full h-full flex items-center justify-center"
      >
        <span class="text-4xl text-gray-400 dark:text-gray-500">📝</span>
      </div>
      
      <!-- Бейдж "Новое" если создано сегодня -->
      <div 
        v-if="isNew" 
        class="absolute top-3 left-3 px-2.5 py-1 rounded-full text-xs font-medium bg-blue-500 text-white shadow-lg"
      >
        <span class="flex items-center gap-1">
          <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          Новое
        </span>
      </div>
      
      <!-- Бейдж "Черновик" -->
      <div 
        v-if="!post.is_published && showDraftBadge" 
        class="absolute top-3 right-3 px-2.5 py-1 rounded-full text-xs font-medium bg-yellow-500 text-white shadow-lg"
      >
        <span class="flex items-center gap-1">
          <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
          </svg>
          Черновик
        </span>
      </div>
    </div>
    
    <!-- Контент -->
    <div class="p-4 flex flex-col flex-1">
      <div class="flex-1">
        <h3 class="text-base font-semibold text-gray-800 dark:text-gray-200 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors line-clamp-2">
          {{ post.title }}
        </h3>
        
        <p class="text-gray-500 dark:text-gray-400 text-sm mt-1.5 line-clamp-3">
          {{ post.excerpt || post.content?.substring(0, 100) }}...
        </p>
      </div>
      
      <!-- Нижняя часть -->
      <div class="mt-3 pt-3 border-t border-gray-100 dark:border-gray-700">
        <!-- Автор -->
        <div class="flex items-center justify-between text-xs text-gray-500 dark:text-gray-400">
          <div class="flex items-center gap-1.5">
            <img 
              v-if="post.author_avatar" 
              :src="post.author_avatar" 
              :alt="post.author_name"
              class="w-5 h-5 rounded-full object-cover"
            >
            <div 
              v-else
              class="w-5 h-5 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-[8px] font-bold"
            >
              {{ getInitials(post.author_name) }}
            </div>
            <span class="font-medium text-gray-700 dark:text-gray-300">
              {{ getAuthorFullName(post) }}
            </span>
          </div>
          <span>{{ formatDate(post.created_at) }}</span>
        </div>
        
        <!-- Статистика -->
        <div class="flex items-center gap-3 mt-2 text-xs text-gray-400 dark:text-gray-500">
          <span class="flex items-center gap-1">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
            </svg>
            {{ post.views || 0 }}
          </span>
          <span class="flex items-center gap-1">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
            </svg>
            {{ post.comments?.length || 0 }}
          </span>
          <span class="flex items-center gap-1">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            {{ post.likes_count || 0 }}
          </span>
        </div>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
const props = defineProps({
  post: {
    type: Object,
    required: true
  },
  showDraftBadge: {
    type: Boolean,
    default: true
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

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const getAuthorFullName = (post) => {
  if (post.author_first_name || post.author_last_name) {
    const parts = []
    if (post.author_last_name) parts.push(post.author_last_name)
    if (post.author_first_name) parts.push(post.author_first_name)
    if (parts.length > 0) return parts.join(' ')
  }
  if (post.author_full_name) {
    return post.author_full_name
  }
  return post.author_name || post.author?.username || 'Автор'
}

// Проверяем, создан ли пост сегодня
const isNew = computed(() => {
  if (!props.post.created_at) return false
  const postDate = new Date(props.post.created_at)
  const today = new Date()
  return postDate.toDateString() === today.toDateString()
})
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>