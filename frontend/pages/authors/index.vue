<!-- frontend/pages/authors/index.vue -->
<template>
  <div class="container mx-auto p-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <!-- Иконка "Авторы" -->
        <svg class="w-8 h-8 text-purple-500 dark:text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
        </svg>
        Все авторы
      </h1>
    </div>
    
    <div v-if="loading" class="text-center py-20">
      <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="authors.length === 0" class="text-center py-20 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет авторов</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>
    
    <div v-else>
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 md:gap-5">
        <NuxtLink 
          v-for="author in authors" 
          :key="author.id" 
          :to="`/users/${author.id}`" 
          class="group bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden hover:-translate-y-1"
        >
          <div class="p-5 text-center">
            <!-- Аватар с обводкой -->
            <div class="relative w-24 h-24 mx-auto">
              <!-- Кольцо-ободок -->
              <div class="absolute inset-0 rounded-full bg-gradient-to-br from-blue-400 via-purple-400 to-pink-400 p-1 group-hover:scale-105 transition-transform duration-300">
                <div class="w-full h-full rounded-full bg-white dark:bg-gray-800 overflow-hidden">
                  <img 
                    v-if="author.avatar_url" 
                    :src="author.avatar_url" 
                    :alt="author.username" 
                    class="w-full h-full object-cover"
                  >
                  <div 
                    v-else 
                    class="w-full h-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-white text-2xl font-bold"
                  >
                    {{ getInitials(author) }}
                  </div>
                </div>
              </div>
              
              <!-- Онлайн-статус (заглушка) -->
              <div class="absolute bottom-1 right-1 w-4 h-4 bg-green-500 border-2 border-white dark:border-gray-800 rounded-full"></div>
            </div>
            
            <!-- Имя автора -->
            <h3 class="text-base font-semibold text-gray-800 dark:text-gray-200 mt-3 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
              {{ getFullName(author) }}
            </h3>
            
            <!-- Роль с иконкой -->
            <div class="flex items-center justify-center gap-1.5 mt-1">
              <svg class="w-3.5 h-3.5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
              </svg>
              <span class="text-xs text-gray-500 dark:text-gray-400">{{ author.role_display }}</span>
            </div>
            
            <!-- Краткая статистика -->
            <div class="flex justify-center gap-4 mt-3 pt-3 border-t border-gray-100 dark:border-gray-700">
              <!-- Количество публикаций -->
              <div class="text-center">
                <div class="flex items-center gap-1 text-xs text-gray-400 dark:text-gray-500">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9"/>
                  </svg>
                  <span class="font-medium text-gray-700 dark:text-gray-300">
                    {{ author.posts_count || 0 }}
                  </span>
                </div>
                <span class="text-[10px] text-gray-400 dark:text-gray-500">Публикаций</span>
              </div>
              
              <!-- Количество подписчиков -->
              <div class="text-center">
                <div class="flex items-center gap-1 text-xs text-gray-400 dark:text-gray-500">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/>
                  </svg>
                  <span class="font-medium text-gray-700 dark:text-gray-300">
                    {{ author.subscribers_count || 0 }}
                  </span>
                </div>
                <span class="text-[10px] text-gray-400 dark:text-gray-500">Подписчиков</span>
              </div>
            </div>
            
            <!-- Кнопка "Публикации автора" -->
            <div class="mt-3 inline-flex items-center gap-1.5 text-xs font-medium text-purple-500 dark:text-purple-400 group-hover:text-purple-700 dark:group-hover:text-purple-300 transition-colors">
              <span>Публикации автора</span>
              <svg class="w-3.5 h-3.5 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
              </svg>
            </div>
          </div>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()

useSeoMeta({
  title: 'Авторы',
  description: 'Авторы и редакция центра культуры.'
})
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authors = ref([])
const loading = ref(true)

const getInitials = (user) => {
  const name = user.full_name || user.username
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const getFullName = (user) => {
  return user.full_name || user.username
}

onMounted(async () => {
  try {
    const res = await fetch(`${API_URL}/auth/users/`)
    if (res.ok) {
      const allUsers = await res.json()
      authors.value = allUsers.filter(user => user.role === 'author' || user.role === 'editor')
    }
  } catch (e) {
    console.error('Ошибка загрузки авторов:', e)
  } finally {
    loading.value = false
  }
})
</script>