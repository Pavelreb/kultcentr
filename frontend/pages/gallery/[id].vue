<!-- frontend/pages/gallery/[id].vue -->
<template>
  <div class="container mx-auto p-4">
    <!-- Хлебные крошки -->
    <Breadcrumbs 
      :items="breadcrumbItems" 
      :current-page-name="album?.title || 'Загрузка...'"
      class="mb-6"
    />
    
    <!-- Детальная страница альбома -->
    <AlbumDetail 
      :album="album" 
      :loading="loading"
      @delete="handleDelete"
    />
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import Breadcrumbs from '~/components/common/Breadcrumbs.vue'
import AlbumDetail from '~/components/features/albums/AlbumDetail.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const { apiFetch } = useApi()

const album = ref(null)
const loading = ref(true)

// Хлебные крошки
const breadcrumbItems = [
  { label: 'Фотоальбомы', to: '/gallery' }
]

const handleDelete = async (albumId) => {
  try {
    const res = await apiFetch(`${API_URL}/albums/${albumId}/`, {
      method: 'DELETE',
    })
    
    if (res.ok) {
      router.push('/gallery')
    } else {
      alert('Ошибка при удалении альбома')
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
    const res = await apiFetch(`${API_URL}/albums/${id}/`)
    
    if (res.ok) {
      album.value = await res.json()
    } else {
      router.push('/gallery')
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>