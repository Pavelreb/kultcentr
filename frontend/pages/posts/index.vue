<!-- frontend/pages/posts/index.vue -->
<template>
  <div class="container mx-auto p-4">
    <!-- Хлебные крошки -->
    <Breadcrumbs 
      :items="breadcrumbItems" 
      class="mb-6"
    />
    
    <!-- ========================================== -->
    <!-- ГЛАВНАЯ ПУБЛИКАЦИЯ (только на 1-й странице) -->
    <!-- ========================================== -->
    <FeaturedPost v-if="isFirstPage" :post="featuredPost" />
    
    <!-- ========================================== -->
    <!-- СПИСОК ВСЕХ ПУБЛИКАЦИЙ (с пагинацией)    -->
    <!-- ========================================== -->
    <PostList 
      :posts="remainingPosts" 
      :loading="loading"
      :items-per-page="9"
    />
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import Breadcrumbs from '~/components/common/Breadcrumbs.vue'

useSeoMeta({
  title: 'Публикации',
  description: 'Новости, статьи и публикации центра культуры.'
})
import FeaturedPost from '~/components/features/posts/FeaturedPost.vue'
import PostList from '~/components/features/posts/PostList.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()
const route = useRoute()
const posts = ref([])
const loading = ref(true)

// Главную новость показываем только на первой странице пагинации
const isFirstPage = computed(() => (Number(route.query.page) || 1) === 1)

// Хлебные крошки — на странице публикаций последняя крошка "Публикации"
const breadcrumbItems = [
  { label: 'Публикации' }
]

// Главная публикация: выбранная редактором, иначе — самая свежая опубликованная
const featuredPost = computed(() => {
  if (posts.value.length === 0) return null

  const manual = posts.value.find(p => p.is_featured && p.is_published)
  if (manual) return manual

  const sorted = [...posts.value]
    .filter(p => p.is_published)
    .sort((a, b) => new Date(b.created_at) - new Date(a.created_at))

  return sorted.length > 0 ? sorted[0] : posts.value[0]
})

// Список постов без главного
const remainingPosts = computed(() => {
  if (!featuredPost.value) return posts.value
  return posts.value.filter(p => p.id !== featuredPost.value.id)
})

onMounted(() => {
  authStore.restoreAuth()
})

onMounted(async () => {
  try {
    const res = await apiFetch(`${API_URL}/posts/`)
    posts.value = await res.json()
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>