<!-- frontend/pages/settings/clubs.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4 pb-16">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-teal-500 dark:text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
        </svg>
        Клубные формирования
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
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут управлять клубными формированиями.</p>
    </div>

    <template v-else>
      <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow mb-6">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">Список формирований ({{ clubs.length }})</h2>
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

        <p v-else-if="clubs.length === 0" class="text-gray-500 dark:text-gray-400 text-sm py-4">
          Клубных формирований пока нет. Нажмите «Добавить», чтобы создать первое.
        </p>

        <div v-else class="space-y-2">
          <div
            v-for="club in clubs"
            :key="club.id"
            class="flex items-center gap-3 p-3 rounded-xl border border-gray-100 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700/40 transition"
          >
            <img
              v-if="club.display_image"
              :src="club.display_image"
              :alt="club.title"
              class="w-14 h-11 rounded-lg object-cover border border-gray-200 dark:border-gray-600 flex-shrink-0"
            />
            <div v-else class="w-14 h-11 rounded-lg bg-gray-200 dark:bg-gray-600 flex items-center justify-center text-gray-400 flex-shrink-0">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
            </div>
            <div class="flex-1 min-w-0">
              <p class="font-medium text-gray-800 dark:text-gray-200 truncate">
                {{ club.title }}
                <span v-if="!club.is_published" class="ml-2 text-xs text-amber-600 dark:text-amber-400">(скрыто)</span>
              </p>
              <p class="text-sm text-gray-500 dark:text-gray-400 truncate">{{ club.leader_name || club.schedule || '—' }}</p>
            </div>
            <NuxtLink
              :to="`/about/clubs/${club.id}`"
              class="px-3 py-1.5 text-sm text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition"
            >
              Открыть
            </NuxtLink>
            <button
              @click="openEditForm(club)"
              class="px-3 py-1.5 text-sm text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/20 rounded-lg transition"
            >
              Изменить
            </button>
            <button
              @click="removeClub(club)"
              class="px-3 py-1.5 text-sm text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
            >
              Удалить
            </button>
          </div>
        </div>
      </div>

      <div v-if="formVisible" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 mb-4">
          {{ editingId ? 'Редактировать формирование' : 'Новое клубное формирование' }}
        </h2>

        <form @submit.prevent="submitForm" enctype="multipart/form-data" class="space-y-4">
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Название <span class="text-red-500">*</span></label>
            <input v-model="form.title" type="text" required placeholder="Народный коллектив «…»"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-teal-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
          </div>

          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Краткое описание <span class="text-red-500">*</span></label>
            <textarea v-model="form.excerpt" rows="2" required placeholder="Пара предложений для карточки"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-teal-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"></textarea>
          </div>

          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Полное описание <span class="text-red-500">*</span></label>
            <textarea v-model="form.content" rows="6" required placeholder="Подробно о коллективе: история, занятия, достижения"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-teal-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"></textarea>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Руководитель</label>
              <input v-model="form.leader_name" type="text" placeholder="Иванова М. П."
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-teal-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
            </div>
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Расписание</label>
              <input v-model="form.schedule" type="text" placeholder="Пн, Ср 17:00–19:00"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-teal-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
            </div>
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Возраст</label>
              <input v-model="form.age" type="text" placeholder="6+"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-teal-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
            </div>
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
            <input v-model="form.is_published" type="checkbox" class="w-4 h-4 text-teal-500 rounded focus:ring-2 focus:ring-teal-500 cursor-pointer" />
            <span class="text-gray-700 dark:text-gray-300 text-sm">Опубликовано (видно на сайте)</span>
          </label>

          <div class="flex flex-wrap gap-3 pt-4 border-t border-gray-100 dark:border-gray-700">
            <button type="submit" :disabled="submitting"
              class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-teal-500 to-teal-600 text-white rounded-xl hover:from-teal-600 hover:to-teal-700 transition-all duration-300 font-medium shadow-lg shadow-teal-500/25 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed">
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
  title: 'Настройки: клубные формирования'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()

const clubs = ref([])
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
  leader_name: '',
  schedule: '',
  age: '',
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

const loadClubs = async () => {
  loading.value = true
  try {
    const res = await apiFetch(`${API_URL}/about/clubs/`)
    if (res.ok) clubs.value = await res.json()
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

const openEditForm = (club) => {
  editingId.value = club.id
  form.value = {
    title: club.title || '',
    excerpt: club.excerpt || '',
    content: club.content || '',
    leader_name: club.leader_name || '',
    schedule: club.schedule || '',
    age: club.age || '',
    image_url: club.image_url || '',
    display_image: club.display_image || '',
    is_published: club.is_published !== undefined ? club.is_published : true
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
    formData.append('leader_name', form.value.leader_name || '')
    formData.append('schedule', form.value.schedule || '')
    formData.append('age', form.value.age || '')
    formData.append('is_published', form.value.is_published ? 'true' : 'false')

    if (imageRemoved.value) {
      formData.append('image_url', '')
    } else if (imageFile.value) {
      formData.append('image', imageFile.value)
    } else if (form.value.image_url && isValidUrl(form.value.image_url)) {
      formData.append('image_url', form.value.image_url)
    }

    const url = editingId.value ? `${API_URL}/about/clubs/${editingId.value}/` : `${API_URL}/about/clubs/`
    const res = await apiFetch(url, { method: editingId.value ? 'PUT' : 'POST', body: formData })

    if (res.ok) {
      success.value = editingId.value ? 'Формирование обновлено!' : 'Формирование добавлено!'
      setTimeout(() => { success.value = '' }, 3000)
      closeForm()
      await loadClubs()
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

const removeClub = async (club) => {
  if (!confirm(`Удалить «${club.title}»?`)) return
  try {
    const res = await apiFetch(`${API_URL}/about/clubs/${club.id}/`, { method: 'DELETE' })
    if (res.ok || res.status === 204) {
      success.value = 'Формирование удалено.'
      setTimeout(() => { success.value = '' }, 3000)
      await loadClubs()
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
  if (authStore.isEditor) await loadClubs()
})
</script>
