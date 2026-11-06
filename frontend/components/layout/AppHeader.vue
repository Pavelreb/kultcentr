<!-- frontend/components/layout/AppHeader.vue -->
<template>
  <header class="bg-white dark:bg-gray-800 shadow transition-colors duration-200 sticky top-0 z-50 border-b border-gray-200 dark:border-gray-700">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center">
      <!-- Левая часть: Логотип + Бургер -->
      <div class="flex items-center gap-2">
        <AppLogo />
        <BurgerMenu />
      </div>
      
      <!-- Правая часть: Создать + Переключатель темы + Кнопки пользователя -->
      <div class="flex items-center gap-2 md:gap-4">
        <CreateMenu />
        <ThemeToggle />
        <AuthButtons />
      </div>
    </div>
  </header>
</template>

<script setup>
import AppLogo from './AppLogo.vue'
import BurgerMenu from '~/components/common/BurgerMenu.vue'
import ThemeToggle from '~/components/common/ThemeToggle.vue'
import AuthButtons from '~/components/common/AuthButtons.vue'
import CreateMenu from '~/components/common/CreateMenu.vue'
</script>