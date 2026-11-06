<!-- frontend/pages/gallery/create.vue -->
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 transition-colors duration-200">
    <div v-if="!authStore.isEditor" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">
        <svg class="w-24 h-24 mx-auto text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
        </svg>
      </div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только редакторы могут создавать альбомы.</p>
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
        <div class="p-2 rounded-xl bg-pink-100 dark:bg-pink-900/30">
          <svg class="w-6 h-6 text-pink-600 dark:text-pink-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
        </div>
        <div>
          <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200">Новый альбом</h1>
          <p class="text-sm text-gray-500 dark:text-gray-400">Создайте новый фотоальбом</p>
        </div>
      </div>
      
      <form @submit.prevent="createAlbum" enctype="multipart/form-data" class="space-y-4">
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
        
        <!-- Миниатюра обложки -->
        <div v-if="coverPreview" class="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
          <div class="relative flex-shrink-0">
            <img 
              :src="coverPreview" 
              alt="Превью обложки" 
              class="w-20 h-20 rounded-lg object-cover border border-gray-200 dark:border-gray-600"
            />
            <button 
              @click="removeCover"
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
            @click="removeCover"
            type="button"
            class="px-3 py-1.5 text-sm text-red-500 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
          >
            Удалить
          </button>
        </div>
        
        <!-- Фотографии -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
            <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            Фотографии
          </label>
          <input 
            type="file" 
            accept="image/*"
            multiple
            @change="onPhotosSelected"
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 dark:file:bg-blue-900/30 dark:file:text-blue-400"
          />
          <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Выберите несколько фотографий. Максимум 10MB на файл.</p>
          
          <!-- Список выбранных фото с превью -->
          <div v-if="photoPreviews.length > 0" class="mt-3">
            <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Выбрано {{ photoPreviews.length }} фотографий:</p>
            <div class="grid grid-cols-4 sm:grid-cols-5 md:grid-cols-6 gap-2">
              <div 
                v-for="(item, index) in photoPreviews" 
                :key="index"
                class="relative group"
              >
                <img 
                  :src="item.preview" 
                  :alt="item.file.name"
                  class="w-full aspect-square rounded-lg object-cover border border-gray-200 dark:border-gray-600"
                />
                <button 
                  @click="removePhoto(index)"
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
            Опубликовать сразу
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
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
            </svg>
            {{ submitting ? 'Создание...' : 'Создать альбом' }}
          </button>
          
          <NuxtLink to="/gallery">
            <button type="button" class="inline-flex items-center gap-2 px-6 py-3 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 font-medium hover:-translate-y-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
              Отмена
            </button>
          </NuxtLink>
        </div>
        
        <p v-if="error" class="text-red-500 text-sm flex items-center gap-1.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
          </svg>
          {{ error }}
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

const authStore = useAuthStore()
const router = useRouter()

const submitting = ref(false)
const error = ref('')

const form = ref({
  title: '',
  description: '',
  date: new Date().toISOString().split('T')[0],
  is_published: true
})

const coverFile = ref(null)
const coverUrl = ref('')
const coverPreview = ref('')
const photoPreviews = ref([]) // [{ file, preview }]

// Валидация URL
const isValidUrl = (string) => {
  try {
    const url = new URL(string)
    return url.protocol === 'http:' || url.protocol === 'https:'
  } catch (_) {
    return false
  }
}

// Обработка ввода URL для обложки
const onCoverUrlInput = () => {
  const url = coverUrl.value.trim()
  if (url && isValidUrl(url)) {
    coverPreview.value = url
    coverFile.value = null
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
  }
}

const removeCover = () => {
  coverFile.value = null
  coverUrl.value = ''
  coverPreview.value = ''
}

// Обработка выбора фотографий
const onPhotosSelected = (event) => {
  const files = event.target.files
  if (files && files.length > 0) {
    for (const file of files) {
      // Проверка размера
      if (file.size > 10 * 1024 * 1024) {
        alert(`Файл "${file.name}" слишком большой (макс 10MB)`)
        continue
      }
      // Проверка типа
      const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
      if (!allowedTypes.includes(file.type)) {
        alert(`Файл "${file.name}" имеет неподдерживаемый формат`)
        continue
      }
      
      // Создаём превью
      const preview = URL.createObjectURL(file)
      photoPreviews.value.push({
        file: file,
        preview: preview
      })
    }
  }
  event.target.value = ''
}

const removePhoto = (index) => {
  // Освобождаем URL
  URL.revokeObjectURL(photoPreviews.value[index].preview)
  photoPreviews.value.splice(index, 1)
}

// Очистка превью при размонтировании
onBeforeUnmount(() => {
  for (const item of photoPreviews.value) {
    URL.revokeObjectURL(item.preview)
  }
})

const createAlbum = async () => {
  if (!form.value.title) {
    error.value = 'Заполните название альбома'
    return
  }
  
  if (!form.value.date) {
    error.value = 'Укажите дату события'
    return
  }
  
  submitting.value = true
  error.value = ''
  
  try {
    const formData = new FormData()
    formData.append('title', form.value.title)
    formData.append('description', form.value.description || '')
    formData.append('date', form.value.date)
    formData.append('is_published', form.value.is_published ? 'true' : 'false')
    
    if (coverFile.value) {
      formData.append('cover_image', coverFile.value)
    } else if (coverUrl.value && isValidUrl(coverUrl.value)) {
      formData.append('cover_image_url', coverUrl.value)
    }
    
    const res = await fetch(`${API_URL}/albums/`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: formData
    })
    
    if (!res.ok) {
      const data = await res.json()
      error.value = data.detail || JSON.stringify(data)
      submitting.value = false
      return
    }
    
    const album = await res.json()
    
    // Загрузка фотографий
    if (photoPreviews.value.length > 0) {
      const uploadFormData = new FormData()
      for (const item of photoPreviews.value) {
        uploadFormData.append('photos', item.file)
      }
      
      const uploadRes = await fetch(`${API_URL}/albums/${album.id}/upload-photos/`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${authStore.accessToken}`
        },
        body: uploadFormData
      })
      
      if (!uploadRes.ok) {
        console.warn('Фотографии загружены не полностью')
      }
    }
    
    router.push(`/gallery/${album.id}`)
    
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}
</script>