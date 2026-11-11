<!-- frontend/pages/posts/edit-[id].vue -->
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 transition-colors duration-200">
    <div v-if="!authStore.isAuthor && !authStore.isEditor" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">
        <svg class="w-24 h-24 mx-auto text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
        </svg>
      </div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только авторы и главные редакторы могут редактировать посты.</p>
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
        <div class="p-2 rounded-xl bg-amber-100 dark:bg-amber-900/30">
          <svg class="w-6 h-6 text-amber-600 dark:text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
          </svg>
        </div>
        <div>
          <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200">Редактировать пост</h1>
          <p class="text-sm text-gray-500 dark:text-gray-400">Измените информацию о публикации</p>
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
      
      <form v-else @submit.prevent="updatePost" enctype="multipart/form-data" class="space-y-4">
        <!-- Заголовок -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
            Заголовок
            <span class="text-red-500">*</span>
          </label>
          <input 
            v-model="form.title"
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
            v-model="form.excerpt"
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
          <RichTextEditor
            v-model="form.content"
            placeholder="Текст поста..."
            :rows="10"
            :required="true"
          />
        </div>
        
        <!-- Изображение -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
            <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            Изображение
          </label>
          
          <!-- Текущее изображение -->
          <div v-if="form.image_url && !imageRemoved && !imagePreview" class="mb-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
            <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Текущее изображение:</p>
            <div class="flex items-center gap-3">
              <img 
                :src="form.image_url" 
                alt="Текущее изображение" 
                class="w-20 h-20 rounded-lg object-cover border border-gray-200 dark:border-gray-600"
              />
              <button 
                @click="removeImage"
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
        
        <!-- Миниатюра нового изображения -->
        <div v-if="imagePreview" class="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
          <div class="relative flex-shrink-0">
            <img 
              :src="imagePreview" 
              alt="Превью изображения" 
              class="w-20 h-20 rounded-lg object-cover border border-gray-200 dark:border-gray-600"
            />
            <button 
              @click="removeNewImage"
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
            @click="removeNewImage"
            type="button"
            class="px-3 py-1.5 text-sm text-red-500 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
          >
            Удалить
          </button>
        </div>
        
        <!-- Голосование (только редакторы) -->
        <PollEditor v-if="authStore.isEditor" v-model="pollData" />
        
        <!-- Тест (только редакторы) -->
        <QuizEditor v-if="authStore.isEditor" v-model="quizData" />
        
        <!-- Предупреждение о сбросе результатов -->
        <div
          v-if="authStore.isEditor && (pollData || quizData)"
          class="flex items-start gap-3 p-4 rounded-xl border-2 border-red-300 dark:border-red-700 bg-red-50 dark:bg-red-900/20"
        >
          <svg class="w-6 h-6 text-red-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
          </svg>
          <p class="text-base font-bold text-red-600 dark:text-red-400">
            ВНИМАНИЕ: сохранение этого поста полностью сбросит результаты голосования и теста — все голоса и прохождения будут удалены!
          </p>
        </div>
        
        <!-- Статус публикации -->
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Статус публикации</label>
          <div class="flex gap-6">
            <label class="flex items-center gap-2 cursor-pointer">
              <input 
                type="radio" 
                :value="true" 
                v-model="form.is_published"
                class="w-4 h-4 text-blue-500"
              />
              <span class="text-gray-700 dark:text-gray-300">Опубликовано</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input 
                type="radio" 
                :value="false" 
                v-model="form.is_published"
                class="w-4 h-4 text-gray-400"
              />
              <span class="text-gray-700 dark:text-gray-300">Черновик</span>
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
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/>
            </svg>
            {{ submitting ? 'Сохранение...' : 'Сохранить изменения' }}
          </button>
          
          <NuxtLink :to="`/posts/${postId}`">
            <button type="button" class="inline-flex items-center gap-2 px-6 py-3 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 font-medium hover:-translate-y-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
              Отмена
            </button>
          </NuxtLink>
          
          <button 
            type="button"
            @click="deletePost"
            class="inline-flex items-center gap-2 px-6 py-3 bg-red-500 text-white rounded-xl hover:bg-red-600 transition-all duration-300 font-medium shadow-lg shadow-red-500/25 hover:shadow-xl hover:shadow-red-500/40 hover:-translate-y-0.5"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
            </svg>
            Удалить пост
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
import RichTextEditor from '~/components/common/RichTextEditor.vue'
import PollEditor from '~/components/features/posts/PollEditor.vue'
import QuizEditor from '~/components/features/posts/QuizEditor.vue'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const authStore = useAuthStore()
const { apiFetch } = useApi()
const router = useRouter()

