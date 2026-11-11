<!-- frontend/pages/settings/videos.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4 pb-16">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-rose-500 dark:text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/>
        </svg>
        Видеотека
      </h1>
      <NuxtLink
        to="/settings"
        class="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 hover:-translate-y-0.5"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
        </svg>
        Все настройки
      </NuxtLink>
    </div>

    <div v-if="!authStore.isEditor" class="bg-white dark:bg-gray-800 p-8 rounded-lg shadow text-center py-20">
      <svg class="w-24 h-24 mx-auto text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
      </svg>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут управлять видеотекой.</p>
    </div>

    <template v-else>
      <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow mb-6">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">Список видеороликов ({{ videos.length }})</h2>
          <button
            v-if="!formVisible"
            @click="openCreateForm"
            class="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-rose-500 to-rose-600 text-white rounded-xl hover:from-rose-600 hover:to-rose-700 transition-all duration-300 text-sm font-medium"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
            </svg>
            Добавить
          </button>
        </div>

        <div v-if="loading" class="space-y-2">
          <div v-for="n in 4" :key="n" class="h-14 bg-gray-100 dark:bg-gray-700 rounded-lg animate-pulse"></div>
        </div>

        <p v-else-if="videos.length === 0" class="text-gray-500 dark:text-gray-400 text-sm py-4">
          Видеороликов пока нет. Нажмите «Добавить», чтобы загрузить первый.
        </p>

        <div v-else class="space-y-2">
          <div
            v-for="video in videos"
            :key="video.id"
            class="flex items-center gap-3 p-3 rounded-xl border border-gray-100 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700/40 transition"
          >
            <div class="w-16 h-10 rounded-lg overflow-hidden flex-shrink-0 bg-gradient-to-br from-rose-500 to-red-600 flex items-center justify-center">
              <img v-if="video.thumbnail_display" :src="video.thumbnail_display" class="w-full h-full object-cover" alt="">
              <svg v-else class="w-5 h-5 text-white/80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/>
              </svg>
            </div>
            <div class="flex-1 min-w-0">
              <p class="font-medium text-gray-800 dark:text-gray-200 truncate">
                {{ video.title }}
                <span v-if="!video.is_published" class="ml-2 text-xs text-amber-600 dark:text-amber-400">(скрыт)</span>
              </p>
              <p class="text-sm text-gray-500 dark:text-gray-400 truncate">
                {{ formatDuration(video.duration) }}
              </p>
            </div>
            <NuxtLink
              :to="`/media/videos/${video.id}`"
              class="px-3 py-1.5 text-sm text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition"
            >
              Открыть
            </NuxtLink>
            <button
              @click="openEditForm(video)"
              class="px-3 py-1.5 text-sm text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/20 rounded-lg transition"
            >
              Изменить
            </button>
            <button
              @click="removeVideo(video)"
              class="px-3 py-1.5 text-sm text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
            >
              Удалить
            </button>
          </div>
        </div>
      </div>

      <div v-if="formVisible" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 mb-4">
          {{ editingId ? 'Редактировать видеоролик' : 'Новый видеоролик' }}
        </h2>

        <form @submit.prevent="submitForm" enctype="multipart/form-data" class="space-y-4">
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Название <span class="text-red-500">*</span></label>
            <input v-model="form.title" type="text" required placeholder="Концерт ко Дню Победы"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-rose-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
          </div>

          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Описание</label>
            <textarea v-model="form.description" rows="3" placeholder="Необязательно: о чём это видео"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-rose-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"></textarea>
          </div>

          <!-- Файл видео -->
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Файл видео {{ editingId ? '' : '*' }}</label>

            <div v-if="form.file_display && !fileRemoved && !file" class="mb-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
              <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Текущее видео:</p>
              <div class="flex items-center gap-3">
                <a :href="form.file_display" target="_blank" rel="noopener" class="text-sm text-rose-600 dark:text-rose-400 hover:underline truncate">
                  {{ form.title }}
                </a>
                <button type="button" @click="fileRemoved = true"
                  class="px-3 py-1.5 text-sm text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition flex-shrink-0">
                  Удалить
                </button>
              </div>
            </div>

            <div class="flex flex-col gap-2">
              <input
                type="file"
                accept=".mp4,.mov,.avi,.mkv,.webm"
                @change="onFileSelected"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-rose-50 file:text-rose-700 hover:file:bg-rose-100 dark:file:bg-rose-900/30 dark:file:text-rose-400"
              />
              <div class="flex items-center gap-2">
                <span class="text-gray-400 dark:text-gray-500 text-sm">или</span>
                <input
                  v-model="form.video_url"
                  type="url"
                  placeholder="https://example.com/video.mp4"
                  class="flex-1 border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-rose-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
                  @input="onUrlInput"
                />
              </div>
            </div>
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">
              Форматы: MP4, MOV, AVI, MKV, WEBM. Максимум 500 МБ. При загрузке видео автоматически сжимается — сохранение может занять некоторое время.
            </p>

            <div v-if="file" class="mt-2 flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
              <div class="flex-1 min-w-0">
                <p class="text-sm font-medium text-gray-700 dark:text-gray-300 truncate">{{ file.name }}</p>
                <p class="text-xs text-gray-400 dark:text-gray-500">{{ formatBytes(file.size) }}</p>
              </div>
              <button type="button" @click="clearFile"
                class="px-3 py-1.5 text-sm text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition">
                Удалить
              </button>
            </div>
          </div>

          <!-- Обложка -->
          <ImageField
            :file="thumbnailFile"
            :url="form.thumbnail_url"
            :current-url="thumbnailRemoved ? '' : (form.thumbnail_display || '')"
            label="Обложка (необязательно)"
            hint="Рекомендуется 16:9, например 1280×720"
            @update:file="onThumbnailFile"
            @update:url="onThumbnailUrl"
            @remove="thumbnailRemoved = true"
          />

          <div class="flex items-center">
            <label class="flex items-center gap-2 cursor-pointer">
              <input v-model="form.is_published" type="checkbox" class="w-4 h-4 text-rose-500 rounded focus:ring-2 focus:ring-rose-500 cursor-pointer" />
              <span class="text-gray-700 dark:text-gray-300 text-sm">Опубликовано (видно на сайте)</span>
            </label>
          </div>

          <div class="flex flex-wrap gap-3 pt-4 border-t border-gray-100 dark:border-gray-700">
            <button type="submit" :disabled="submitting"
              class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-rose-500 to-rose-600 text-white rounded-xl hover:from-rose-600 hover:to-rose-700 transition-all duration-300 font-medium shadow-lg shadow-rose-500/25 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed">
              {{ submitting ? 'Сохранение (сжатие видео)...' : (editingId ? 'Сохранить изменения' : 'Добавить видео') }}
            </button>
            <button type="button" @click="closeForm"
              class="px-6 py-3 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 font-medium">
              Отмена
            </button>
          </div>

          <p v-if="error" class="text-red-500 text-sm">{{ error }}</p>
        </form>
      </div>

      <p v-if="success" class="mt-4 text-green-500 text-sm">{{ success }}</p>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import ImageField from '~/components/common/ImageField.vue'

