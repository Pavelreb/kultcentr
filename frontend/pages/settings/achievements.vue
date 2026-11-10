<!-- frontend/pages/settings/achievements.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4 pb-16">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-amber-500 dark:text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/>
        </svg>
        Достижения
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
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут управлять достижениями.</p>
    </div>

    <template v-else>
      <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow mb-6">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">Список достижений ({{ achievements.length }})</h2>
          <button
            v-if="!formVisible"
            @click="openCreateForm"
            class="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-amber-500 to-amber-600 text-white rounded-xl hover:from-amber-600 hover:to-amber-700 transition-all duration-300 text-sm font-medium"
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

        <p v-else-if="achievements.length === 0" class="text-gray-500 dark:text-gray-400 text-sm py-4">
          Достижений пока нет. Нажмите «Добавить», чтобы создать первое.
        </p>

        <div v-else class="space-y-2">
          <div
            v-for="item in achievements"
            :key="item.id"
            class="flex items-center gap-3 p-3 rounded-xl border border-gray-100 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700/40 transition"
          >
            <img
              v-if="item.display_image"
              :src="item.display_image"
              :alt="item.title"
              class="w-14 h-11 rounded-lg object-cover border border-gray-200 dark:border-gray-600 flex-shrink-0"
            />
            <div v-else class="w-14 h-11 rounded-lg bg-gray-200 dark:bg-gray-600 flex items-center justify-center text-gray-400 flex-shrink-0">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/>
              </svg>
            </div>
            <div class="flex-1 min-w-0">
              <p class="font-medium text-gray-800 dark:text-gray-200 truncate">
                {{ item.title }}
                <span v-if="!item.is_published" class="ml-2 text-xs text-amber-600 dark:text-amber-400">(скрыто)</span>
              </p>
              <p class="text-sm text-gray-500 dark:text-gray-400 truncate">{{ item.date ? formatDate(item.date) : 'Без даты' }}</p>
            </div>
            <NuxtLink
              :to="`/about/achievements/${item.id}`"
              class="px-3 py-1.5 text-sm text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition"
            >
              Открыть
            </NuxtLink>
            <button
              @click="openEditForm(item)"
              class="px-3 py-1.5 text-sm text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/20 rounded-lg transition"
            >
              Изменить
            </button>
            <button
              @click="removeAchievement(item)"
              class="px-3 py-1.5 text-sm text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
            >
              Удалить
            </button>
          </div>
        </div>
      </div>

      <div v-if="formVisible" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 mb-4">
          {{ editingId ? 'Редактировать достижение' : 'Новое достижение' }}
        </h2>

        <form @submit.prevent="submitForm" enctype="multipart/form-data" class="space-y-4">
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Название награды <span class="text-red-500">*</span></label>
            <input v-model="form.title" type="text" required placeholder="Гран-при фестиваля «…»"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-amber-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
          </div>

          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Краткое описание <span class="text-red-500">*</span></label>
            <textarea v-model="form.excerpt" rows="2" required placeholder="Пара предложений для карточки"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-amber-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"></textarea>
          </div>

          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Полное описание <span class="text-red-500">*</span></label>
            <textarea v-model="form.content" rows="6" required placeholder="Подробно о награде: кто получил, за что, где"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-amber-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"></textarea>
          </div>

          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Дата награждения</label>
            <input v-model="form.date" type="date"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-amber-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
          </div>

          <ImageField
            label="Изображение"
            hint="Рекомендуется 16:9, до 5MB."
            :current-url="form.display_image"
            v-model:file="imageFile"
            v-model:url="form.image_url"
            @remove="imageRemoved = true"
          />

          <label class="flex items-center gap-2 cursor-pointer">
            <input v-model="form.is_published" type="checkbox" class="w-4 h-4 text-amber-500 rounded focus:ring-2 focus:ring-amber-500 cursor-pointer" />
            <span class="text-gray-700 dark:text-gray-300 text-sm">Опубликовано (видно на сайте)</span>
          </label>

          <div class="flex flex-wrap gap-3 pt-4 border-t border-gray-100 dark:border-gray-700">
            <button type="submit" :disabled="submitting"
              class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-amber-500 to-amber-600 text-white rounded-xl hover:from-amber-600 hover:to-amber-700 transition-all duration-300 font-medium shadow-lg shadow-amber-500/25 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed">
              {{ submitting ? 'Сохранение...' : (editingId ? 'Сохранить изменения' : 'Добавить') }}
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
  title: 'Настройки: достижения'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()

const achievements = ref([])
const loading = ref(true)
const submitting = ref(false)
const error = ref('')
const success = ref('')

const formVisible = ref(false)
const editingId = ref(null)
const imageFile = ref(null)
const imageRemoved = ref(false)

const emptyForm = () => ({
  title: '',
  excerpt: '',
  content: '',
  date: '',
  image_url: '',
  display_image: '',
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

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })
}

const loadAchievements = async () => {
  loading.value = true
  try {
    const res = await apiFetch(`${API_URL}/about/achievements/`)
    if (res.ok) achievements.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки:', e)
  } finally {
    loading.value = false
  }
}

const openCreateForm = () => {
  editingId.value = null
  form.value = emptyForm()
  imageFile.value = null
  imageRemoved.value = false
  error.value = ''
  formVisible.value = true
}

const openEditForm = (item) => {
  editingId.value = item.id
  form.value = {
    title: item.title || '',
    excerpt: item.excerpt || '',
    content: item.content || '',
    date: item.date || '',
    image_url: item.image_url || '',
    display_image: item.display_image || '',
    is_published: item.is_published !== undefined ? item.is_published : true
  }
  imageFile.value = null
  imageRemoved.value = false
  error.value = ''
  formVisible.value = true
}

const closeForm = () => {
  formVisible.value = false
  editingId.value = null
  error.value = ''
}

const submitForm = async () => {
  submitting.value = true
  error.value = ''

  try {
    const formData = new FormData()
    formData.append('title', form.value.title)
    formData.append('excerpt', form.value.excerpt)
    formData.append('content', form.value.content)
    if (form.value.date) formData.append('date', form.value.date)
    else formData.append('date', '')
    formData.append('is_published', form.value.is_published ? 'true' : 'false')

    if (imageRemoved.value) {
      formData.append('image_url', '')
    } else if (imageFile.value) {
      formData.append('image', imageFile.value)
    } else if (form.value.image_url && isValidUrl(form.value.image_url)) {
      formData.append('image_url', form.value.image_url)
    }

    const url = editingId.value ? `${API_URL}/about/achievements/${editingId.value}/` : `${API_URL}/about/achievements/`
    const res = await apiFetch(url, { method: editingId.value ? 'PUT' : 'POST', body: formData })

    if (res.ok) {
      success.value = editingId.value ? 'Достижение обновлено!' : 'Достижение добавлено!'
      setTimeout(() => { success.value = '' }, 3000)
      closeForm()
      await loadAchievements()
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

const removeAchievement = async (item) => {
  if (!confirm(`Удалить «${item.title}»?`)) return
  try {
    const res = await apiFetch(`${API_URL}/about/achievements/${item.id}/`, { method: 'DELETE' })
    if (res.ok || res.status === 204) {
      success.value = 'Достижение удалено.'
      setTimeout(() => { success.value = '' }, 3000)
      await loadAchievements()
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
  if (authStore.isEditor) await loadAchievements()
})
</script>
