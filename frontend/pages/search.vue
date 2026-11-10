<!-- frontend/pages/search.vue -->
<template>
  <div class="container mx-auto p-4">
    <!-- Заголовок -->
    <div class="mb-6">
      <h1 class="text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-6 h-6 text-blue-500 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35M17 11a6 6 0 11-12 0 6 6 0 0112 0z"/>
        </svg>
        Результаты поиска
      </h1>
      <p v-if="query" class="text-gray-500 dark:text-gray-400 mt-1">
        По запросу <span class="font-medium text-gray-700 dark:text-gray-300">«{{ query }}»</span>
        <template v-if="!loading"> — найдено: {{ totalCount }}</template>
      </p>
    </div>

    <!-- Загрузка -->
    <div v-if="loading" class="text-center py-20">
      <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Ищем…</p>
    </div>

    <!-- Ничего не найдено -->
    <div v-else-if="query && totalCount === 0" class="text-center py-20 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 21l-4.35-4.35M17 11a6 6 0 11-12 0 6 6 0 0112 0z"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 9l6 6m0-6l-6 6"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">По запросу «{{ query }}» ничего не найдено</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Попробуйте изменить запрос или посмотрите разделы сайта в меню</p>
    </div>

    <template v-else>
      <!-- Публикации -->
      <section v-if="posts.length > 0" class="mb-10">
        <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4 flex items-center gap-2">
          Публикации
          <span class="text-sm font-normal text-gray-400 dark:text-gray-500">{{ posts.length }}</span>
        </h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-5">
          <PostListItem v-for="post in posts" :key="post.id" :post="post" :show-draft-badge="false" />
        </div>
      </section>

      <!-- Афиша -->
      <section v-if="events.length > 0" class="mb-10">
        <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4 flex items-center gap-2">
          Афиша
          <span class="text-sm font-normal text-gray-400 dark:text-gray-500">{{ events.length }}</span>
        </h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 md:gap-5">
          <EventListItem v-for="event in events" :key="event.id" :event="event" :show-draft-badge="false" />
        </div>
      </section>

      <!-- Фотоальбомы -->
      <section v-if="albums.length > 0" class="mb-10">
        <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4 flex items-center gap-2">
          Фотоальбомы
          <span class="text-sm font-normal text-gray-400 dark:text-gray-500">{{ albums.length }}</span>
        </h2>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 md:gap-5">
          <AlbumCard v-for="album in albums" :key="album.id" :album="album" />
        </div>
      </section>

      <!-- Авторы -->
      <section v-if="authors.length > 0" class="mb-10">
        <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4 flex items-center gap-2">
          Авторы
          <span class="text-sm font-normal text-gray-400 dark:text-gray-500">{{ authors.length }}</span>
        </h2>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 md:gap-5">
          <NuxtLink
            v-for="author in authors"
            :key="author.id"
            :to="`/users/${author.id}`"
            class="group bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden hover:-translate-y-1"
          >
            <div class="p-5 text-center">
              <div class="relative w-20 h-20 mx-auto">
                <img
                  v-if="author.avatar_url"
                  :src="author.avatar_url"
                  :alt="author.full_name || author.username"
                  class="w-20 h-20 rounded-full object-cover border-2 border-gray-100 dark:border-gray-700"
                />
                <div
                  v-else
                  class="w-20 h-20 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-xl font-bold"
                >
                  {{ getInitials(author) }}
                </div>
              </div>
              <h3 class="mt-3 text-sm font-semibold text-gray-800 dark:text-gray-200 group-hover:text-purple-600 dark:group-hover:text-purple-400 transition-colors truncate">
                {{ author.full_name || author.username }}
              </h3>
              <p class="text-xs text-gray-400 dark:text-gray-500">
                {{ author.role === 'editor' ? 'Главный редактор' : 'Автор' }}
              </p>
            </div>
          </NuxtLink>
        </div>
      </section>
    </template>
  </div>
</template>

<script setup>
import PostListItem from '~/components/features/posts/PostListItem.vue'
import EventListItem from '~/components/features/events/EventListItem.vue'
import AlbumCard from '~/components/features/albums/AlbumCard.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const { apiFetch } = useApi()

const query = computed(() => (route.query.q || '').toString().trim())

const posts = ref([])
const events = ref([])
const albums = ref([])
const authors = ref([])
const loading = ref(false)

const totalCount = computed(() =>
  posts.value.length + events.value.length + albums.value.length + authors.value.length
)

const getInitials = (user) => {
  const name = user.full_name || user.username || '?'
  const parts = name.split(' ')
  if (parts.length >= 2) return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  return name.substring(0, 2).toUpperCase()
}

useHead(() => ({
  title: query.value ? `Поиск: ${query.value}` : 'Поиск'
}))

const performSearch = async (q) => {
  if (!q || q.length < 2) {
    posts.value = []
    events.value = []
    albums.value = []
    authors.value = []
    return
  }

  loading.value = true
  try {
    const params = `?search=${encodeURIComponent(q)}`
    const [postsRes, eventsRes, albumsRes, usersRes] = await Promise.all([
      apiFetch(`${API_URL}/posts/${params}`),
      apiFetch(`${API_URL}/events/${params}`),
      apiFetch(`${API_URL}/albums/${params}`),
      apiFetch(`${API_URL}/auth/users/${params}`)
    ])

    posts.value = postsRes.ok ? await postsRes.json() : []
    events.value = eventsRes.ok ? await eventsRes.json() : []
    albums.value = albumsRes.ok ? await albumsRes.json() : []
    const users = usersRes.ok ? await usersRes.json() : []
    // В поиске показываем только авторов и редакцию, как на странице «Авторы»
    authors.value = users.filter(u => u.role === 'author' || u.role === 'editor')
  } catch (e) {
    console.error('Ошибка поиска:', e)
  } finally {
    loading.value = false
  }
}

// Запускаем при открытии страницы и при каждом новом запросе из шапки
watch(query, (q) => performSearch(q), { immediate: true })
</script>
