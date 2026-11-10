<!-- frontend/components/layout/AppFooter.vue -->
<template>
  <footer class="app-footer text-gray-300 mt-10">
    <div class="container mx-auto px-4">
      <div v-if="contactsLoading" class="text-center py-4 text-gray-400">
        Загрузка контактов...
      </div>
      
      <div v-else-if="contacts" class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Левая колонка: Описание -->
        <div>
          <h3 class="text-white text-lg font-semibold mb-3 flex items-center gap-2">
            <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 21v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v4a2 2 0 002 2h2a2 2 0 002-2V3"/>
            </svg>
            Центр Культуры
          </h3>
          <p class="text-sm text-gray-400 leading-relaxed whitespace-pre-wrap">
            {{ contacts.description }}
          </p>

          <!-- Социальные сети -->
          <div v-if="contacts.vk || contacts.max || contacts.ok || contacts.rutube" class="social-links flex gap-3 mt-4">
            <a
              v-if="contacts.vk"
              :href="contacts.vk"
              target="_blank"
              class="w-9 h-9 rounded-full bg-blue-600 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow-lg"
              title="ВКонтакте"
            >
              <svg class="w-[18px] h-[18px]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M13.162 18.994c.609 0 .858-.406.851-.915-.031-1.917.714-2.949 2.059-1.604 1.488 1.488 1.796 2.519 3.603 2.519h3.2c.808 0 1.126-.26 1.126-.668 0-.863-1.421-2.386-2.625-3.504-1.686-1.565-1.765-1.602-.313-3.486 1.507-1.949 2.505-3.995 1.628-4.147-.244-.04-1.183-.05-2.303.018-.079.008-.146.03-.206.066-.128.075-.252.17-.389.291-1.158 1.039-2.208 2.313-2.562 2.486-.105.052-.18.063-.259.045-.142-.034-.338-.212-.354-.944-.028-1.258-.341-2.021-.946-2.384-.283-.17-.494-.262-1.371-.252-.674.007-1.172.055-1.613.336-.24.153-.383.367-.565.763-.07.153-.146.354-.226.617-.242.788-.483 1.574-1.037 2.287-.335.431-.748.899-1.155 1.331-.133.143-.255.273-.38.399-.425.428-.729.459-.915.445-.389-.029-.786-.044-1.054-.11-.703-.174-1.004-.854-1.08-1.398-.037-.265-.117-.712-.132-.997-.034-.663-.172-1.164-.628-1.455-.273-.174-.655-.249-1.273-.252-.816-.004-1.337.161-1.582.611-.21.386-.091.979.009 1.279.067.201.186.436.315.685.344.664.736 1.421 1.248 2.134.87 1.213 1.62 2.116 2.546 3.087.886.93 1.751 1.487 2.713 1.805.449.149.761.205 1.141.21z"/>
              </svg>
            </a>
            <a
              v-if="contacts.max"
              :href="contacts.max"
              target="_blank"
              class="w-9 h-9 rounded-full bg-gradient-to-br from-purple-500 to-indigo-600 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow-lg"
              title="MAX"
            >
              <svg class="w-[18px] h-[18px]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2C6.48 2 2 6.02 2 11c0 2.4 1.05 4.6 2.77 6.27-.13.86-.65 2.47-1.65 3.73 1.4-.08 3.13-.68 4.16-1.22.86.25 1.78.39 2.72.39 5.52 0 10-4.02 10-8.97S17.52 2 12 2zm-4.5 9.5a1.5 1.5 0 110-3 1.5 1.5 0 010 3zm4.5 0a1.5 1.5 0 110-3 1.5 1.5 0 010 3zm4.5 0a1.5 1.5 0 110-3 1.5 1.5 0 010 3z"/>
              </svg>
            </a>
            <a
              v-if="contacts.ok"
              :href="contacts.ok"
              target="_blank"
              class="w-9 h-9 rounded-full bg-orange-500 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow-lg"
              title="Одноклассники"
            >
              <svg class="w-[18px] h-[18px]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2a5 5 0 00-5 5c0 2.76 2.24 5 5 5s5-2.24 5-5a5 5 0 00-5-5zm0 8a3 3 0 110-6 3 3 0 010 6zm5.83 3.42a1.25 1.25 0 00-1.77-.15c-1.1.94-2.55 1.5-4.06 1.5s-2.96-.56-4.06-1.5a1.25 1.25 0 10-1.62 1.9c1.28 1.1 2.87 1.76 4.55 1.93l-2.6 3.9a1.25 1.25 0 102.06 1.4L12 19.66l1.67 2.51a1.25 1.25 0 102.06-1.4l-2.6-3.9c1.68-.17 3.27-.83 4.55-1.93.5-.42.56-1.17.15-1.62z"/>
              </svg>
            </a>
            <a
              v-if="contacts.rutube"
              :href="contacts.rutube"
              target="_blank"
              class="w-9 h-9 rounded-full bg-gray-900 border border-gray-700 flex items-center justify-center text-white hover:scale-110 transition-transform duration-300 shadow-lg"
              title="RuTube"
            >
              <svg class="w-[18px] h-[18px]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/>
              </svg>
            </a>
          </div>
        </div>
        
        <!-- Центральная колонка: Контакты -->
        <div>
          <h3 class="text-white text-lg font-semibold mb-3 flex items-center gap-2">
            <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
            </svg>
            Контакты
          </h3>
          <ul class="space-y-2 text-sm">
            <li class="flex items-center gap-2 text-gray-300">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
              </svg>
              <span>{{ contacts.address }}</span>
            </li>
            <li class="flex items-center gap-2 text-gray-300">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
              </svg>
              <a :href="`tel:${contacts.phone}`" class="text-gray-300 hover:text-blue-400 transition">
                {{ contacts.phone }}
              </a>
            </li>
            <li class="flex items-center gap-2 text-gray-300">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
              </svg>
              <a :href="`mailto:${contacts.email}`" class="text-gray-300 hover:text-blue-400 transition">
                {{ contacts.email }}
              </a>
            </li>
            <li class="flex items-center gap-2 text-gray-300">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <span>{{ contacts.work_hours }}</span>
            </li>
          </ul>
        </div>
        
        <!-- Правая колонка: Разделы -->
        <div>
          <h3 class="text-white text-lg font-semibold mb-3 flex items-center gap-2">
            <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
            </svg>
            Разделы
          </h3>
          <ul class="space-y-2 text-sm">
            <li>
              <NuxtLink to="/events" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
                </svg>
                Афиша
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/posts" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
                </svg>
                Публикации
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/gallery" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
                Галерея
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/authors" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
                </svg>
                Авторы
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/contacts" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                </svg>
                Контакты
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/guide" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                </svg>
                Справочник
              </NuxtLink>
            </li>
            <li v-if="authStore.isEditor">
              <NuxtLink to="/settings" class="flex items-center gap-2 text-yellow-400 hover:text-yellow-300 transition">
                <svg class="w-4 h-4 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
                Настройки
              </NuxtLink>
            </li>
          </ul>
        </div>
      </div>
      
      <div class="border-t border-gray-800 mt-6 pt-6 text-center text-sm text-gray-500">
        <p>© {{ new Date().getFullYear() }} Центр Культуры. Все права защищены.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()

