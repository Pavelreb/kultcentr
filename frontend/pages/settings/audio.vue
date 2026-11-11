<!-- frontend/pages/settings/audio.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4 pb-16">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-teal-500 dark:text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/>
        </svg>
        Аудиотека
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
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут управлять аудиотекой.</p>
    </div>

    <template v-else>
      <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow mb-6">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">Список аудиозаписей ({{ audios.length }})</h2>
          <button
            v-if="!formVisible"
            @click="openCreateForm"
            class="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-teal-500 to-teal-600 text-white rounded-xl hover:from-teal-600 hover:to-teal-700 transition-all duration-300 text-sm font-medium"
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

        <p v-else-if="audios.length === 0" class="text-gray-500 dark:text-gray-400 text-sm py-4">
          Аудиозаписей пока нет. Нажмите «Добавить», чтобы загрузить первую.
        </p>

        <div v-else class="space-y-2">
          <div
            v-for="audio in audios"
            :key="audio.id"
            class="flex items-center gap-3 p-3 rounded-xl border border-gray-100 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700/40 transition"
          >
            <div class="w-10 h-10 rounded-lg overflow-hidden flex-shrink-0 bg-gradient-to-br from-teal-500 to-emerald-600 flex items-center justify-center">
              <img v-if="audio.cover_display" :src="audio.cover_display" class="w-full h-full object-cover" alt="">
              <svg v-else class="w-5 h-5 text-white/80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/>
              </svg>
            </div>
            <div class="flex-1 min-w-0">
              <p class="font-medium text-gray-800 dark:text-gray-200 truncate">
                {{ audio.title }}
                <span v-if="!audio.is_published" class="ml-2 text-xs text-amber-600 dark:text-amber-400">(скрыта)</span>
              </p>
              <p class="text-sm text-gray-500 dark:text-gray-400 truncate">
                {{ formatDuration(audio.duration) }}
              </p>
            </div>
            <button
              @click="openEditForm(audio)"
              class="px-3 py-1.5 text-sm text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/20 rounded-lg transition"
            >
              Изменить
            </button>
            <button
              @click="removeAudio(audio)"
              class="px-3 py-1.5 text-sm text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
            >
              Удалить
            </button>
          </div>
        </div>
      </div>

      <div v-if="formVisible" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 mb-4">
          {{ editingId ? 'Редактировать аудиозапись' : 'Новая аудиозапись' }}
        </h2>

        <form @submit.prevent="submitForm" enctype="multipart/form-data" class="space-y-4">
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Название <span class="text-red-500">*</span></label>
            <input v-model="form.title" type="text" required placeholder="Песня в исполнении ансамбля"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-teal-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
          </div>

          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Описание</label>
            <textarea v-model="form.description" rows="3" placeholder="Необязательно: пара слов о записи"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-teal-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"></textarea>
          </div>

          <!-- Файл аудио -->
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Файл аудио {{ editingId ? '' : '*' }}</label>

            <div v-if="form.file_display && !fileRemoved && !file" class="mb-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
              <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Текущая запись:</p>
              <div class="flex items-center gap-3">
                <a :href="form.file_display" target="_blank" rel="noopener" class="text-sm text-teal-600 dark:text-teal-400 hover:underline truncate">
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
                accept=".mp3,.wav,.ogg,.m4a,.flac,.aac"
                @change="onFileSelected"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-teal-50 file:text-teal-700 hover:file:bg-teal-100 dark:file:bg-teal-900/30 dark:file:text-teal-400"
              />
              <div class="flex items-center gap-2">
                <span class="text-gray-400 dark:text-gray-500 text-sm">или</span>
                <input
                  v-model="form.audio_url"
                  type="url"
                  placeholder="https://example.com/audio.mp3"
                  class="flex-1 border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-teal-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
                  @input="onUrlInput"
                />
              </div>
            </div>
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">
              Форматы: MP3, WAV, OGG, M4A, FLAC, AAC. Максимум 50 МБ. При загрузке запись автоматически конвертируется в MP3.
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
            :file="coverFile"
            :url="form.cover_url"
            :current-url="coverRemoved ? '' : (form.cover_display || '')"
            label="Обложка (необязательно)"
            hint="Рекомендуется квадратная, например 600×600"
            @update:file="onCoverFile"
            @update:url="onCoverUrl"
            @remove="coverRemoved = true"
          />

          <div class="flex items-center">
            <label class="flex items-center gap-2 cursor-pointer">
              <input v-model="form.is_published" type="checkbox" class="w-4 h-4 text-teal-500 rounded focus:ring-2 focus:ring-teal-500 cursor-pointer" />
              <span class="text-gray-700 dark:text-gray-300 text-sm">Опубликовано (видно на сайте)</span>
            </label>
          </div>

          <div class="flex flex-wrap gap-3 pt-4 border-t border-gray-100 dark:border-gray-700">
            <button type="submit" :disabled="submitting"
              class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-teal-500 to-teal-600 text-white rounded-xl hover:from-teal-600 hover:to-teal-700 transition-all duration-300 font-medium shadow-lg shadow-teal-500/25 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed">
              {{ submitting ? 'Сохранение (конвертация)...' : (editingId ? 'Сохранить изменения' : 'Добавить аудио') }}
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
  title: 'Настройки: аудиотека'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()

