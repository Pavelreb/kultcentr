<!-- frontend/pages/settings/institution.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-teal-500 dark:text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
        </svg>
        Об учреждении
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
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут управлять настройками сайта.</p>
    </div>

    <template v-else>
      <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <p class="text-sm text-gray-500 dark:text-gray-400 mb-4">
          Эти данные выводятся на главной странице раздела
          <NuxtLink to="/about" class="text-teal-600 dark:text-teal-400 hover:underline">«Об учреждении»</NuxtLink>.
        </p>

        <!-- Живой предпросмотр хироу-баннера -->
        <div class="mb-6 rounded-xl overflow-hidden border border-gray-200 dark:border-gray-700">
          <p class="text-xs font-medium text-gray-400 dark:text-gray-500 uppercase tracking-wider px-3 py-2 bg-gray-50 dark:bg-gray-700/50">
            Предпросмотр баннера
          </p>
          <div class="relative overflow-hidden">
            <div
              class="absolute inset-0 bg-cover bg-center"
              :style="bgPreviewUrl ? { backgroundImage: `url(${bgPreviewUrl})` } : {}"
              :class="!bgPreviewUrl ? 'bg-gradient-to-br from-blue-600 via-indigo-600 to-purple-700' : ''"
            ></div>
            <div class="absolute inset-0 bg-black/50"></div>
            <div class="relative px-4 py-10 text-center text-white">
              <div v-if="logoPreviewUrl" class="w-16 h-16 mx-auto rounded-full bg-white/10 backdrop-blur-sm p-1 shadow-xl mb-3 overflow-hidden">
                <img :src="logoPreviewUrl" alt="Логотип" class="w-full h-full object-cover rounded-full bg-white" />
              </div>
              <div v-else class="w-16 h-16 mx-auto rounded-full bg-white/10 backdrop-blur-sm flex items-center justify-center shadow-xl mb-3">
                <svg class="w-8 h-8 text-white/80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5v-9a2 2 0 00-2-2H9a2 2 0 00-2 2v9m12 0H3"/>
                </svg>
              </div>
              <p class="text-xl md:text-2xl font-bold drop-shadow-lg">{{ form.name || 'Центр Культуры' }}</p>
              <p v-if="form.description" class="mt-2 max-w-xl mx-auto text-white/90 text-xs md:text-sm leading-relaxed whitespace-pre-wrap drop-shadow line-clamp-3">
                {{ form.description }}
              </p>
            </div>
          </div>
        </div>

        <form @submit.prevent="updateInfo" enctype="multipart/form-data" class="space-y-4">
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
              Название учреждения <span class="text-red-500">*</span>
            </label>
            <input
              v-model="form.name"
              type="text"
              placeholder="Например: Центр Культуры"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-teal-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              required
            />
          </div>

          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
              Описание учреждения <span class="text-red-500">*</span>
            </label>
            <textarea
              v-model="form.description"
              placeholder="Краткое описание деятельности учреждения"
              rows="4"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-teal-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              required
            ></textarea>
          </div>

          <!-- Логотип -->
          <ImageField
            label="Логотип"
            hint="Рекомендуется квадратное изображение, до 5MB."
            :current-url="form.logo_display"
            v-model:file="logoFile"
            v-model:url="form.logo_url"
            @remove="logoRemoved = true"
          />

          <!-- Фон баннера -->
          <ImageField
            label="Фоновое изображение баннера"
            hint="Рекомендуемый размер: 1920x600px, до 5MB."
            :current-url="form.background_display"
            v-model:file="bgFile"
            v-model:url="form.background_image_url"
            @remove="bgRemoved = true"
          />

          <div class="flex flex-wrap gap-3 pt-4 border-t border-gray-100 dark:border-gray-700">
            <button
              type="submit"
              :disabled="submitting"
              class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-teal-500 to-teal-600 text-white rounded-xl hover:from-teal-600 hover:to-teal-700 transition-all duration-300 font-medium shadow-lg shadow-teal-500/25 hover:shadow-xl hover:shadow-teal-500/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/>
              </svg>
              {{ submitting ? 'Сохранение...' : 'Сохранить' }}
            </button>
          </div>

          <p v-if="error" class="text-red-500 text-sm">{{ error }}</p>
          <p v-if="success" class="text-green-500 text-sm">{{ success }}</p>
        </form>
      </div>
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
  title: 'Настройки: об учреждении'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()

