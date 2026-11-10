<!-- frontend/pages/posts/create.vue -->
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 transition-colors duration-200">
    <div v-if="!authStore.isAuthor && !authStore.isEditor" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">
        <svg class="w-24 h-24 mx-auto text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
        </svg>
      </div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только авторы и главные редакторы могут создавать посты.</p>
      <NuxtLink to="/" class="mt-4 inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1h-2z"/>
        </svg>
        На главную
      </NuxtLink>
    </div>

    <template v-else>
      <!-- Заголовок -->
      <div class="flex items-center gap-3 mb-6">
        <div class="p-2 rounded-xl bg-green-100 dark:bg-green-900/30">
          <svg class="w-6 h-6 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
          </svg>
        </div>
        <div>
          <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200">Новый пост</h1>
          <p class="text-sm text-gray-500 dark:text-gray-400">Создайте новую публикацию</p>
        </div>
      </div>
      
      <form @submit.prevent="createPost" enctype="multipart/form-data" class="space-y-4">
        <!-- Заголовок -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
            Заголовок
            <span class="text-red-500">*</span>
          </label>
          <input 
            v-model="title"
            type="text"
            placeholder="Введите заголовок поста"
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            required
          />
        </div>
        
        <!-- Краткое описание -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
            Краткое описание
          </label>
          <input 
            v-model="excerpt"
            type="text"
            placeholder="Короткое описание поста..."
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          />
        </div>
        
        <!-- Содержание -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
            Содержание
            <span class="text-red-500">*</span>
          </label>
          <textarea 
            v-model="content"
            placeholder="Текст поста..."
            rows="10"
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            required
          ></textarea>
        </div>
        
        <!-- Изображение -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
            <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            Изображение
          </label>
          <div class="flex flex-col gap-2">
            <input 
              type="file" 
              accept="image/*"
              @change="onImageSelected"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 dark:file:bg-blue-900/30 dark:file:text-blue-400"
            />
            <div class="flex items-center gap-2">
              <span class="text-gray-400 dark:text-gray-500 text-sm">или</span>
              <input 
                v-model="imageUrl"
                type="url"
                placeholder="https://example.com/image.jpg"
                class="flex-1 border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
                @input="onUrlInput"
              />
            </div>
          </div>
          <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Рекомендуемый размер: 1920x1080px. Максимум 5MB.</p>
        </div>
        
        <!-- Миниатюра изображения -->
        <div v-if="imagePreview" class="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
          <div class="relative flex-shrink-0">
            <img 
              :src="imagePreview" 
              alt="Превью изображения" 
              class="w-20 h-20 rounded-lg object-cover border border-gray-200 dark:border-gray-600"
            />
            <button 
              @click="removeImage"
              type="button"
              class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center hover:bg-red-600 transition shadow-lg hover:scale-110"
              title="Удалить изображение"
            >
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
            </button>
          </div>
          <div class="flex-1 min-w-0">
            <p class="text-sm font-medium text-gray-700 dark:text-gray-300 truncate">
              {{ imageFile ? imageFile.name : 'Изображение по ссылке' }}
            </p>
            <p class="text-xs text-gray-400 dark:text-gray-500">
              {{ imageFile ? (imageFile.size / 1024).toFixed(0) + ' KB' : 'Загружено по URL' }}
            </p>
          </div>
          <button 
            @click="removeImage"
            type="button"
            class="px-3 py-1.5 text-sm text-red-500 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
          >
            Удалить
          </button>
        </div>
        
        <!-- Статус публикации -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Статус публикации</label>
          <div class="flex gap-6">
            <label class="flex items-center gap-2 cursor-pointer">
              <input 
                type="radio" 
                :value="true" 
                v-model="is_published"
                class="w-4 h-4 text-blue-500"
              />
              <span class="text-gray-700 dark:text-gray-300">Опубликовать</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input 
                type="radio" 
                :value="false" 
                v-model="is_published"
                class="w-4 h-4 text-gray-400"
              />
              <span class="text-gray-700 dark:text-gray-300">Сохранить как черновик</span>
            </label>
          </div>
        </div>
        
        <!-- Кнопки -->
        <div class="flex flex-wrap gap-3 pt-4 border-t border-gray-100 dark:border-gray-700">
          <button 
            type="submit" 
            :disabled="submitting"
            class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
            </svg>
            {{ submitting ? 'Создание...' : is_published ? 'Опубликовать' : 'Сохранить черновик' }}
          </button>
          
          <NuxtLink to="/">
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
const { apiFetch } = useApi()
const router = useRouter()

const submitting = ref(false)
const error = ref('')

const title = ref('')
const excerpt = ref('')
const content = ref('')
const imageFile = ref(null)
const imageUrl = ref('')
const imagePreview = ref('')
const is_published = ref(true)

// Валидация URL
const isValidUrl = (string) => {
  try {
    const url = new URL(string)
    return url.protocol === 'http:' || url.protocol === 'https:'
  } catch (_) {
    return false
  }
}

// Обработка ввода URL
const onUrlInput = () => {
  const url = imageUrl.value.trim()
  if (url && isValidUrl(url)) {
    imagePreview.value = url
    imageFile.value = null
  } else if (!url) {
    if (!imageFile.value) {
      imagePreview.value = ''
    }
  }
}

const onImageSelected = (event) => {
  const file = event.target.files[0]
  if (file) {
    imageFile.value = file
    imagePreview.value = URL.createObjectURL(file)
    imageUrl.value = ''
  }
}

const removeImage = () => {
  imageFile.value = null
  imageUrl.value = ''
  imagePreview.value = ''
}

const createPost = async () => {
  if (!title.value || !content.value) {
    error.value = 'Заполните заголовок и содержание'
    return
  }
  
  submitting.value = true
  error.value = ''
  
  try {
    let finalImageUrl = null
    
    if (imageFile.value) {
      const formData = new FormData()
      formData.append('image', imageFile.value)
      
      const uploadRes = await apiFetch(`${API_URL}/posts/upload-image/`, {
        method: 'POST',
        body: formData
      })
      
      if (uploadRes.ok) {
        const data = await uploadRes.json()
        finalImageUrl = data.image_url
      } else {
        const err = await uploadRes.json()
        error.value = err.detail || 'Ошибка загрузки изображения'
        submitting.value = false
        return
      }
    } else if (imageUrl.value && isValidUrl(imageUrl.value)) {
      finalImageUrl = imageUrl.value
    }
    
    const res = await apiFetch(`${API_URL}/posts/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        title: title.value,
        excerpt: excerpt.value,
        content: content.value,
        image_url: finalImageUrl,
        is_published: is_published.value
      })
    })
    
    if (res.ok) {
      const post = await res.json()
      router.push(`/posts/${post.id}`)
    } else {
      const data = await res.json()
      error.value = data.detail || 'Ошибка создания поста'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}
</script>