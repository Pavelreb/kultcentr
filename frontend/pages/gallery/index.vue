<!-- frontend/pages/gallery/index.vue -->
<template>
  <div class="container mx-auto p-4">
    <!-- Хлебные крошки -->
    <Breadcrumbs 
      :items="breadcrumbItems" 
      class="mb-6"
    />
    
    <!-- Сетка альбомов с пагинацией -->
    <AlbumGrid 
      :albums="albums" 
      :loading="loading"
      :items-per-page="15"
    />
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import Breadcrumbs from '~/components/common/Breadcrumbs.vue'
import AlbumGrid from '~/components/features/albums/AlbumGrid.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const albums = ref([])
const loading = ref(true)

// Хлебные крошки
const breadcrumbItems = [
  { label: 'Фотоальбомы' }
]

onMounted(() => {
  authStore.restoreAuth()
})

onMounted(async () => {
  try {
    const headers = {}
    if (authStore.isAuthenticated) {
      headers['Authorization'] = `Bearer ${authStore.accessToken}`
    }
    const res = await fetch(`${API_URL}/albums/`, { headers })
    if (res.ok) {
      albums.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка загрузки альбомов:', e)
  } finally {
    loading.value = false
  }
})
</script>