const postId = computed(() => {
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
const imageRemoved = ref(false)

const form = ref({
  title: '',
  excerpt: '',
  content: '',
  image_url: '',
  is_published: false
})

const imageFile = ref(null)
const imageUrl = ref('')
const imagePreview = ref('')
const pollData = ref(null)
const quizData = ref(null)

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
    imageRemoved.value = false
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
    imageRemoved.value = false
  }
}

const removeImage = () => {
  imageRemoved.value = true
  form.value.image_url = ''
  imageFile.value = null
  imagePreview.value = ''
  imageUrl.value = ''
}

const removeNewImage = () => {
  imageFile.value = null
  imagePreview.value = ''
  imageUrl.value = ''
}

// Загрузка данных поста
onMounted(async () => {
  try {
    const res = await apiFetch(`${API_URL}/posts/${postId.value}/`, {
    })
    
    if (res.ok) {
      const data = await res.json()
      
      // Проверка прав
      if (data.author_name !== authStore.user?.username && !authStore.isEditor) {
        router.push(`/posts/${postId.value}`)
        return
      }
      
      form.value = {
        title: data.title || '',
        excerpt: data.excerpt || '',
        content: data.content || '',
        image_url: data.image_url || '',
        is_published: data.is_published || false
      }
      
      // Голосование: приводим варианты к строкам для редактора
      if (data.poll) {
        pollData.value = {
          question: data.poll.question || '',
          options: (data.poll.options || []).map((o) => o.text)
        }
      }
      
      // Тест: структура совпадает с редактором (id лишними не будут)
      if (data.quiz) {
        quizData.value = {
          title: data.quiz.title || '',
          description: data.quiz.description || '',
          questions: (data.quiz.questions || []).map((q) => ({
            text: q.text,
            answers: (q.answers || []).map((a) => ({
              text: a.text,
              is_correct: !!a.is_correct
            }))
          }))
        }
      }
    } else {
      errorMessage.value = 'Пост не найден'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    errorMessage.value = 'Ошибка подключения к серверу'
  } finally {
    loading.value = false
  }
})

// Обновление поста
const updatePost = async () => {
  if (!form.value.title || !form.value.content) {
    submitError.value = 'Заполните заголовок и содержание'
    return
  }
  
  submitting.value = true
  submitError.value = ''
  
  try {
    let finalImageUrl = form.value.image_url || null
    
    if (imageRemoved.value) {
      finalImageUrl = null
    } else if (imageFile.value) {
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
        submitError.value = err.detail || 'Ошибка загрузки изображения'
        submitting.value = false
        return
      }
    } else if (imageUrl.value && isValidUrl(imageUrl.value)) {
      finalImageUrl = imageUrl.value
    }
    
    const body = {
      title: form.value.title,
      excerpt: form.value.excerpt,
      content: form.value.content,
      image_url: finalImageUrl,
      is_published: form.value.is_published
    }
    // Голосование и тест отправляем только редакторы (null = удалить)
    if (authStore.isEditor) {
      body.poll = pollData.value
      body.quiz = quizData.value
    }
    
    const res = await apiFetch(`${API_URL}/posts/${postId.value}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    })
    
    if (res.ok) {
      const post = await res.json()
      router.push(`/posts/${post.id}`)
    } else {
      const data = await res.json()
      submitError.value = data.detail || data.poll || data.quiz || 'Ошибка обновления'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    submitError.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}

// Удаление поста
const deletePost = async () => {
  if (!confirm(`Вы уверены, что хотите удалить пост "${form.value.title}"?`)) return
  
  try {
    const res = await apiFetch(`${API_URL}/posts/${postId.value}/`, {
      method: 'DELETE',
    })
    
    if (res.ok) {
      router.push('/posts')
    } else {
      alert('Ошибка при удалении поста')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  }
}
</script>