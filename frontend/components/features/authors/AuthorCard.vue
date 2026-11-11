<!-- frontend/components/features/authors/AuthorCard.vue -->
<template>
  <NuxtLink 
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
        
        <!-- Онлайн-статус -->
        <div
          v-if="author.is_online"
          class="absolute bottom-1 right-1 w-4 h-4 bg-green-500 border-2 border-white dark:border-gray-800 rounded-full"
          title="В сети"
        ></div>
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
        <span v-if="author.is_online" class="inline-flex items-center gap-1 text-[10px] font-medium text-emerald-600 dark:text-emerald-400">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
          в сети
        </span>
      </div>
      
      <!-- Краткая статистика -->
      <div class="grid grid-cols-4 gap-2 mt-3 pt-3 border-t border-gray-100 dark:border-gray-700">
        <!-- Публикации -->
        <div class="group/stat text-center cursor-default">
          <div class="flex items-center justify-center gap-1 text-xs text-gray-400 dark:text-gray-500">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9"/>
            </svg>
            <span class="font-medium text-gray-700 dark:text-gray-300">
              {{ author.posts_count || 0 }}
            </span>
          </div>
          <span class="block text-[10px] text-gray-400 dark:text-gray-500 opacity-0 group-hover/stat:opacity-100 transition-opacity duration-200">Публикаций</span>
        </div>

        <!-- Подписчики -->
        <div class="group/stat text-center cursor-default">
          <div class="flex items-center justify-center gap-1 text-xs text-gray-400 dark:text-gray-500">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/>
            </svg>
            <span class="font-medium text-gray-700 dark:text-gray-300">
              {{ author.subscribers_count || 0 }}
            </span>
          </div>
          <span class="block text-[10px] text-gray-400 dark:text-gray-500 opacity-0 group-hover/stat:opacity-100 transition-opacity duration-200">Подписчиков</span>
        </div>

        <!-- Просмотры -->
        <div class="group/stat text-center cursor-default">
          <div class="flex items-center justify-center gap-1 text-xs text-gray-400 dark:text-gray-500">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
            </svg>
            <span class="font-medium text-gray-700 dark:text-gray-300">
              {{ author.total_views || 0 }}
            </span>
          </div>
          <span class="block text-[10px] text-gray-400 dark:text-gray-500 opacity-0 group-hover/stat:opacity-100 transition-opacity duration-200">Просмотров</span>
        </div>

        <!-- Лайки -->
        <div class="group/stat text-center cursor-default">
          <div class="flex items-center justify-center gap-1 text-xs text-gray-400 dark:text-gray-500">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <span class="font-medium text-gray-700 dark:text-gray-300">
              {{ author.total_likes || 0 }}
            </span>
          </div>
          <span class="block text-[10px] text-gray-400 dark:text-gray-500 opacity-0 group-hover/stat:opacity-100 transition-opacity duration-200">Лайков</span>
        </div>
      </div>
      
      <!-- Кнопка "Публикации автора" -->
      <div class="mt-3 inline-flex items-center gap-1.5 text-xs font-medium text-blue-500 dark:text-blue-400 group-hover:text-blue-700 dark:group-hover:text-blue-300 transition-colors">
        <span>Публикации автора</span>
        <svg class="w-3.5 h-3.5 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
        </svg>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
const props = defineProps({
  author: {
    type: Object,
    required: true
  }
})

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
</script>