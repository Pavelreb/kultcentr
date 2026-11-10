<!-- frontend/pages/gallery/edit-[id].vue -->
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 transition-colors duration-200">
    <div v-if="!authStore.isEditor" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">
        <svg class="w-24 h-24 mx-auto text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
        </svg>
      </div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только редакторы могут редактировать альбомы.</p>
      <NuxtLink to="/gallery" class="mt-4 inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-pink-500 to-pink-600 text-white rounded-xl hover:from-pink-600 hover:to-pink-700 transition-all duration-300 font-medium shadow-lg shadow-pink-500/25 hover:shadow-xl hover:shadow-pink-500/40 hover:-translate-y-0.5">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
        </svg>
        К альбомам
      </NuxtLink>
    </div>

    <template v-else>
      <!-- Заголовок -->
      <div class="flex items-center gap-3 mb-6">
        <div class="p-2 rounded-xl bg-amber-100 dark:bg-amber-900/30">
          <svg class="w-6 h-6 text-amber-600 dark:text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
          </svg>
        </div>
        <div>
          <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200">Редактировать альбом</h1>
          <p class="text-sm text-gray-500 dark:text-gray-400">Измените информацию об альбоме</p>
        </div>
      </div>

      <div v-if="loading" class="text-center py-10">
        <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
        </svg>
        <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
      </div>

      <div v-else-if="errorMessage" class="text-center py-10 text-red-500">
        <svg class="w-16 h-16 mx-auto text-red-400 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
        </svg>
        {{ errorMessage }}
      </div>

      <form v-else @submit.prevent="updateAlbum" enctype="multipart/form-data" class="space-y-4">
        <!-- Название альбома -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
            Название альбома
            <span class="text-red-500">*</span>
          </label>
          <input 
            v-model="form.title"
            type="text"
            placeholder="Введите название альбома"
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            required
          />
        </div>

        <!-- Описание -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
            Описание
          </label>
          <textarea 
            v-model="form.description"
            placeholder="Расскажите о событии..."
            rows="4"
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          ></textarea>
        </div>

        <!-- Дата события -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
            <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            Дата события
            <span class="text-red-500">*</span>
          </label>
          <input 
            v-model="form.date"
            type="date"
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            required
          />
        </div>

        <!-- Обложка альбома -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
            <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            Обложка альбома
          </label>

          <div v-if="form.cover_image_url && !coverRemoved && !coverPreview" class="mb-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
            <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Текущая обложка:</p>
            <div class="flex items-center gap-3">
              <img 
                :src="form.cover_image_url" 
                alt="Текущая обложка" 
                class="w-20 h-20 rounded-lg object-cover border border-gray-200 dark:border-gray-600"
              />
              <button 
                @click="removeCover"
                type="button"
                class="px-3 py-1.5 text-sm text-red-500 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
              >
                Удалить
              </button>
            </div>
          </div>

          <div class="flex flex-col gap-2">
            <input 
              type="file" 
              accept="image/*"
              @change="onCoverSelected"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 dark:file:bg-blue-900/30 dark:file:text-blue-400"
            />
            <div class="flex items-center gap-2">
              <span class="text-gray-400 dark:text-gray-500 text-sm">или</span>
              <input 
                v-model="coverUrl"
                type="url"
                placeholder="https://example.com/cover.jpg"
                class="flex-1 border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
                @input="onCoverUrlInput"
              />
            </div>
          </div>
          <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Рекомендуемый размер: 800x800px. Максимум 5MB.</p>
        </div>

        <div v-if="coverPreview" class="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
          <div class="relative flex-shrink-0">
            <img 
              :src="coverPreview" 
              alt="Превью обложки" 
              class="w-20 h-20 rounded-lg object-cover border border-gray-200 dark:border-gray-600"
            />
            <button 
              @click="removeNewCover"
              type="button"
              class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center hover:bg-red-600 transition shadow-lg hover:scale-110"
              title="Удалить обложку"
            >
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
            </button>
          </div>
          <div class="flex-1 min-w-0">
            <p class="text-sm font-medium text-gray-700 dark:text-gray-300 truncate">
              {{ coverFile ? coverFile.name : 'Обложка по ссылке' }}
            </p>
            <p class="text-xs text-gray-400 dark:text-gray-500">
              {{ coverFile ? (coverFile.size / 1024).toFixed(0) + ' KB' : 'Загружено по URL' }}
            </p>
          </div>
          <button 
            @click="removeNewCover"
            type="button"
            class="px-3 py-1.5 text-sm text-red-500 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
          >
            Удалить
          </button>
        </div>

        <!-- Существующие фотографии -->
        <div v-if="existingPhotos.length > 0">
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
            <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            Текущие фотографии ({{ existingPhotos.length }})
          </label>
          <div class="grid grid-cols-4 sm:grid-cols-5 md:grid-cols-6 gap-2">
            <div 
              v-for="photo in existingPhotos" 
              :key="photo.id"
              class="relative group"
            >
              <img 
                :src="photo.image_url" 
                :alt="photo.caption || 'Фото'"
                class="w-full aspect-square rounded-lg object-cover border border-gray-200 dark:border-gray-600"
              />
              <button 
                @click="deleteExistingPhoto(photo.id)"
                type="button"
                class="absolute -top-1.5 -right-1.5 bg-red-500 text-white rounded-full w-5 h-5 flex items-center justify-center hover:bg-red-600 transition opacity-0 group-hover:opacity-100 shadow-lg"
              >
                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Добавление новых фотографий -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
            <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            Добавить фотографии
          </label>
          <input 
            type="file" 
            accept="image/*"
            multiple
            @change="onPhotosSelected"
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 dark:file:bg-blue-900/30 dark:file:text-blue-400"
          />
          <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Выберите несколько фотографий. Максимум 10MB на файл.</p>
        </div>

        <div v-if="newPhotoPreviews.length > 0" class="mt-3">
          <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Новые фотографии ({{ newPhotoPreviews.length }}):</p>
          <div class="grid grid-cols-4 sm:grid-cols-5 md:grid-cols-6 gap-2">
            <div 
              v-for="(item, index) in newPhotoPreviews" 
              :key="index"
              class="relative group"
            >
              <img 
                :src="item.preview" 
                :alt="item.file.name"
                class="w-full aspect-square rounded-lg object-cover border border-gray-200 dark:border-gray-600"
              />
              <button 
                @click="removeNewPhoto(index)"
                type="button"
                class="absolute -top-1.5 -right-1.5 bg-red-500 text-white rounded-full w-5 h-5 flex items-center justify-center hover:bg-red-600 transition opacity-0 group-hover:opacity-100 shadow-lg"
              >
                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                </svg>
              </button>
              <div class="absolute bottom-0 left-0 right-0 bg-black/60 text-white text-[10px] p-0.5 truncate text-center rounded-b-lg">
                {{ item.file.name.length > 15 ? item.file.name.substring(0, 15) + '…' : item.file.name }}
              </div>
            </div>
          </div>
        </div>

        <!-- Опубликовать -->
        <div class="flex items-center gap-2 py-2">
          <input 
            v-model="form.is_published"
            type="checkbox"
            id="is_published"
            class="w-4 h-4 text-blue-500 rounded focus:ring-2 focus:ring-blue-500 cursor-pointer"
          />
          <label for="is_published" class="text-gray-700 dark:text-gray-300 text-sm cursor-pointer select-none">
            Опубликован
          </label>
        </div>

        <!-- Кнопки -->
        <div class="flex flex-wrap gap-3 pt-4 border-t border-gray-100 dark:border-gray-700">
          <button 
            type="submit" 
            :disabled="submitting"
            class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-pink-500 to-pink-600 text-white rounded-xl hover:from-pink-600 hover:to-pink-700 transition-all duration-300 font-medium shadow-lg shadow-pink-500/25 hover:shadow-xl hover:shadow-pink-500/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/>
            </svg>
            {{ submitting ? 'Сохранение...' : 'Сохранить изменения' }}
          </button>

          <NuxtLink :to="`/gallery/${albumId}`">
            <button type="button" class="inline-flex items-center gap-2 px-6 py-3 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 font-medium hover:-translate-y-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
              Отмена
            </button>
          </NuxtLink>

          <!-- ✅ Кнопка "Удалить альбом" -->
          <button 
            type="button"
            @click="deleteAlbum"
            class="inline-flex items-center gap-2 px-6 py-3 bg-red-500 text-white rounded-xl hover:bg-red-600 transition-all duration-300 font-medium shadow-lg shadow-red-500/25 hover:shadow-xl hover:shadow-red-500/40 hover:-translate-y-0.5"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
            </svg>
            Удалить альбом
          </button>
        </div>

        <p v-if="submitError" class="text-red-500 text-sm flex items-center gap-1.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
          </svg>
          {{ submitError }}
        </p>
      </form>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const authStore = useAuthStore()
