<!-- frontend/components/features/media/VideoCard.vue -->
<template>
  <NuxtLink
    :to="`/media/videos/${video.id}`"
    class="group bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden hover:-translate-y-1"
  >
    <!-- Обложка 16:9 -->
    <div class="relative aspect-video overflow-hidden bg-gray-100 dark:bg-gray-700">
      <img
        v-if="video.thumbnail_display"
        :src="video.thumbnail_display"
        :alt="video.title"
        class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
      >
      <div
        v-else
        class="w-full h-full bg-gradient-to-br from-rose-500 to-red-600 flex items-center justify-center"
      >
        <svg class="w-12 h-12 text-white/80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/>
        </svg>
      </div>

      <!-- Кнопка play по центру -->
      <div class="absolute inset-0 flex items-center justify-center bg-black/0 group-hover:bg-black/25 transition-colors duration-300">
        <div class="w-12 h-12 rounded-full bg-white/90 dark:bg-gray-800/90 flex items-center justify-center shadow-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300 scale-90 group-hover:scale-100">
          <svg class="w-5 h-5 text-rose-600 ml-0.5" fill="currentColor" viewBox="0 0 24 24">
            <path d="M8 5v14l11-7z"/>
          </svg>
        </div>
      </div>

      <!-- Длительность -->
      <span
        v-if="video.duration"
        class="absolute bottom-2 right-2 px-1.5 py-0.5 rounded-md bg-black/70 text-white text-[10px] font-medium"
      >
        {{ formatDuration(video.duration) }}
      </span>
    </div>

    <div class="p-3">
      <h3 class="text-sm font-semibold text-gray-800 dark:text-gray-200 line-clamp-2 group-hover:text-rose-600 dark:group-hover:text-rose-400 transition-colors">
        {{ video.title }}
      </h3>
      <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">
        {{ formatDate(video.created_at) }}
      </p>
    </div>
  </NuxtLink>
</template>

<script setup>
defineProps({
  video: {
    type: Object,
    required: true
  }
})

const formatDuration = (sec) => {
  if (!sec && sec !== 0) return ''
  const m = Math.floor(sec / 60)
  const s = sec % 60
  return `${m}:${String(s).padStart(2, '0')}`
}

const formatDate = (iso) => {
  if (!iso) return ''
  return new Date(iso).toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })
}
</script>
