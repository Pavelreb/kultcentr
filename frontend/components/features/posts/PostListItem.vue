<!-- frontend/components/features/posts/PostListItem.vue -->
<template>
  <NuxtLink 
    :to="`/posts/${post.id}`" 
    class="bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden flex flex-col group hover:-translate-y-1"
  >
    <!-- Изображение-постер 16:9 -->
    <div class="p-3 bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-800 dark:to-gray-900 flex-shrink-0">
      <div class="relative aspect-video overflow-hidden rounded-lg shadow-md ring-1 ring-black/5 dark:ring-white/5 bg-gradient-to-r from-gray-200 to-gray-300 dark:from-gray-700 dark:to-gray-600">
        <img 
          v-if="post.display_image" 
          :src="post.display_image" 
          :alt="post.title" 
          class="w-full h-full object-cover group-hover:scale-105 transition duration-500"
          loading="lazy"
        />
        <div v-else class="w-full h-full flex items-center justify-center">
          <svg class="w-16 h-16 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9"/>
          </svg>
        </div>
        
        <!-- Бейдж "Черновик" -->
        <div 
          v-if="!post.is_published && showDraftBadge"
          class="absolute top-3 right-3 px-2.5 py-1 rounded-full text-xs font-semibold bg-yellow-400 text-black shadow-lg backdrop-blur-md"
        >
          Черновик
        </div>
      </div>
    </div>
    
    <!-- Контент -->
    <div class="p-5 flex flex-col flex-1">
      <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition line-clamp-2">
        {{ post.title }}
      </h2>
      
      <!-- Автор с аватаркой -->
      <div
        class="flex items-center gap-2 mt-2 text-sm text-gray-500 dark:text-gray-400 cursor-pointer hover:text-blue-600 dark:hover:text-blue-400 transition-colors self-start"
        @click.prevent.stop="goToAuthor"
      >
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
      </div>
      
      <p class="text-gray-600 dark:text-gray-400 text-sm mt-2 line-clamp-3">
        <RichText :text="post.excerpt || post.content || ''" compact />
      </p>
      
      <div class="flex justify-between items-center mt-4 pt-4 border-t border-gray-100 dark:border-gray-700">
        <div class="flex items-center gap-3 text-sm text-gray-400 dark:text-gray-500">
          <span class="flex items-center gap-1">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
            </svg>
            {{ post.views || 0 }}
          </span>
          <span class="flex items-center gap-1">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
            </svg>
            {{ post.comments?.length || 0 }}
          </span>
          <span class="flex items-center gap-1">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            {{ post.likes_count || 0 }}
          </span>
        </div>
        <span class="text-xs text-gray-400 dark:text-gray-500 flex items-center gap-1">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
          {{ formatDate(post.created_at) }}
        </span>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
import RichText from '~/components/common/RichText.vue'

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

const getAuthorFullName = () => {
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

// Переход на страницу автора (карточка целиком — ссылка, поэтому стопорим всплытие)
const goToAuthor = () => {
  if (props.post.author_id) {
    navigateTo(`/users/${props.post.author_id}`)
  }
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
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'short',
    year: 'numeric'
  })
}
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