<!-- frontend/components/features/posts/FeaturedPost.vue -->
<template>
  <div v-if="post" class="mb-10">
    <div class="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden shadow-xl border border-gray-100 dark:border-gray-700">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-0">
        <!-- Левая колонка: Изображение-постер 16:9 -->
        <div class="relative flex items-center justify-center p-4 md:p-6 bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-800 dark:to-gray-900">
          <div class="relative aspect-video w-full rounded-2xl overflow-hidden shadow-2xl ring-1 ring-black/5 dark:ring-white/5">
            <img 
              v-if="post.display_image" 
              :src="post.display_image" 
              :alt="post.title"
              class="w-full h-full object-cover"
            />
            <div v-else class="w-full h-full flex items-center justify-center bg-gradient-to-br from-blue-600 to-purple-700">
              <svg class="w-24 h-24 text-white/30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9"/>
              </svg>
            </div>
            
            <!-- Бейджи поверх изображения -->
            <div class="absolute top-3 left-3 right-3 flex flex-wrap gap-2 z-10">
              <div class="px-3 py-1 rounded-full text-xs font-semibold bg-gradient-to-r from-amber-400 to-yellow-500 text-black shadow-lg backdrop-blur-md">
                <span class="flex items-center gap-1.5">
                  <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/>
                  </svg>
                  ГЛАВНАЯ ПУБЛИКАЦИЯ
                </span>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Правая колонка: Информация -->
        <div class="p-6 md:p-8 lg:p-10 flex flex-col justify-center">
          <!-- Заголовок -->
          <h2 class="text-2xl md:text-3xl lg:text-4xl font-bold text-gray-900 dark:text-white mb-3 leading-tight">
            {{ post.title }}
          </h2>
          
          <!-- Автор с полным именем -->
          <div class="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-3">
            <img 
              v-if="post.author_avatar" 
              :src="post.author_avatar" 
              :alt="post.author_name"
              class="w-6 h-6 rounded-full object-cover border border-gray-200 dark:border-gray-600"
            >
            <div 
              v-else
              class="w-6 h-6 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-[10px] font-bold flex-shrink-0"
            >
              {{ getInitials(getAuthorFullName()) }}
            </div>
            <span>{{ getAuthorFullName() }}</span>
            <span class="text-gray-300 dark:text-gray-600">•</span>
            <span class="flex items-center gap-1">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
              {{ formatDate(post.created_at) }}
            </span>
          </div>
          
          <!-- Описание -->
          <p class="text-gray-600 dark:text-gray-300 text-sm md:text-base leading-relaxed mb-4 line-clamp-3">
            {{ post.excerpt || post.content?.substring(0, 200) }}...
          </p>
          
          <!-- Статистика -->
          <div class="flex flex-wrap gap-4 mb-6 text-sm text-gray-500 dark:text-gray-400">
            <span class="flex items-center gap-1.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
              </svg>
              {{ post.views || 0 }} просмотров
            </span>
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
          
          <!-- Кнопки -->
          <div class="flex flex-wrap gap-3">
            <NuxtLink 
              :to="`/posts/${post.id}`" 
              class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5"
            >
              Читать публикацию
              <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
              </svg>
            </NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  post: {
    type: Object,
    default: null
  }
})

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

// Функция для получения полного имени автора
const getAuthorFullName = () => {
  if (!props.post) return 'Автор'
  
  // Если есть поля first_name и last_name
  if (props.post.author_first_name || props.post.author_last_name) {
    const parts = []
    if (props.post.author_last_name) parts.push(props.post.author_last_name)
    if (props.post.author_first_name) parts.push(props.post.author_first_name)
    if (parts.length > 0) return parts.join(' ')
  }
  // Если есть full_name
  if (props.post.author_full_name) {
    return props.post.author_full_name
  }
  // Fallback - используем username
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
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>