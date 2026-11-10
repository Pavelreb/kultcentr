<!-- frontend/components/features/about/AchievementCard.vue -->
<template>
  <NuxtLink
    :to="`/about/achievements/${achievement.id}`"
    class="group bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden flex flex-col h-full hover:-translate-y-1 border border-gray-100 dark:border-gray-700"
  >
    <div class="relative aspect-video overflow-hidden bg-gradient-to-br from-amber-50 to-amber-100 dark:from-gray-700 dark:to-gray-800">
      <img
        v-if="achievement.display_image"
        :src="achievement.display_image"
        :alt="achievement.title"
        class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
        loading="lazy"
      />
      <div v-else class="w-full h-full flex items-center justify-center">
        <svg class="w-14 h-14 text-amber-300 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/>
        </svg>
      </div>
      <div
        v-if="achievement.date"
        class="absolute top-3 left-3 px-2.5 py-1 rounded-full text-xs font-medium bg-amber-500 text-white shadow-lg"
      >
        {{ formatDate(achievement.date) }}
      </div>
    </div>
    <div class="p-4 flex flex-col flex-1">
      <h3 class="text-base font-semibold text-gray-800 dark:text-gray-200 group-hover:text-amber-600 dark:group-hover:text-amber-400 transition-colors line-clamp-2">
        {{ achievement.title }}
      </h3>
      <p v-if="achievement.excerpt" class="text-sm text-gray-500 dark:text-gray-400 mt-1.5 line-clamp-3">
        {{ achievement.excerpt }}
      </p>
    </div>
  </NuxtLink>
</template>

<script setup>
defineProps({
  achievement: {
    type: Object,
    required: true
  }
})

const formatDate = (dateStr) => {
  if (!dateStr) return ''
  return new Date(dateStr).toLocaleDateString('ru-RU', {
    day: 'numeric', month: 'long', year: 'numeric'
  })
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