const audios = ref([])
const loading = ref(true)
const submitting = ref(false)
const error = ref('')
const success = ref('')

const formVisible = ref(false)
const editingId = ref(null)
const file = ref(null)
const coverFile = ref(null)
const coverRemoved = ref(false)
const fileRemoved = ref(false)

const ALLOWED_EXT = ['mp3', 'wav', 'ogg', 'm4a', 'flac', 'aac']
const MAX_SIZE = 50 * 1024 * 1024

const emptyForm = () => ({
  title: '',
  description: '',
  audio_url: '',
  file_display: '',
  cover_url: '',
  cover_display: '',
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
    alert('Файл слишком большой. Максимум 50 МБ.')
    event.target.value = ''
    return
  }
  file.value = f
  form.value.audio_url = ''
  fileRemoved.value = false
}

const onUrlInput = () => {
  const url = form.value.audio_url.trim()
  if (url && isValidUrl(url)) {
    file.value = null
    fileRemoved.value = false
  }
}

const clearFile = () => {
  file.value = null
  form.value.audio_url = ''
}

const onCoverFile = (f) => {
  coverFile.value = f
  if (f) {
    form.value.cover_url = ''
    coverRemoved.value = false
  }
}

const onCoverUrl = (url) => {
  form.value.cover_url = url
  if (url && isValidUrl(url)) {
    coverFile.value = null
    coverRemoved.value = false
  }
}

const loadAudios = async () => {
  loading.value = true
  try {
    const res = await apiFetch(`${API_URL}/medialib/audio/`)
    if (res.ok) audios.value = await res.json()
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
  coverFile.value = null
  coverRemoved.value = false
  fileRemoved.value = false
  error.value = ''
  formVisible.value = true
}

const openEditForm = (audio) => {
  editingId.value = audio.id
  form.value = {
    title: audio.title || '',
    description: audio.description || '',
    audio_url: audio.audio_url || '',
    file_display: audio.file_display || '',
    cover_url: '',
    cover_display: audio.cover_display || '',
    is_published: audio.is_published !== undefined ? audio.is_published : true
  }
  file.value = null
  coverFile.value = null
  coverRemoved.value = false
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
  if (!editingId.value && !file.value && !(form.value.audio_url && isValidUrl(form.value.audio_url))) {
    error.value = 'Выберите файл аудио или укажите ссылку'
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
      formData.append('audio_url', '')
    } else if (file.value) {
      formData.append('file', file.value)
    } else if (form.value.audio_url && isValidUrl(form.value.audio_url)) {
      formData.append('audio_url', form.value.audio_url)
    }

    if (coverFile.value) {
      formData.append('cover', coverFile.value)
    } else if (form.value.cover_url && isValidUrl(form.value.cover_url)) {
      formData.append('cover_url', form.value.cover_url)
    } else if (editingId.value && coverRemoved.value) {
      // очистка обложки: отдельный JSON-запрос (пустой файл в multipart не принимается)
      await apiFetch(`${API_URL}/medialib/audio/${editingId.value}/`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ cover: null, cover_url: '' })
      })
    }

    const url = editingId.value ? `${API_URL}/medialib/audio/${editingId.value}/` : `${API_URL}/medialib/audio/`
    const res = await apiFetch(url, { method: editingId.value ? 'PUT' : 'POST', body: formData })

    if (res.ok) {
      success.value = editingId.value ? 'Аудиозапись обновлена!' : 'Аудиозапись добавлена!'
      setTimeout(() => { success.value = '' }, 3000)
      closeForm()
      await loadAudios()
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

const removeAudio = async (audio) => {
  if (!confirm(`Удалить аудиозапись «${audio.title}»?`)) return
  try {
    const res = await apiFetch(`${API_URL}/medialib/audio/${audio.id}/`, { method: 'DELETE' })
    if (res.ok || res.status === 204) {
      success.value = 'Аудиозапись удалена.'
      setTimeout(() => { success.value = '' }, 3000)
      await loadAudios()
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
  if (authStore.isEditor) await loadAudios()
})
</script>
