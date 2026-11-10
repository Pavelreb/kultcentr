<!-- frontend/components/features/about/DocumentCard.vue -->
<template>
  <a
    :href="doc.file_display"
    target="_blank"
    rel="noopener"
    class="group flex items-center gap-3 bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 hover:-translate-y-0.5 p-3 border border-gray-100 dark:border-gray-700"
    :title="doc.title"
  >
    <div
      class="w-11 h-11 rounded-lg flex items-center justify-center flex-shrink-0 text-white text-[10px] font-bold uppercase tracking-wide"
      :class="extColor"
    >
      {{ doc.file_ext || 'doc' }}
    </div>
    <span class="flex-1 min-w-0 text-sm font-medium text-gray-800 dark:text-gray-200 line-clamp-2 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
      {{ doc.title }}
    </span>
    <svg class="w-4 h-4 text-gray-300 dark:text-gray-600 group-hover:text-blue-500 dark:group-hover:text-blue-400 transition-colors flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
    </svg>
  </a>
</template>

<script setup>
const props = defineProps({
  doc: { type: Object, required: true }
})

const extColor = computed(() => {
  const ext = props.doc.file_ext
  if (ext === 'pdf') return 'bg-red-500'
  if (ext === 'doc' || ext === 'docx') return 'bg-blue-500'
  if (ext === 'xls' || ext === 'xlsx') return 'bg-green-600'
  if (ext === 'ppt' || ext === 'pptx') return 'bg-orange-500'
  return 'bg-gray-500'
})
</script>
