<!-- frontend/components/ui/SkeletonCard.vue -->
<template>
  <div class="bg-gray-200 dark:bg-gray-700 rounded-xl animate-pulse overflow-hidden">
    <div class="aspect-[4/3] bg-gray-300 dark:bg-gray-600"></div>
    <div class="p-4 space-y-3">
      <div class="h-4 bg-gray-300 dark:bg-gray-600 rounded w-3/4"></div>
      <div class="h-3 bg-gray-300 dark:bg-gray-600 rounded w-full"></div>
      <div class="h-3 bg-gray-300 dark:bg-gray-600 rounded w-2/3"></div>
      <div class="flex gap-2 pt-2">
        <div class="h-6 bg-gray-300 dark:bg-gray-600 rounded-full w-16"></div>
        <div class="h-6 bg-gray-300 dark:bg-gray-600 rounded-full w-16"></div>
      </div>
    </div>
  </div>
</template>