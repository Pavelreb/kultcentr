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