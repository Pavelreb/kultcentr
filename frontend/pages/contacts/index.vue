<!-- frontend/pages/contacts/index.vue -->
<template>
  <div class="container mx-auto p-4 max-w-4xl">
    <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 mb-6 flex items-center gap-3">
      <!-- Иконка "Контакты" -->
      <svg class="w-8 h-8 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
      </svg>
      Контакты
    </h1>
    
    <div v-if="loading" class="text-center py-10">
      <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="error" class="text-center py-10 text-red-500">
      <svg class="w-16 h-16 mx-auto text-red-400 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
      </svg>
      {{ error }}
    </div>
    
    <div v-else-if="contact" class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 overflow-hidden transition-colors duration-200">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-0">
        <!-- Левая колонка: О нас -->
        <div class="p-6 md:p-8 lg:p-10 bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20">
          <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4 flex items-center gap-2">
            <svg class="w-6 h-6 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 21v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v4a2 2 0 002 2h2a2 2 0 002-2V3"/>
            </svg>
            О нас
          </h2>
          <p class="text-gray-600 dark:text-gray-300 leading-relaxed whitespace-pre-wrap">
            {{ contact.description }}
          </p>
        </div>
        
        <!-- Правая колонка: Контакты -->
        <div class="p-6 md:p-8 lg:p-10">
          <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4 flex items-center gap-2">
            <svg class="w-6 h-6 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
            </svg>
            Контактная информация
          </h2>
          
          <ul class="space-y-4 text-gray-600 dark:text-gray-300">
            <!-- Адрес -->
            <li>
              <span class="text-xs text-gray-400 dark:text-gray-500">Адрес</span>
              <p class="font-medium flex items-center gap-2 mt-0.5">
                <svg class="w-4 h-4 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
                {{ contact.address }}
              </p>
            </li>
            
            <!-- Телефон -->
            <li>
              <span class="text-xs text-gray-400 dark:text-gray-500">Телефон</span>
              <p class="font-medium flex items-center gap-2 mt-0.5">
                <svg class="w-4 h-4 text-green-500 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                </svg>
                <a :href="`tel:${contact.phone}`" class="hover:text-blue-600 dark:hover:text-blue-400 transition">
                  {{ contact.phone }}
                </a>
              </p>
            </li>
            
            <!-- Email -->
            <li>
              <span class="text-xs text-gray-400 dark:text-gray-500">Email</span>
              <p class="font-medium flex items-center gap-2 mt-0.5">
                <svg class="w-4 h-4 text-purple-500 dark:text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                </svg>
                <a :href="`mailto:${contact.email}`" class="hover:text-blue-600 dark:hover:text-blue-400 transition">
                  {{ contact.email }}
                </a>
              </p>
            </li>
            
            <!-- Часы работы -->
            <li>
              <span class="text-xs text-gray-400 dark:text-gray-500">Часы работы</span>
              <p class="font-medium flex items-center gap-2 mt-0.5">
                <svg class="w-4 h-4 text-amber-500 dark:text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                {{ contact.work_hours }}
              </p>
            </li>
          </ul>
          
          <!-- Социальные сети -->
          <div v-if="contact.instagram || contact.vk || contact.telegram" class="mt-6 pt-6 border-t border-gray-200 dark:border-gray-700">
            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 mb-3 flex items-center gap-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/>
              </svg>
              Мы в соцсетях
            </h3>
            <div class="flex gap-3">
              <a 
                v-if="contact.instagram" 
                :href="contact.instagram" 
                target="_blank" 
                class="w-10 h-10 rounded-full bg-gradient-to-br from-pink-500 to-orange-500 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow-lg hover:shadow-xl"
                title="Instagram"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>
                </svg>
              </a>
              <a 
                v-if="contact.vk" 
                :href="contact.vk" 
                target="_blank" 
                class="w-10 h-10 rounded-full bg-blue-600 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow-lg hover:shadow-xl"
                title="VK"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M13.162 18.994c.609 0 .858-.406.851-.915-.031-1.917.714-2.949 2.059-1.604 1.488 1.488 1.796 2.519 3.603 2.519h3.2c.808 0 1.126-.26 1.126-.668 0-.863-1.421-2.386-2.625-3.504-1.686-1.565-1.765-1.602-.313-3.486 1.507-1.949 2.505-3.995 1.628-4.147-.244-.04-1.183-.05-2.303.018-.079.008-.146.03-.206.066-.128.075-.252.17-.389.291-1.158 1.039-2.208 2.313-2.562 2.486-.105.052-.18.063-.259.045-.142-.034-.338-.212-.354-.944-.028-1.258-.341-2.021-.946-2.384-.283-.17-.494-.262-1.371-.252-.674.007-1.172.055-1.613.336-.24.153-.383.367-.565.763-.07.153-.146.354-.226.617-.242.788-.483 1.574-1.037 2.287-.335.431-.748.899-1.155 1.331-.133.143-.255.273-.38.399-.425.428-.729.459-.915.445-.389-.029-.786-.044-1.054-.11-.703-.174-1.004-.854-1.08-1.398-.037-.265-.117-.712-.132-.997-.034-.663-.172-1.164-.628-1.455-.273-.174-.655-.249-1.273-.252-.816-.004-1.337.161-1.582.611-.21.386-.091.979.009 1.279.067.201.186.436.315.685.344.664.736 1.421 1.248 2.134.87 1.213 1.62 2.116 2.546 3.087.886.93 1.751 1.487 2.713 1.805.449.149.761.205 1.141.21z"/>
                </svg>
              </a>
              <a 
                v-if="contact.telegram" 
                :href="contact.telegram" 
                target="_blank" 
                class="w-10 h-10 rounded-full bg-blue-400 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow-lg hover:shadow-xl"
                title="Telegram"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

useSeoMeta({
  title: 'Контакты',
  description: 'Контакты центра культуры: адрес, телефон, время работы.'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const contact = ref(null)
const loading = ref(true)
const error = ref('')

onMounted(() => {
  authStore.restoreAuth()
})

onMounted(async () => {
  try {
    const res = await fetch(`${API_URL}/contact-info/`)
    if (res.ok) {
      contact.value = await res.json()
    } else {
      error.value = 'Не удалось загрузить контакты'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    loading.value = false
  }
})
</script>