definePageMeta({
  middleware: ['auth', 'editor']
})

useSeoMeta({
  title: 'Настройки: видеотека'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()

const videos = ref([])
const loading = ref(true)
const submitting = ref(false)
const error = ref('')
const success = ref('')

const formVisible = ref(false)
const editingId = ref(null)
const file = ref(null)
const thumbnailFile = ref(null)
const thumbnailRemoved = ref(false)
const fileRemoved = ref(false)

const ALLOWED_EXT = ['mp4', 'mov', 'avi', 'mkv', 'webm']
const MAX_SIZE = 500 * 1024 * 1024

const emptyForm = () => ({
  title: '',
  description: '',
  video_url: '',
  file_display: '',
  thumbnail_url: '',
  thumbnail_display: '',
  is_published: true
})

const form = ref(emptyForm())

const isValidUrl = (string) => {
  try {
    const u = new URL(string)
    return u.protocol === 'http:' || u.protocol === 'https:'
  } catch (_) {
    return false
  }
}

const formatBytes = (bytes) => {
  if (!bytes) return ''
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(0) + ' КБ'
  return (bytes / (1024 * 1024)).toFixed(1) + ' МБ'
}

const formatDuration = (sec) => {
  if (!sec) return '—'
  const m = Math.floor(sec / 60)
  const s = sec % 60
  return `${m}:${String(s).padStart(2, '0')}`
}

const onFileSelected = (event) => {
  const f = event.target.files[0]
  if (!f) return
  const ext = f.name.includes('.') ? f.name.split('.').pop().toLowerCase() : ''
  if (!ALLOWED_EXT.includes(ext)) {
    alert('Неподдерживаемый формат. Разрешены: ' + ALLOWED_EXT.join(', ').toUpperCase())
    event.target.value = ''
    return
  }
  if (f.size > MAX_SIZE) {
    alert('Файл слишком большой. Максимум 500 МБ.')
    event.target.value = ''
    return
  }
  file.value = f
  form.value.video_url = ''
  fileRemoved.value = false
}

const onUrlInput = () => {
  const url = form.value.video_url.trim()
  if (url && isValidUrl(url)) {
    file.value = null
    fileRemoved.value = false
  }
}

const onThumbnailFile = (f) => {
  thumbnailFile.value = f
  if (f) {
    form.value.thumbnail_url = ''
    thumbnailRemoved.value = false
  }
}

const onThumbnailUrl = (url) => {
  form.value.thumbnail_url = url
  if (url && isValidUrl(url)) {
    thumbnailFile.value = null
    thumbnailRemoved.value = false
  }
}

const clearFile = () => {
  file.value = null
  form.value.video_url = ''
}

const loadVideos = async () => {
  loading.value = true
  try {
    const res = await apiFetch(`${API_URL}/medialib/videos/`)
    if (res.ok) videos.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки:', e)
  } finally {
    loading.value = false
  }
}

const openCreateForm = () => {
  editingId.value = null
  form.value = emptyForm()
  file.value = null
  thumbnailFile.value = null
  thumbnailRemoved.value = false
  fileRemoved.value = false
  error.value = ''
  formVisible.value = true
}

const openEditForm = (video) => {
  editingId.value = video.id
  form.value = {
    title: video.title || '',
    description: video.description || '',
    video_url: video.video_url || '',
    file_display: video.file_display || '',
    thumbnail_url: '',
    thumbnail_display: video.thumbnail_display || '',
    is_published: video.is_published !== undefined ? video.is_published : true
  }
  file.value = null
  thumbnailFile.value = null
  thumbnailRemoved.value = false
  fileRemoved.value = false
  error.value = ''
  formVisible.value = true
}

const closeForm = () => {
  formVisible.value = false
  editingId.value = null
  error.value = ''
}

const submitForm = async () => {
  if (!form.value.title) {
    error.value = 'Заполните название'
    return
  }
  if (!editingId.value && !file.value && !(form.value.video_url && isValidUrl(form.value.video_url))) {
    error.value = 'Выберите файл видео или укажите ссылку'
    return
  }

  submitting.value = true
  error.value = ''

  try {
    const formData = new FormData()
    formData.append('title', form.value.title)
    formData.append('description', form.value.description || '')
    formData.append('is_published', form.value.is_published ? 'true' : 'false')

    if (fileRemoved.value) {
      formData.append('video_url', '')
    } else if (file.value) {
      formData.append('file', file.value)
    } else if (form.value.video_url && isValidUrl(form.value.video_url)) {
      formData.append('video_url', form.value.video_url)
    }

    if (thumbnailFile.value) {
      formData.append('thumbnail', thumbnailFile.value)
    } else if (form.value.thumbnail_url && isValidUrl(form.value.thumbnail_url)) {
      formData.append('thumbnail_url', form.value.thumbnail_url)
    } else if (editingId.value && thumbnailRemoved.value) {
      // очистка обложки: отдельный JSON-запрос (пустой файл в multipart не принимается)
      await apiFetch(`${API_URL}/medialib/videos/${editingId.value}/`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ thumbnail: null, thumbnail_url: '' })
      })
    }

    const url = editingId.value ? `${API_URL}/medialib/videos/${editingId.value}/` : `${API_URL}/medialib/videos/`
    const res = await apiFetch(url, { method: editingId.value ? 'PUT' : 'POST', body: formData })

    if (res.ok) {
      success.value = editingId.value ? 'Видеоролик обновлён!' : 'Видеоролик добавлен!'
      setTimeout(() => { success.value = '' }, 3000)
      closeForm()
      await loadVideos()
    } else {
      const data = await res.json().catch(() => ({}))
      error.value = data.detail || 'Ошибка сохранения'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}

const removeVideo = async (video) => {
  if (!confirm(`Удалить видеоролик «${video.title}»?`)) return
  try {
    const res = await apiFetch(`${API_URL}/medialib/videos/${video.id}/`, { method: 'DELETE' })
    if (res.ok || res.status === 204) {
      success.value = 'Видеоролик удалён.'
      setTimeout(() => { success.value = '' }, 3000)
      await loadVideos()
    } else {
      error.value = 'Ошибка удаления'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  }
}

onMounted(async () => {
  authStore.restoreAuth()
  if (authStore.isEditor) await loadVideos()
})
</script>
