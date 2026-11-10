<!-- frontend/pages/users/[id].vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4 pb-16">
    <!-- Хлебные крошки -->
    <Breadcrumb :items="breadcrumbItems" />

    <div v-if="loading" class="text-center py-20 text-gray-500 dark:text-gray-400">
      Загрузка…
    </div>

    <div v-else-if="!user" class="bg-white dark:bg-gray-800 p-8 rounded-xl shadow text-center py-20">
      <svg class="w-24 h-24 mx-auto text-gray-300 dark:text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
      </svg>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mt-4 mb-2">Пользователь не найден</h2>
      <NuxtLink to="/" class="text-blue-500 dark:text-blue-400 hover:underline">На главную</NuxtLink>
    </div>

    <template v-else>
      <!-- Карточка профиля -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-6 mb-8">
        <div class="flex flex-col sm:flex-row items-center sm:items-start gap-6">
          <!-- Аватар -->
          <div class="w-28 h-28 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-4xl font-bold overflow-hidden flex-shrink-0 shadow-lg">
            <img v-if="user.avatar_url" :src="user.avatar_url" :alt="user.username" class="w-full h-full object-cover" />
            <span v-else>{{ getInitials(user) }}</span>
          </div>

          <div class="flex-1 text-center sm:text-left min-w-0">
            <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3">
              <h1 class="text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200 truncate">
                {{ user.full_name || user.username }}
              </h1>
              <span
                class="inline-flex items-center self-center px-3 py-1 rounded-full text-xs font-medium"
                :class="roleBadgeClass"
              >
                {{ user.role_display }}
              </span>
            </div>
            <p class="text-gray-400 dark:text-gray-500 text-sm mt-1">@{{ user.username }}</p>

            <p v-if="user.bio" class="text-gray-600 dark:text-gray-300 mt-3 whitespace-pre-wrap">{{ user.bio }}</p>

            <div class="flex flex-wrap justify-center sm:justify-start gap-x-6 gap-y-2 mt-4 text-sm text-gray-500 dark:text-gray-400">
              <span class="flex items-center gap-1.5">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
                </svg>
                Публикаций: {{ user.posts_count || 0 }}
              </span>
              <span class="flex items-center gap-1.5">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
                На сайте с {{ formatDate(user.date_joined) }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Публикации автора/редактора -->
      <template v-if="isCreator">
        <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-4 flex items-center gap-2">
          <svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
          </svg>
          Публикации
        </h2>

        <div v-if="postsLoading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <div v-for="n in 3" :key="n" class="bg-white dark:bg-gray-800 rounded-xl shadow-md overflow-hidden animate-pulse">
            <div class="aspect-video bg-gray-200 dark:bg-gray-700"></div>
            <div class="p-4 space-y-2">
              <div class="h-4 bg-gray-200 dark:bg-gray-700 rounded w-3/4"></div>
              <div class="h-3 bg-gray-200 dark:bg-gray-700 rounded w-full"></div>
            </div>
          </div>
        </div>

        <div v-else-if="posts.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700">
          <p class="text-gray-500 dark:text-gray-400">Пока нет публикаций</p>
        </div>

        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <PostCard v-for="post in posts" :key="post.id" :post="post" :show-draft-badge="false" />
        </div>
      </template>
    </template>
  </div>
</template>

<script setup>
import PostCard from '~/components/features/posts/PostCard.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const { apiFetch } = useApi()
const route = useRoute()

const user = ref(null)
const posts = ref([])
const loading = ref(true)
const postsLoading = ref(false)

const breadcrumbItems = computed(() => [
  { label: user.value ? (user.value.full_name || user.value.username) : 'Профиль' }
])

const isCreator = computed(() => ['author', 'editor'].includes(user.value?.role))

const roleBadgeClass = computed(() => {
  switch (user.value?.role) {
    case 'editor':
      return 'bg-yellow-100 dark:bg-yellow-900/30 text-yellow-700 dark:text-yellow-300'
    case 'author':
      return 'bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-300'
    default:
      return 'bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300'
  }
})

const getInitials = (u) => {
  const name = u.full_name || u.username || '?'
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  return new Date(dateString).toLocaleDateString('ru-RU', {
    day: 'numeric', month: 'long', year: 'numeric'
  })
}

useHead(() => ({
  title: user.value ? `${user.value.full_name || user.value.username} — Центр Культуры` : 'Профиль — Центр Культуры',
  meta: [
    { name: 'description', content: user.value?.bio ? user.value.bio.substring(0, 160) : 'Профиль пользователя Центра Культуры' }
  ]
}))

onMounted(async () => {
  try {
    const userId = route.params.id

    const userRes = await apiFetch(`${API_URL}/auth/users/${userId}/`)
    if (userRes.ok) {
      user.value = await userRes.json()
    } else {
      user.value = null
      return
    }

    if (isCreator.value && user.value?.username) {
      postsLoading.value = true
      const postsRes = await apiFetch(`${API_URL}/posts/?author_name=${user.value.username}`)
      if (postsRes.ok) {
        // На публичной странице показываем только опубликованные
        posts.value = (await postsRes.json()).filter(p => p.is_published)
      }
      postsLoading.value = false
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>
