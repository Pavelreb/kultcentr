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
          <div v-if="contact.vk || contact.max || contact.ok || contact.rutube" class="mt-6 pt-6 border-t border-gray-200 dark:border-gray-700">
            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 mb-3 flex items-center gap-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/>
              </svg>
              Мы в соцсетях
            </h3>
            <div class="flex gap-3">
              <a
                v-if="contact.vk"
                :href="contact.vk"
                target="_blank"
                class="w-10 h-10 rounded-full bg-blue-600 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow-lg hover:shadow-xl"
                title="ВКонтакте"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M13.162 18.994c.609 0 .858-.406.851-.915-.031-1.917.714-2.949 2.059-1.604 1.488 1.488 1.796 2.519 3.603 2.519h3.2c.808 0 1.126-.26 1.126-.668 0-.863-1.421-2.386-2.625-3.504-1.686-1.565-1.765-1.602-.313-3.486 1.507-1.949 2.505-3.995 1.628-4.147-.244-.04-1.183-.05-2.303.018-.079.008-.146.03-.206.066-.128.075-.252.17-.389.291-1.158 1.039-2.208 2.313-2.562 2.486-.105.052-.18.063-.259.045-.142-.034-.338-.212-.354-.944-.028-1.258-.341-2.021-.946-2.384-.283-.17-.494-.262-1.371-.252-.674.007-1.172.055-1.613.336-.24.153-.383.367-.565.763-.07.153-.146.354-.226.617-.242.788-.483 1.574-1.037 2.287-.335.431-.748.899-1.155 1.331-.133.143-.255.273-.38.399-.425.428-.729.459-.915.445-.389-.029-.786-.044-1.054-.11-.703-.174-1.004-.854-1.08-1.398-.037-.265-.117-.712-.132-.997-.034-.663-.172-1.164-.628-1.455-.273-.174-.655-.249-1.273-.252-.816-.004-1.337.161-1.582.611-.21.386-.091.979.009 1.279.067.201.186.436.315.685.344.664.736 1.421 1.248 2.134.87 1.213 1.62 2.116 2.546 3.087.886.93 1.751 1.487 2.713 1.805.449.149.761.205 1.141.21z"/>
                </svg>
              </a>
              <a
                v-if="contact.max"
                :href="contact.max"
                target="_blank"
                class="w-10 h-10 rounded-full bg-gradient-to-br from-purple-500 to-indigo-600 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow-lg hover:shadow-xl"
                title="MAX"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2C6.48 2 2 6.02 2 11c0 2.4 1.05 4.6 2.77 6.27-.13.86-.65 2.47-1.65 3.73 1.4-.08 3.13-.68 4.16-1.22.86.25 1.78.39 2.72.39 5.52 0 10-4.02 10-8.97S17.52 2 12 2zm-4.5 9.5a1.5 1.5 0 110-3 1.5 1.5 0 010 3zm4.5 0a1.5 1.5 0 110-3 1.5 1.5 0 010 3zm4.5 0a1.5 1.5 0 110-3 1.5 1.5 0 010 3z"/>
                </svg>
              </a>
              <a
                v-if="contact.ok"
                :href="contact.ok"
                target="_blank"
                class="w-10 h-10 rounded-full bg-orange-500 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow-lg hover:shadow-xl"
                title="Одноклассники"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2a5 5 0 00-5 5c0 2.76 2.24 5 5 5s5-2.24 5-5a5 5 0 00-5-5zm0 8a3 3 0 110-6 3 3 0 010 6zm5.83 3.42a1.25 1.25 0 00-1.77-.15c-1.1.94-2.55 1.5-4.06 1.5s-2.96-.56-4.06-1.5a1.25 1.25 0 10-1.62 1.9c1.28 1.1 2.87 1.76 4.55 1.93l-2.6 3.9a1.25 1.25 0 102.06 1.4L12 19.66l1.67 2.51a1.25 1.25 0 102.06-1.4l-2.6-3.9c1.68-.17 3.27-.83 4.55-1.93.5-.42.56-1.17.15-1.62z"/>
                </svg>
              </a>
              <a
                v-if="contact.rutube"
                :href="contact.rutube"
                target="_blank"
                class="w-10 h-10 rounded-full bg-gray-900 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow-lg hover:shadow-xl"
                title="RuTube"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/>
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