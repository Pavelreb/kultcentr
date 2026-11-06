<!-- frontend/components/common/AuthButtons.vue -->
<template>
  <div class="flex items-center gap-3">
    <template v-if="authStore.isAuthenticated">
      <NuxtLink 
        to="/profile" 
        class="hidden md:flex items-center gap-2 text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition font-medium group"
      >
        <!-- Аватар -->
        <img 
          v-if="authStore.user?.avatar_url" 
          :src="authStore.user?.avatar_url" 
          :alt="displayName"
          class="w-8 h-8 rounded-full object-cover border-2 border-blue-200 dark:border-blue-800 group-hover:border-blue-400 dark:group-hover:border-blue-600 transition"
        >
        <div 
          v-else
          class="w-8 h-8 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-xs font-bold"
        >
          {{ authStore.initials }}
        </div>
        
        <!-- Имя и роль -->
        <div class="flex flex-col leading-tight">
          <!-- Имя пользователя -->
          <span class="font-medium text-gray-700 dark:text-gray-300">
            {{ displayName }}
          </span>
          <!-- Роль пользователя (маленькая надпись) -->
          <span class="text-xs text-gray-400 dark:text-gray-500">
            {{ roleDisplay }}
          </span>
        </div>
        
        <!-- Маленькая стрелка как индикатор -->
        <svg class="w-3 h-3 text-gray-400 dark:text-gray-500 group-hover:translate-x-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </NuxtLink>
    </template>
    
    <template v-else>
      <NuxtLink to="/auth/login">
        <UiButton variant="outline" size="sm" class="items-center gap-1.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"/>
          </svg>
          Войти
        </UiButton>
      </NuxtLink>
      
      <NuxtLink to="/auth/register">
        <UiButton variant="primary" size="sm" class="items-center gap-1.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/>
          </svg>
          Регистрация
        </UiButton>
      </NuxtLink>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'

const authStore = useAuthStore()

// Вычисляемое свойство для отображения имени
const displayName = computed(() => {
  return authStore.fullName || authStore.username
})

// Вычисляемое свойство для отображения роли
const roleDisplay = computed(() => {
  if (!authStore.user) return ''
  const roleMap = {
    'admin': 'Администратор',
    'editor': 'Главный редактор',
    'author': 'Автор',
    'subscriber': 'Подписчик'
  }
  return roleMap[authStore.user.role] || authStore.user.role_display || 'Пользователь'
})
</script>