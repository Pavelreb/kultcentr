<!-- frontend/pages/settings/index.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-yellow-500 dark:text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
        </svg>
        Настройки сайта
      </h1>
      <NuxtLink 
        to="/" 
        class="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 hover:-translate-y-0.5"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1h-2z"/>
        </svg>
        На главную
      </NuxtLink>
    </div>
    
    <div v-if="!authStore.isEditor" class="bg-white dark:bg-gray-800 p-8 rounded-lg shadow text-center py-20">
      <svg class="w-24 h-24 mx-auto text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
      </svg>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут управлять настройками сайта.</p>
      <NuxtLink to="/" class="mt-4 inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1h-2z"/>
        </svg>
        На главную
      </NuxtLink>
    </div>
    
    <template v-else>
      <!-- Вкладки -->
      <div class="flex gap-2 mb-6 border-b border-gray-200 dark:border-gray-700 overflow-x-auto">
        <button 
          @click="activeTab = 'banner'"
          class="inline-flex items-center gap-2 px-6 py-3 font-medium transition rounded-t-lg whitespace-nowrap"
          :class="activeTab === 'banner' 
            ? 'bg-blue-500 text-white shadow-lg shadow-blue-500/25' 
            : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
          Баннер
        </button>
        <button 
          @click="activeTab = 'contacts'"
          class="inline-flex items-center gap-2 px-6 py-3 font-medium transition rounded-t-lg whitespace-nowrap"
          :class="activeTab === 'contacts' 
            ? 'bg-blue-500 text-white shadow-lg shadow-blue-500/25' 
            : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
          </svg>
          Контакты
        </button>
        <button 
          @click="activeTab = 'gallery'"
          class="inline-flex items-center gap-2 px-6 py-3 font-medium transition rounded-t-lg whitespace-nowrap"
          :class="activeTab === 'gallery' 
            ? 'bg-blue-500 text-white shadow-lg shadow-blue-500/25' 
            : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
          Галерея
        </button>
      </div>
      
      <!-- Блок настроек баннера -->
      <div v-show="activeTab === 'banner'" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6 flex items-center gap-2">
          <svg class="w-6 h-6 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
          Настройка баннера
        </h2>
        
        <div class="mb-6 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700">
          <HeroBanner :banner="bannerPreview" />
        </div>
        
        <form @submit.prevent="updateBanner" enctype="multipart/form-data" class="space-y-4">
          <!-- Заголовок -->
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
              Заголовок
              <span class="text-red-500">*</span>
            </label>
            <input 
              v-model="bannerForm.title"
              type="text"
              placeholder="Введите заголовок баннера"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              required
            />
          </div>
          
          <!-- Подзаголовок -->
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
              Подзаголовок
              <span class="text-red-500">*</span>
            </label>
            <textarea 
              v-model="bannerForm.subtitle"
              placeholder="Введите подзаголовок баннера"
              rows="3"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              required
            ></textarea>
          </div>
          
          <!-- Фоновое изображение -->
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
              <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
              Фоновое изображение
            </label>
            
            <!-- Текущее изображение -->
            <div v-if="bannerForm.background_image_url_display && !bannerImageRemoved && !bannerImagePreview" class="mb-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
              <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Текущее изображение:</p>
              <div class="flex items-center gap-3">
                <img 
                  :src="bannerForm.background_image_url_display" 
                  alt="Фон баннера" 
                  class="w-20 h-20 rounded-lg object-cover border border-gray-200 dark:border-gray-600"
                />
                <button 
                  @click="removeBannerImage"
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
                @change="onBannerFileSelected"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 dark:file:bg-blue-900/30 dark:file:text-blue-400"
              />
              <div class="flex items-center gap-2">
                <span class="text-gray-400 dark:text-gray-500 text-sm">или</span>
                <input 
                  v-model="bannerForm.background_image_url"
                  type="url"
                  placeholder="https://example.com/banner.jpg"
                  class="flex-1 border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
                  @input="onBannerUrlInput"
                />
              </div>
            </div>
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Рекомендуемый размер: 1920x600px. Максимум 5MB.</p>
          </div>
          
          <!-- Миниатюра нового изображения -->
          <div v-if="bannerImagePreview" class="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
            <div class="relative flex-shrink-0">
              <img 
                :src="bannerImagePreview" 
                alt="Превью изображения" 
                class="w-20 h-20 rounded-lg object-cover border border-gray-200 dark:border-gray-600"
              />
              <button 
                @click="removeBannerImagePreview"
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
                {{ bannerImageFile ? bannerImageFile.name : 'Изображение по ссылке' }}
              </p>
              <p class="text-xs text-gray-400 dark:text-gray-500">
                {{ bannerImageFile ? (bannerImageFile.size / 1024).toFixed(0) + ' KB' : 'Загружено по URL' }}
              </p>
            </div>
            <button 
              @click="removeBannerImagePreview"
              type="button"
              class="px-3 py-1.5 text-sm text-red-500 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
            >
              Удалить
            </button>
          </div>
          
          <!-- Кнопка -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
                <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4-4-4m-4-4l-4-4 4-4 4 4"/>
                </svg>
                Текст кнопки
              </label>
              <input 
                v-model="bannerForm.button_text"
                type="text"
                placeholder="Смотреть афишу"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              />
            </div>
            
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
                <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 9l3 3m0 0l-3 3m3-3H8m13 0a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                Ссылка кнопки
              </label>
              <input 
                v-model="bannerForm.button_link"
                type="text"
                placeholder="/events"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              />
            </div>
          </div>
          
          <!-- Чекбоксы -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 cursor-pointer">
              <input 
                v-model="bannerForm.button_enabled"
                type="checkbox"
                class="w-4 h-4 text-blue-500 rounded focus:ring-2 focus:ring-blue-500 cursor-pointer"
              />
              <span class="text-gray-700 dark:text-gray-300 text-sm">Показывать кнопку</span>
            </label>
            
            <label class="flex items-center gap-2 cursor-pointer">
              <input 
                v-model="bannerForm.is_active"
                type="checkbox"
                class="w-4 h-4 text-blue-500 rounded focus:ring-2 focus:ring-blue-500 cursor-pointer"
              />
              <span class="text-gray-700 dark:text-gray-300 text-sm">Баннер активен (отображается на главной)</span>
            </label>
          </div>
          
          <!-- Кнопки -->
          <div class="flex flex-wrap gap-3 pt-4 border-t border-gray-100 dark:border-gray-700">
            <button 
              type="submit" 
              :disabled="bannerSubmitting"
              class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/>
              </svg>
              {{ bannerSubmitting ? 'Сохранение...' : 'Сохранить баннер' }}
            </button>
            
            <button 
              type="button"
              @click="confirmResetBanner"
              class="inline-flex items-center gap-2 px-6 py-3 bg-amber-500 text-white rounded-xl hover:bg-amber-600 transition-all duration-300 font-medium shadow-lg shadow-amber-500/25 hover:shadow-xl hover:shadow-amber-500/40 hover:-translate-y-0.5"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
              </svg>
              Сбросить
            </button>
          </div>
          
          <p v-if="bannerSubmitError" class="text-red-500 text-sm flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
            </svg>
            {{ bannerSubmitError }}
          </p>
          <p v-if="bannerSuccess" class="text-green-500 text-sm flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            {{ bannerSuccess }}
          </p>
        </form>
      </div>
      
      <!-- Блок настроек контактов (без изменений) -->
      <div v-show="activeTab === 'contacts'" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <!-- ... контакты ... -->
      </div>
      
      <!-- Блок настроек галереи (без изменений) -->
      <div v-show="activeTab === 'gallery'" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <!-- ... галерея ... -->
      </div>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import HeroBanner from '~/components/features/banner/HeroBanner.vue'