const { apiFetch } = useApi()
const router = useRouter()

const albumId = computed(() => {
  const id = route.params.id
  if (typeof id === 'string' && id.includes('edit-')) {
    return id.replace('edit-', '')
  }
  return id
})

const loading = ref(true)
const submitting = ref(false)
const errorMessage = ref('')
const submitError = ref('')
const coverRemoved = ref(false)

const form = ref({
  title: '',
  description: '',
  date: '',
  cover_image_url: '',
  is_published: false
})

const existingPhotos = ref([])
const coverFile = ref(null)
const coverUrl = ref('')
const coverPreview = ref('')
const newPhotoPreviews = ref([])

// Валидация URL
const isValidUrl = (string) => {
  try {
    const url = new URL(string)
    return url.protocol === 'http:' || url.protocol === 'https:'
  } catch (_) {
    return false
  }
}

const onCoverUrlInput = () => {
  const url = coverUrl.value.trim()
  if (url && isValidUrl(url)) {
    coverPreview.value = url
    coverFile.value = null
    coverRemoved.value = false
  } else if (!url) {
    if (!coverFile.value) {
      coverPreview.value = ''
    }
  }
}

const onCoverSelected = (event) => {
  const file = event.target.files[0]
  if (file) {
    coverFile.value = file
    coverPreview.value = URL.createObjectURL(file)
    coverUrl.value = ''
    coverRemoved.value = false
  }
}

