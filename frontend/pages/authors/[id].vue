<template>
  <div class="container mx-auto p-4 max-w-4xl">
    <NuxtLink to="/" class="text-blue-500 dark:text-blue-400 hover:underline mb-4 inline-block">
      ← На главную
    </NuxtLink>

    <div v-if="author" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg mb-8 transition-colors duration-200">
      <div class="flex items-center gap-6">
        <!-- Аватарка -->
        <div class="w-24 h-24 rounded-full bg-blue-500 flex items-center justify-center text-white text-3xl font-bold overflow-hidden flex-shrink-0">
          <img v-if="author.avatar_url" :src="author.avatar_url" :alt="author.username" class="w-full h-full object-cover">
          <span v-else>{{ getInitials(author) }}</span>
        </div>
        <div>
          <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200">{{ getFullName(author) }}</h1>
          <p class="text-gray-500 dark:text-gray-400">{{ author.role_display }}</p>
          <p v-if="author.bio" class="text-gray-600 dark:text-gray-300 mt-2">{{ author.bio }}</p>
        </div>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-4">📝 Публикации автора</h2>

    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>

    <div v-else-if="posts.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-lg shadow">
      <p class="text-gray-500 dark:text-gray-400">У автора пока нет публикаций</p>
    </div>

    <div v-else class="space-y-4">
      <div 
        v-for="post in posts" 
        :key="post.id" 
        class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow hover:shadow-md transition flex gap-4"
      >
        <div v-if="post.image_url" class="h-24 w-24 rounded-lg overflow-hidden flex-shrink-0">
          <img :src="post.image_url" :alt="post.title" class="w-full h-full object-cover">
        </div>
        <div v-else class="h-24 w-24 bg-gradient-to-r from-gray-200 to-gray-300 dark:from-gray-600 dark:to-gray-500 rounded-lg flex items-center justify-center flex-shrink-0">
          <span class="text-gray-400 dark:text-gray-500 text-2xl">📝</span>
        </div>
        
        <NuxtLink :to="`/posts/${post.id}`" class="block flex-1">
          <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition">{{ post.title }}</h3>
          <p class="text-gray-600 dark:text-gray-400 text-sm">{{ formatDate(post.created_at) }}</p>
          <p class="text-gray-700 dark:text-gray-300 mt-1 line-clamp-2">{{ post.excerpt || post.content?.substring(0, 150) }}...</p>
          <div class="flex items-center gap-4 mt-2 text-sm text-gray-400 dark:text-gray-500">
            <span>💬 {{ post.comments?.length || 0 }}</span>
            <span>❤️ {{ post.likes_count || 0 }}</span>
          </div>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()
const route = useRoute()
const author = ref(null)
const posts = ref([])
const loading = ref(true)

const getInitials = (user) => {
  const name = user.full_name || user.username
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const getFullName = (user) => {
  return user.full_name || user.username
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

onMounted(async () => {
  try {
    const authorId = route.params.id
    
    const authorRes = await apiFetch(`${API_URL}/auth/users/${authorId}/`)
    if (authorRes.ok) {
      author.value = await authorRes.json()
    }
    
    if (author.value?.username) {
      const url = `${API_URL}/posts/?author_name=${author.value.username}`
      const postsRes = await apiFetch(url)
      if (postsRes.ok) {
        posts.value = await postsRes.json()
      }
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>