definePageMeta({
  middleware: ['auth', 'editor']
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()

// ============================================
// АКТИВНАЯ ВКЛАДКА
// ============================================
const activeTab = ref('banner')

// ============================================
// БАННЕР
// ============================================
const bannerSubmitting = ref(false)
const bannerSubmitError = ref('')
const bannerSuccess = ref('')

const bannerImageFile = ref(null)
const bannerImagePreview = ref('')
const bannerImageRemoved = ref(false)
const bannerImageChanged = ref(false)

const DEFAULT_BANNER = {
  title: '🏛️ Добро пожаловать в Центр Культуры',
  subtitle: 'Место, где искусство, традиции и творчество объединяются',
  background_image_url: '',
  background_image_url_display: '',
  button_text: 'Смотреть афишу',
  button_link: '/events',
  button_enabled: true,
  is_active: true
}

const bannerForm = ref({
  title: '',
  subtitle: '',
  background_image_url: '',
  background_image_url_display: '',
  button_text: '',
  button_link: '',
  button_enabled: true,
  is_active: true
})

const bannerOriginalForm = ref({})

const bannerPreview = computed(() => ({
  ...bannerForm.value,
  has_background: !!(bannerForm.value.background_image_url_display || bannerImagePreview.value) && !bannerImageRemoved.value,
  background_image_url_display: bannerImagePreview.value || (bannerImageRemoved.value ? '' : bannerForm.value.background_image_url_display)
}))

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
const onBannerUrlInput = () => {
  const url = bannerForm.value.background_image_url.trim()
  if (url && isValidUrl(url)) {
    bannerImagePreview.value = url
    bannerImageFile.value = null
    bannerImageRemoved.value = false
    bannerImageChanged.value = true
  } else if (!url) {
    if (!bannerImageFile.value) {
      bannerImagePreview.value = ''
    }
  }
}

const onBannerFileSelected = (event) => {
  const file = event.target.files[0]
  if (file) {
    if (file.size > 5 * 1024 * 1024) {
      alert('Файл слишком большой. Максимум 5MB.')
      return
    }
    const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
    if (!allowedTypes.includes(file.type)) {
      alert('Неподдерживаемый формат. Используйте JPEG, PNG, GIF или WEBP.')
      return
    }
    bannerImageFile.value = file
    bannerImagePreview.value = URL.createObjectURL(file)
    bannerForm.value.background_image_url = ''
    bannerImageRemoved.value = false
    bannerImageChanged.value = true
  }
}

const removeBannerImage = () => {
  bannerImageRemoved.value = true
  bannerImageChanged.value = true
  bannerForm.value.background_image_url = ''
  bannerForm.value.background_image_url_display = ''
  bannerImageFile.value = null
  bannerImagePreview.value = ''
}

const removeBannerImagePreview = () => {
  bannerImageFile.value = null
  bannerImagePreview.value = ''
  bannerForm.value.background_image_url = ''
  bannerImageChanged.value = false
}

const resetBannerForm = () => {
  bannerForm.value = { ...bannerOriginalForm.value }
  bannerImageFile.value = null
  bannerImagePreview.value = ''
  bannerImageRemoved.value = false
  bannerImageChanged.value = false
  bannerSubmitError.value = ''
  bannerSuccess.value = ''
}

const confirmResetBanner = () => {
  if (confirm('Вы уверены, что хотите сбросить настройки баннера к значениям по умолчанию?')) {
    applyDefaultBannerSettings()
  }
}

const applyDefaultBannerSettings = async () => {
  bannerSubmitting.value = true
  bannerSubmitError.value = ''
  bannerSuccess.value = ''
  
  try {
    const formData = new FormData()
    formData.append('title', DEFAULT_BANNER.title)
    formData.append('subtitle', DEFAULT_BANNER.subtitle)
    formData.append('button_text', DEFAULT_BANNER.button_text)
    formData.append('button_link', DEFAULT_BANNER.button_link)
    formData.append('button_enabled', DEFAULT_BANNER.button_enabled ? 'true' : 'false')
    formData.append('is_active', DEFAULT_BANNER.is_active ? 'true' : 'false')
    formData.append('background_image_url', '')
    
    const res = await fetch(`${API_URL}/banner/update/`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: formData
    })
    
    if (res.ok) {
      const data = await res.json()
      bannerForm.value = {
        title: data.title || DEFAULT_BANNER.title,
        subtitle: data.subtitle || DEFAULT_BANNER.subtitle,
        background_image_url: data.background_image_url || '',
        background_image_url_display: data.background_image_url_display || '',
        button_text: data.button_text || DEFAULT_BANNER.button_text,
        button_link: data.button_link || DEFAULT_BANNER.button_link,
        button_enabled: data.button_enabled !== undefined ? data.button_enabled : DEFAULT_BANNER.button_enabled,
        is_active: data.is_active !== undefined ? data.is_active : DEFAULT_BANNER.is_active
      }
      bannerOriginalForm.value = { ...bannerForm.value }
      bannerImageFile.value = null
      bannerImagePreview.value = ''
      bannerImageRemoved.value = false
      bannerImageChanged.value = false
      
      bannerSuccess.value = '✅ Настройки баннера сброшены к значениям по умолчанию!'
      
      setTimeout(() => {
        bannerSuccess.value = ''
      }, 3000)
    } else {
      const data = await res.json()
      bannerSubmitError.value = data.detail || data.message || 'Ошибка сброса настроек'
      console.error('Ошибка сервера:', data)
    }
  } catch (e) {
    console.error('Ошибка:', e)
    bannerSubmitError.value = 'Ошибка подключения к серверу'
  } finally {
    bannerSubmitting.value = false
  }
}

// ============================================
// ЗАГРУЗКА ДАННЫХ
// ============================================
const loadBanner = async () => {
  try {
    const res = await fetch(`${API_URL}/banner/`)
    if (res.ok) {
      const data = await res.json()
      bannerForm.value = {
        title: data.title || DEFAULT_BANNER.title,
        subtitle: data.subtitle || DEFAULT_BANNER.subtitle,
        background_image_url: data.background_image_url || '',
        background_image_url_display: data.background_image_url_display || '',
        button_text: data.button_text || DEFAULT_BANNER.button_text,
        button_link: data.button_link || DEFAULT_BANNER.button_link,
        button_enabled: data.button_enabled !== undefined ? data.button_enabled : DEFAULT_BANNER.button_enabled,
        is_active: data.is_active !== undefined ? data.is_active : DEFAULT_BANNER.is_active
      }
      bannerOriginalForm.value = { ...bannerForm.value }
      bannerImageRemoved.value = false
    }
  } catch (e) {
    console.error('Ошибка загрузки баннера:', e)
  }
}

// ============================================
// ОБНОВЛЕНИЕ БАННЕРА
// ============================================
const updateBanner = async () => {
  if (!bannerForm.value.title || !bannerForm.value.subtitle) {
    bannerSubmitError.value = 'Заполните заголовок и подзаголовок'
    return
  }
  
  bannerSubmitting.value = true
  bannerSubmitError.value = ''
  bannerSuccess.value = ''
  
  try {
    const formData = new FormData()
    formData.append('title', bannerForm.value.title)
    formData.append('subtitle', bannerForm.value.subtitle)
    formData.append('button_text', bannerForm.value.button_text || '')
    formData.append('button_link', bannerForm.value.button_link || '')
    formData.append('button_enabled', bannerForm.value.button_enabled ? 'true' : 'false')
    formData.append('is_active', bannerForm.value.is_active ? 'true' : 'false')
    
    if (bannerImageRemoved.value) {
      formData.append('background_image_url', '')
    } else if (bannerImageFile.value) {
      formData.append('background_image', bannerImageFile.value)
    } else if (bannerForm.value.background_image_url && isValidUrl(bannerForm.value.background_image_url)) {
      formData.append('background_image_url', bannerForm.value.background_image_url)
    } else if (bannerForm.value.background_image_url_display && !bannerImageChanged.value) {
      formData.append('background_image_url', bannerForm.value.background_image_url_display)
    }
    
    const res = await fetch(`${API_URL}/banner/update/`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: formData
    })
    
    if (res.ok) {
      const data = await res.json()
      bannerForm.value = {
        ...bannerForm.value,
        title: data.title,
        subtitle: data.subtitle,
        background_image_url: data.background_image_url,
        background_image_url_display: data.background_image_url_display,
        button_text: data.button_text || '',
        button_link: data.button_link || '',
        button_enabled: data.button_enabled !== undefined ? data.button_enabled : true,
        is_active: data.is_active
      }
      bannerOriginalForm.value = { ...bannerForm.value }
      bannerImageFile.value = null
      bannerImagePreview.value = ''
      bannerImageRemoved.value = false
      bannerImageChanged.value = false
      
      bannerSuccess.value = '✅ Баннер успешно обновлён!'
      
      setTimeout(() => {
        bannerSuccess.value = ''
      }, 3000)
    } else {
      const data = await res.json()
      bannerSubmitError.value = data.detail || data.message || 'Ошибка обновления'
      console.error('Ошибка сервера:', data)
    }
  } catch (e) {
    console.error('Ошибка:', e)
    bannerSubmitError.value = 'Ошибка подключения к серверу'
  } finally {
    bannerSubmitting.value = false
  }
}

// ============================================
// ЖИЗНЕННЫЙ ЦИКЛ
// ============================================
onMounted(async () => {
  authStore.restoreAuth()
  await loadBanner()
})
</script>