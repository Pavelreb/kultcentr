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
          <div class="relative w-28 h-28 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-4xl font-bold overflow-hidden flex-shrink-0 shadow-lg">
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
              <!-- Онлайн-статус -->
              <span
                class="inline-flex items-center gap-1.5 self-center px-3 py-1 rounded-full text-xs font-medium"
                :class="user.is_online
                  ? 'bg-emerald-100 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-300'
                  : 'bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400'"
              >
                <span
                  class="w-2 h-2 rounded-full"
                  :class="user.is_online ? 'bg-emerald-500 animate-pulse' : 'bg-gray-400'"
                ></span>
                {{ user.is_online ? 'В сети' : 'Не в сети' }}
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
              <a v-if="user.phone" :href="`tel:${user.phone}`" class="flex items-center gap-1.5 hover:text-blue-500 transition">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                </svg>
                {{ user.phone }}
              </a>
              <a v-if="user.email" :href="`mailto:${user.email}`" class="flex items-center gap-1.5 hover:text-blue-500 transition">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                </svg>
                {{ user.email }}
              </a>
              <span class="flex items-center gap-1.5">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
                Подписчиков: {{ user.subscribers_count || 0 }}
              </span>
              <span class="flex items-center gap-1.5">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
                На сайте с {{ formatDate(user.date_joined) }}
              </span>
            </div>

            <!-- Кнопка подписки (только для авторов/редакторов, не для себя) -->
            <div v-if="isCreator && !isSelf" class="mt-4 flex justify-center sm:justify-start">
              <button
                v-if="authStore.isAuthenticated"
                @click="toggleSubscribe"
                :disabled="subscribing"
                class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-medium transition-all duration-300 disabled:opacity-50"
                :class="user.is_subscribed
                  ? 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'
                  : 'bg-gradient-to-r from-blue-500 to-blue-600 text-white hover:from-blue-600 hover:to-blue-700 shadow-lg shadow-blue-500/25 hover:-translate-y-0.5'"
              >
                <svg v-if="user.is_subscribed" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <svg v-else class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/>
                </svg>
                {{ subscribing ? 'Подождите...' : user.is_subscribed ? 'Вы подписаны' : 'Подписаться' }}
              </button>
              <NuxtLink
                v-else
                to="/auth/login"
                class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-medium bg-gradient-to-r from-blue-500 to-blue-600 text-white hover:from-blue-600 hover:to-blue-700 shadow-lg shadow-blue-500/25 transition-all duration-300 hover:-translate-y-0.5"
              >
                Войдите, чтобы подписаться
              </NuxtLink>
            </div>

            <!-- Социальные сети пользователя (если разрешил показ) -->
            <div v-if="user.vk || user.max || user.ok || user.rutube" class="flex justify-center sm:justify-start gap-3 mt-4">
              <a v-if="user.vk" :href="user.vk" target="_blank" title="ВКонтакте"
                class="w-9 h-9 rounded-full bg-blue-600 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow">
                <svg class="w-[18px] h-[18px]" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M13.162 18.994c.609 0 .858-.406.851-.915-.031-1.917.714-2.949 2.059-1.604 1.488 1.488 1.796 2.519 3.603 2.519h3.2c.808 0 1.126-.26 1.126-.668 0-.863-1.421-2.386-2.625-3.504-1.686-1.565-1.765-1.602-.313-3.486 1.507-1.949 2.505-3.995 1.628-4.147-.244-.04-1.183-.05-2.303.018-.079.008-.146.03-.206.066-.128.075-.252.17-.389.291-1.158 1.039-2.208 2.313-2.562 2.486-.105.052-.18.063-.259.045-.142-.034-.338-.212-.354-.944-.028-1.258-.341-2.021-.946-2.384-.283-.17-.494-.262-1.371-.252-.674.007-1.172.055-1.613.336-.24.153-.383.367-.565.763-.07.153-.146.354-.226.617-.242.788-.483 1.574-1.037 2.287-.335.431-.748.899-1.155 1.331-.133.143-.255.273-.38.399-.425.428-.729.459-.915.445-.389-.029-.786-.044-1.054-.11-.703-.174-1.004-.854-1.08-1.398-.037-.265-.117-.712-.132-.997-.034-.663-.172-1.164-.628-1.455-.273-.174-.655-.249-1.273-.252-.816-.004-1.337.161-1.582.611-.21.386-.091.979.009 1.279.067.201.186.436.315.685.344.664.736 1.421 1.248 2.134.87 1.213 1.62 2.116 2.546 3.087.886.93 1.751 1.487 2.713 1.805.449.149.761.205 1.141.21z"/>
                </svg>
              </a>
              <a v-if="user.max" :href="user.max" target="_blank" title="MAX"
                class="w-9 h-9 rounded-full bg-gradient-to-br from-purple-500 to-indigo-600 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow">
                <svg class="w-[18px] h-[18px]" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2C6.48 2 2 6.02 2 11c0 2.4 1.05 4.6 2.77 6.27-.13.86-.65 2.47-1.65 3.73 1.4-.08 3.13-.68 4.16-1.22.86.25 1.78.39 2.72.39 5.52 0 10-4.02 10-8.97S17.52 2 12 2zm-4.5 9.5a1.5 1.5 0 110-3 1.5 1.5 0 010 3zm4.5 0a1.5 1.5 0 110-3 1.5 1.5 0 010 3zm4.5 0a1.5 1.5 0 110-3 1.5 1.5 0 010 3z"/>
                </svg>
              </a>
              <a v-if="user.ok" :href="user.ok" target="_blank" title="Одноклассники"
                class="w-9 h-9 rounded-full bg-orange-500 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow">
                <svg class="w-[18px] h-[18px]" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2a5 5 0 00-5 5c0 2.76 2.24 5 5 5s5-2.24 5-5a5 5 0 00-5-5zm0 8a3 3 0 110-6 3 3 0 010 6zm5.83 3.42a1.25 1.25 0 00-1.77-.15c-1.1.94-2.55 1.5-4.06 1.5s-2.96-.56-4.06-1.5a1.25 1.25 0 10-1.62 1.9c1.28 1.1 2.87 1.76 4.55 1.93l-2.6 3.9a1.25 1.25 0 102.06 1.4L12 19.66l1.67 2.51a1.25 1.25 0 102.06-1.4l-2.6-3.9c1.68-.17 3.27-.83 4.55-1.93.5-.42.56-1.17.15-1.62z"/>
                </svg>
              </a>
              <a v-if="user.rutube" :href="user.rutube" target="_blank" title="RuTube"
                class="w-9 h-9 rounded-full bg-gray-900 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow">
                <svg class="w-[18px] h-[18px]" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Публикации автора/редактора -->
      <template v-if="isCreator">
        <!-- Статистика автора -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-6">
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-4 text-center">
            <div class="text-xl font-bold text-gray-800 dark:text-gray-200">{{ user.posts_count || 0 }}</div>
            <div class="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Публикаций</div>
          </div>
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-4 text-center">
            <div class="text-xl font-bold text-gray-800 dark:text-gray-200">{{ user.total_views || 0 }}</div>
            <div class="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Просмотров</div>
          </div>
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-4 text-center">
            <div class="text-xl font-bold text-gray-800 dark:text-gray-200">{{ user.total_likes || 0 }}</div>
            <div class="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Лайков</div>
          </div>
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-4 text-center">
            <div class="text-xl font-bold text-gray-800 dark:text-gray-200">{{ user.total_comments || 0 }}</div>
            <div class="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Комментариев</div>
          </div>
        </div>

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
import { useAuthStore } from '~/store/auth'
import PostCard from '~/components/features/posts/PostCard.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const { apiFetch } = useApi()
const route = useRoute()
const authStore = useAuthStore()

const user = ref(null)
const posts = ref([])
const loading = ref(true)
const postsLoading = ref(false)
const subscribing = ref(false)

const isSelf = computed(() => authStore.user?.id === user.value?.id)

const toggleSubscribe = async () => {
  if (subscribing.value) return
  subscribing.value = true
  try {
    const res = await apiFetch(`${API_URL}/auth/users/${user.value.id}/subscribe/`, {
      method: 'POST'
    })
    if (res.ok) {
      const data = await res.json()
      user.value.is_subscribed = data.subscribed
      user.value.subscribers_count = data.subscribers_count
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    subscribing.value = false
  }
}

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
  authStore.restoreAuth()
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
