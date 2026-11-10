<!-- frontend/pages/posts/[id].vue -->
<template>
  <div class="container mx-auto p-4">
    <!-- Хлебные крошки (вне контейнера с постом) -->
    <Breadcrumbs 
      :items="breadcrumbItems" 
      :current-page-name="post?.title || 'Загрузка...'"
      class="mb-6"
    />
    
    <!-- Детальная страница поста -->
    <PostDetail 
      :post="post" 
      :loading="loading"
      @delete="handleDelete"
    />
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import Breadcrumbs from '~/components/common/Breadcrumbs.vue'
import PostDetail from '~/components/features/posts/PostDetail.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const { apiFetch } = useApi()

const post = ref(null)
const loading = ref(true)

// Хлебные крошки
const breadcrumbItems = [
  { label: 'Публикации', to: '/posts' }
]

const handleDelete = async (postId) => {
  try {
    const res = await apiFetch(`${API_URL}/posts/${postId}/`, {
      method: 'DELETE',
    })
    
    if (res.ok) {
      router.push('/posts')
    } else {
      alert('Ошибка при удалении поста')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  }
}

onMounted(() => {
  authStore.restoreAuth()
})

onMounted(async () => {
  try {
    const id = route.params.id
    const res = await apiFetch(`${API_URL}/posts/${id}/`)
    
    if (res.ok) {
      post.value = await res.json()
    } else {
      router.push('/posts')
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>