const submitting = ref(false)
const error = ref('')
const success = ref('')

const form = ref({
  name: '',
  description: '',
  logo_display: '',
  logo_url: '',
  background_display: '',
  background_image_url: ''
})

const logoFile = ref(null)
const bgFile = ref(null)
const logoRemoved = ref(false)
const bgRemoved = ref(false)

// Превью для живого предпросмотра баннера
const logoPreviewUrl = computed(() => {
  if (logoFile.value) return URL.createObjectURL(logoFile.value)
  if (form.value.logo_url && isValidUrl(form.value.logo_url)) return form.value.logo_url
  if (logoRemoved.value) return ''
  return form.value.logo_display || ''
})

const bgPreviewUrl = computed(() => {
  if (bgFile.value) return URL.createObjectURL(bgFile.value)
  if (form.value.background_image_url && isValidUrl(form.value.background_image_url)) return form.value.background_image_url
  if (bgRemoved.value) return ''
  return form.value.background_display || ''
})

const isValidUrl = (string) => {
  try {
    const url = new URL(string)
    return url.protocol === 'http:' || url.protocol === 'https:'
  } catch (_) {
    return false
  }
}

const loadInfo = async () => {
  try {
    const res = await apiFetch(`${API_URL}/about/info/`)
    if (res.ok) {
      const data = await res.json()
      form.value = {
        name: data.name || '',
        description: data.description || '',
        logo_display: data.logo_display || '',
        logo_url: data.logo_url || '',
        background_display: data.background_display || '',
        background_image_url: data.background_image_url || ''
      }
      logoRemoved.value = false
      bgRemoved.value = false
    }
  } catch (e) {
    console.error('Ошибка загрузки:', e)
  }
}

const updateInfo = async () => {
  if (!form.value.name || !form.value.description) {
    error.value = 'Заполните название и описание'
    return
  }

  submitting.value = true
  error.value = ''
  success.value = ''

  try {
    const formData = new FormData()
    formData.append('name', form.value.name)
    formData.append('description', form.value.description)

    if (logoRemoved.value) {
      formData.append('logo_url', '')
    } else if (logoFile.value) {
      formData.append('logo', logoFile.value)
    } else if (form.value.logo_url && isValidUrl(form.value.logo_url)) {
      formData.append('logo_url', form.value.logo_url)
    }

    if (bgRemoved.value) {
      formData.append('background_image_url', '')
    } else if (bgFile.value) {
      formData.append('background_image', bgFile.value)
    } else if (form.value.background_image_url && isValidUrl(form.value.background_image_url)) {
      formData.append('background_image_url', form.value.background_image_url)
    }

    const res = await apiFetch(`${API_URL}/about/info/update/`, {
      method: 'PUT',
      body: formData
    })

    if (res.ok) {
      const data = await res.json()
      form.value = {
        ...form.value,
        name: data.name,
        description: data.description,
        logo_display: data.logo_display || '',
        logo_url: data.logo_url || '',
        background_display: data.background_display || '',
        background_image_url: data.background_image_url || ''
      }
      logoFile.value = null
      bgFile.value = null
      logoRemoved.value = false
      bgRemoved.value = false
      success.value = 'Информация об учреждении сохранена!'
      setTimeout(() => { success.value = '' }, 3000)
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

onMounted(async () => {
  authStore.restoreAuth()
  await loadInfo()
})
</script>