const removeCover = () => {
  coverRemoved.value = true
  form.value.cover_image_url = ''
  coverFile.value = null
  coverPreview.value = ''
  coverUrl.value = ''
}

const removeNewCover = () => {
  coverFile.value = null
  coverPreview.value = ''
  coverUrl.value = ''
}

const onPhotosSelected = (event) => {
  const files = event.target.files
  if (files && files.length > 0) {
    for (const file of files) {
      if (file.size > 10 * 1024 * 1024) {
        alert(`Файл "${file.name}" слишком большой (макс 10MB)`)
        continue
      }
      const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
      if (!allowedTypes.includes(file.type)) {
        alert(`Файл "${file.name}" имеет неподдерживаемый формат`)
        continue
      }
      const preview = URL.createObjectURL(file)
      newPhotoPreviews.value.push({
        file: file,
        preview: preview
      })
    }
  }
  event.target.value = ''
}

const removeNewPhoto = (index) => {
  URL.revokeObjectURL(newPhotoPreviews.value[index].preview)
  newPhotoPreviews.value.splice(index, 1)
}

const deleteExistingPhoto = async (photoId) => {
  if (!confirm('Удалить эту фотографию?')) return

  try {
    const res = await apiFetch(`${API_URL}/albums/${albumId.value}/photos/${photoId}/`, {
      method: 'DELETE',
    })

    if (res.ok) {
      existingPhotos.value = existingPhotos.value.filter(p => p.id !== photoId)
    } else {
      alert('Ошибка при удалении фотографии')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  }
}

onBeforeUnmount(() => {
  for (const item of newPhotoPreviews.value) {
    URL.revokeObjectURL(item.preview)
  }
})

// Загрузка данных альбома
onMounted(async () => {
  try {
    const res = await apiFetch(`${API_URL}/albums/${albumId.value}/`, {
    })

    if (res.ok) {
      const data = await res.json()
      form.value = {
        title: data.title || '',
        description: data.description || '',
        date: data.date || '',
        cover_image_url: data.cover_image_url || '',
        is_published: data.is_published || false
      }
      existingPhotos.value = data.photos || []
    } else {
      errorMessage.value = 'Альбом не найден'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    errorMessage.value = 'Ошибка подключения к серверу'
  } finally {
    loading.value = false
  }
})

// Обновление альбома
const updateAlbum = async () => {
  if (!form.value.title) {
    submitError.value = 'Заполните название альбома'
    return
  }

  if (!form.value.date) {
    submitError.value = 'Укажите дату события'
    return
  }

  submitting.value = true
  submitError.value = ''

  try {
    const formData = new FormData()
    formData.append('title', form.value.title)
    formData.append('description', form.value.description || '')
    formData.append('date', form.value.date)
    formData.append('is_published', form.value.is_published ? 'true' : 'false')

    if (coverRemoved.value) {
      formData.append('cover_image', '')
    } else if (coverFile.value) {
      formData.append('cover_image', coverFile.value)
    } else if (coverUrl.value && isValidUrl(coverUrl.value)) {
      formData.append('cover_image_url', coverUrl.value)
    } else if (form.value.cover_image_url) {
      formData.append('cover_image_url', form.value.cover_image_url)
    }

    const res = await apiFetch(`${API_URL}/albums/${albumId.value}/`, {
      method: 'PUT',
      body: formData
    })

    if (!res.ok) {
      const data = await res.json()
      submitError.value = data.detail || 'Ошибка обновления'
      submitting.value = false
      return
    }

    const album = await res.json()

    if (newPhotoPreviews.value.length > 0) {
      const uploadFormData = new FormData()
      for (const item of newPhotoPreviews.value) {
        uploadFormData.append('photos', item.file)
      }

      await apiFetch(`${API_URL}/albums/${albumId.value}/upload-photos/`, {
        method: 'POST',
        body: uploadFormData
      })
    }

    router.push(`/gallery/${albumId.value}`)

  } catch (e) {
    console.error('Ошибка:', e)
    submitError.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}

// ✅ Удаление альбома
const deleteAlbum = async () => {
  if (!confirm(`Вы уверены, что хотите удалить альбом "${form.value.title}"?`)) return

  try {
    const res = await apiFetch(`${API_URL}/albums/${albumId.value}/`, {
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
</script>