<!-- frontend/pages/index.vue -->
<template>
  <div>
    <!-- HERO БАННЕР -->
    <div v-if="bannerLoading" class="w-full h-64 bg-gray-200 dark:bg-gray-700 animate-pulse"></div>
    <HeroBanner 
      v-else-if="bannerData.is_active !== false"
      :banner="bannerData" 
    />

    <div class="container mx-auto px-4 py-6 md:py-8">
      <div class="space-y-12 md:space-y-16">
        
        <!-- ========================================== -->
        <!-- 1. БЛОК АФИШИ                             -->
        <!-- ========================================== -->
        <EventSection 
          :events="events" 
          :loading="eventsLoading"
          :items-per-page="5"
        />

        <!-- ========================================== -->
        <!-- 2. БЛОК ПУБЛИКАЦИЙ                        -->
        <!-- ========================================== -->
        <PostSection 
          :posts="posts" 
          :loading="postsLoading"
          :items-per-page="4"
        />

        <!-- ========================================== -->
        <!-- 3. БЛОК АВТОРОВ                           -->
        <!-- ========================================== -->
        <AuthorSection 
          :authors="authors" 
          :loading="authorsLoading"
          :items-per-page="6"
        />

        <!-- ========================================== -->
        <!-- 4. БЛОК ФОТОАЛЬБОМОВ                      -->
        <!-- ========================================== -->
        <AlbumSection 
          :albums="albums" 
          :loading="albumsLoading"
          :items-per-page="5"
        />
        
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import HeroBanner from '~/components/features/banner/HeroBanner.vue'

useSeoMeta({
  title: 'Главная',
  description: 'Афиша мероприятий, публикации, фотоальбомы и авторы центра культуры.',
  ogTitle: 'Центр Культуры',
  ogDescription: 'Афиша мероприятий, публикации, фотоальбомы и авторы центра культуры.'
})
import EventSection from '~/components/features/events/EventSection.vue'
import PostSection from '~/components/features/posts/PostSection.vue'
import AuthorSection from '~/components/features/authors/AuthorSection.vue'
import AlbumSection from '~/components/features/albums/AlbumSection.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()

// ============================================
// 1. БАННЕР
// ============================================
const bannerData = ref({
  title: '🏛️ Добро пожаловать в Центр Культуры',
  subtitle: 'Место, где искусство, традиции и творчество объединяются',
  has_background: false,
  background_image_url_display: '',
  button_text: '',
  button_link: '',
  button_enabled: true,
  is_active: true
})
const bannerLoading = ref(true)

// ============================================
// 2. СОБЫТИЯ
// ============================================
const events = ref([])
const eventsLoading = ref(true)

// ============================================
// 3. ПУБЛИКАЦИИ
// ============================================
const posts = ref([])
const postsLoading = ref(true)

// ============================================
// 4. АВТОРЫ
// ============================================
const authors = ref([])
const authorsLoading = ref(true)

// ============================================
// 5. АЛЬБОМЫ
// ============================================
const albums = ref([])
const albumsLoading = ref(true)

// ============================================
// ЗАГРУЗКА ДАННЫХ
// ============================================

const loadBanner = async () => {
  try {
    const res = await fetch(`${API_URL}/banner/`)
    if (res.ok) {
      const data = await res.json()
      bannerData.value = {
        title: data.title || '🏛️ Добро пожаловать в Центр Культуры',
        subtitle: data.subtitle || 'Место, где искусство, традиции и творчество объединяются',
        has_background: data.has_background || false,
        background_image_url_display: data.background_image_url_display || '',
        button_text: data.button_text || '',
        button_link: data.button_link || '',
        button_enabled: data.button_enabled !== undefined ? data.button_enabled : true,
        is_active: data.is_active !== undefined ? data.is_active : true
      }
    }
  } catch (e) {
    console.error('Ошибка загрузки баннера:', e)
  } finally {
    bannerLoading.value = false
  }
}

const loadEvents = async () => {
  try {
    const res = await apiFetch('/events/')
    if (res.ok) {
      events.value = await res.json()
    } else {
      console.warn('Не удалось загрузить события:', res.status)
      events.value = []
    }
  } catch (e) {
    console.error('Ошибка загрузки событий:', e)
    events.value = []
  } finally {
    eventsLoading.value = false
  }
}

const loadPosts = async () => {
  try {
    const res = await apiFetch('/posts/')
    if (res.ok) {
      posts.value = await res.json()
    } else {
      console.warn('Не удалось загрузить посты:', res.status)
      posts.value = []
    }
  } catch (e) {
    console.error('Ошибка загрузки постов:', e)
    posts.value = []
  } finally {
    postsLoading.value = false
  }
}

const loadAuthors = async () => {
  try {
    const res = await fetch(`${API_URL}/auth/users/`)
    if (res.ok) {
      const allUsers = await res.json()
      authors.value = allUsers.filter(user => user.role === 'author' || user.role === 'editor')
    } else {
      authors.value = []
    }
  } catch (e) {
    console.error('Ошибка загрузки авторов:', e)
    authors.value = []
  } finally {
    authorsLoading.value = false
  }
}

const loadAlbums = async () => {
  try {
    const res = await apiFetch('/albums/')
    if (res.ok) {
      albums.value = await res.json()
    } else {
      console.warn('Не удалось загрузить альбомы:', res.status)
      albums.value = []
    }
  } catch (e) {
    console.error('Ошибка загрузки альбомов:', e)
    albums.value = []
  } finally {
    albumsLoading.value = false
  }
}

// ============================================
// ЖИЗНЕННЫЙ ЦИКЛ
// ============================================

onMounted(async () => {
  // Восстанавливаем авторизацию
  authStore.restoreAuth()
  
  // Загружаем все данные параллельно
  await Promise.all([
    loadBanner(),
    loadEvents(),
    loadPosts(),
    loadAuthors(),
    loadAlbums()
  ])
})
</script>