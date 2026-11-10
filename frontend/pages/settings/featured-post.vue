<!-- frontend/pages/settings/featured-post.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-green-500 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
        </svg>
        Главная публикация
      </h1>
      <NuxtLink
        to="/settings"
        class="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 hover:-translate-y-0.5"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
        </svg>
        Все настройки
      </NuxtLink>
    </div>

    <div v-if="!authStore.isEditor" class="bg-white dark:bg-gray-800 p-8 rounded-lg shadow text-center py-20">
      <svg class="w-24 h-24 mx-auto text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
      </svg>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут управлять настройками сайта.</p>
    </div>

    <div v-else class="bg-white dark:bg-gray-800 rounded-xl shadow-md p-6 border border-gray-100 dark:border-gray-700">
      <p class="text-sm text-gray-500 dark:text-gray-400 mb-4">
        Выбранная публикация будет закреплена наверху страницы «Публикации».
        Показаны только опубликованные публикации.
      </p>

      <div v-if="loading" class="text-center py-10 text-gray-500 dark:text-gray-400">
        Загрузка…
      </div>

      <template v-else>
        <!-- Автоматический режим -->
        <label
          class="flex items-center gap-3 p-4 mb-3 rounded-xl border cursor-pointer transition-all duration-300"
          :class="selected === 'auto'
            ? 'border-green-500 bg-green-50 dark:bg-green-900/20'
            : 'border-gray-200 dark:border-gray-700 hover:border-green-300 dark:hover:border-green-700'"
        >
          <input type="radio" v-model="selected" value="auto" class="w-4 h-4 text-green-600" />
          <div>
            <div class="font-medium text-gray-800 dark:text-gray-200">Автоматически</div>
            <div class="text-xs text-gray-400 dark:text-gray-500">Главной становится самая свежая публикация</div>
          </div>
        </label>

        <div v-if="posts.length === 0" class="text-center py-6 text-gray-500 dark:text-gray-400">
          Нет опубликованных публикаций.
        </div>

        <div v-else class="space-y-3 max-h-[60vh] overflow-y-auto pr-1">
          <label
            v-for="post in posts"
            :key="post.id"
            class="flex items-center gap-3 p-4 rounded-xl border cursor-pointer transition-all duration-300"
            :class="selected === post.id
              ? 'border-green-500 bg-green-50 dark:bg-green-900/20'
              : 'border-gray-200 dark:border-gray-700 hover:border-green-300 dark:hover:border-green-700'"
          >
            <input type="radio" v-model="selected" :value="post.id" class="w-4 h-4 text-green-600 flex-shrink-0" />
            <img
              v-if="post.display_image"
              :src="post.display_image"
              :alt="post.title"
              class="w-16 h-10 object-cover rounded-lg flex-shrink-0"
            />
            <div class="min-w-0">
              <div class="font-medium text-gray-800 dark:text-gray-200 truncate">{{ post.title }}</div>
              <div class="text-xs text-gray-400 dark:text-gray-500">
                {{ post.author_full_name || post.author_name }} · {{ formatDate(post.created_at) }}
                <span v-if="post.is_featured" class="ml-1 text-green-600 dark:text-green-400 font-medium">· сейчас главная</span>
              </div>
            </div>
          </label>
        </div>

        <div class="mt-6 flex items-center gap-4">
          <button
            @click="save"
            :disabled="saving"
            class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-green-500 to-green-600 text-white rounded-xl hover:from-green-600 hover:to-green-700 transition-all duration-300 font-medium shadow-lg shadow-green-500/25 hover:shadow-xl hover:shadow-green-500/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0"
          >
            {{ saving ? 'Сохранение…' : 'Сохранить' }}
          </button>
          <span v-if="message" class="text-sm" :class="messageError ? 'text-red-500' : 'text-green-600 dark:text-green-400'">
            {{ message }}
          </span>
        </div>
      </template>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: ['auth', 'editor']
})

useSeoMeta({
  title: 'Главная публикация'
})

const authStore = useAuthStore()
const { apiFetch } = useApi()
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const posts = ref([])
const loading = ref(true)
const saving = ref(false)
const selected = ref('auto')
const message = ref('')
const messageError = ref(false)

const formatDate = (dateStr) => {
  if (!dateStr) return ''
  return new Date(dateStr).toLocaleDateString('ru-RU', {
    day: 'numeric', month: 'long', year: 'numeric'
  })
}

const loadPosts = async () => {
  loading.value = true
  try {
    const res = await apiFetch(`${API_URL}/posts/`)
    posts.value = await res.json()
    const current = posts.value.find(p => p.is_featured)
    selected.value = current ? current.id : 'auto'
  } catch (e) {
    console.error('Ошибка загрузки публикаций:', e)
  } finally {
    loading.value = false
  }
}

const save = async () => {
  saving.value = true
  message.value = ''
  try {
    const url = selected.value === 'auto'
      ? `${API_URL}/posts/unfeature/`
      : `${API_URL}/posts/${selected.value}/feature/`
    const res = await apiFetch(url, { method: 'POST' })
    if (!res.ok) {
      const data = await res.json().catch(() => ({}))
      throw new Error(data.detail || 'Ошибка сохранения')
    }
    messageError.value = false
    message.value = 'Сохранено'
    await loadPosts()
  } catch (e) {
    messageError.value = true
    message.value = e.message || 'Ошибка сохранения'
  } finally {
    saving.value = false
  }
}

onMounted(() => {
  authStore.restoreAuth()
  loadPosts()
})
</script>
