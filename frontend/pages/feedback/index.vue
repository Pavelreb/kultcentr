<!-- frontend/pages/feedback/index.vue -->
<template>
  <div class="max-w-2xl mx-auto mt-10 px-4">
    <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3 mb-6">
      <svg class="w-8 h-8 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
      </svg>
      Обратная связь
    </h1>
    <FeedbackForm />
  </div>
</template>

<script setup>
import FeedbackForm from '~/components/common/FeedbackForm.vue'

useSeoMeta({
  title: 'Обратная связь',
  description: 'Напишите нам: вопросы, предложения и замечания. Регистрация не требуется.'
})
</script>