const contacts = ref(null)
const contactsLoading = ref(true)

const loadContacts = async () => {
  contactsLoading.value = true
  try {
    const res = await fetch(`${API_URL}/contact-info/`)
    if (res.ok) {
      contacts.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка загрузки контактов:', e)
  } finally {
    contactsLoading.value = false
  }
}

onMounted(async () => {
  await loadContacts()
  window.addEventListener('contacts-updated', loadContacts)
})

onUnmounted(() => {
  window.removeEventListener('contacts-updated', loadContacts)
})
</script>

<style scoped>
.app-footer {
  background-color: #111827 !important;
  padding-top: 40px !important;
  padding-bottom: 40px !important;
}

.app-footer,
.app-footer * {
  color: #d1d5db !important;
}

.app-footer h3 {
  color: #ffffff !important;
}

.app-footer a {
  color: #d1d5db !important;
}

.app-footer a:hover {
  color: #60a5fa !important;
}

.app-footer .social-links a,
.app-footer .social-links a:hover {
  color: #ffffff !important;
}

:where(.dark) .app-footer {
  background-color: #111827 !important;
}

:where(.dark) .app-footer,
:where(.dark) .app-footer * {
  color: #d1d5db !important;
}

:where(.dark) .app-footer h3 {
  color: #ffffff !important;
}

:where(.dark) .app-footer a {
  color: #d1d5db !important;
}

:where(.dark) .app-footer a:hover {
  color: #60a5fa !important;
}
</style>