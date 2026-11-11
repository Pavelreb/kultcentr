<!-- frontend/components/features/media/AudioCard.vue -->
<template>
  <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-shadow duration-300 overflow-hidden p-4">
    <div class="flex items-center gap-3 mb-3">
      <!-- Обложка -->
      <div class="w-12 h-12 flex-shrink-0 rounded-lg overflow-hidden bg-gradient-to-br from-teal-500 to-emerald-600 flex items-center justify-center">
        <img
          v-if="audio.cover_display"
          :src="audio.cover_display"
          :alt="audio.title"
          class="w-full h-full object-cover"
        >
        <svg v-else class="w-6 h-6 text-white/90" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/>
        </svg>
      </div>
      <div class="flex-1 min-w-0">
        <h3 class="text-sm font-semibold text-gray-800 dark:text-gray-200 truncate">
          {{ audio.title }}
        </h3>
        <p class="text-xs text-gray-400 dark:text-gray-500">
          {{ formatDate(audio.created_at) }}
        </p>
      </div>
    </div>

    <AudioPlayer v-if="audio.file_display" :src="audio.file_display" :duration-hint="audio.duration" />

    <p v-if="audio.description" class="text-xs text-gray-500 dark:text-gray-400 mt-3 line-clamp-2">
      {{ audio.description }}
    </p>
  </div>
</template>

<script setup>
import AudioPlayer from '~/components/common/AudioPlayer.vue'

defineProps({
  audio: {
    type: Object,
    required: true
  }
})

const formatDate = (iso) => {
  if (!iso) return ''
  return new Date(iso).toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })
}
</script>
