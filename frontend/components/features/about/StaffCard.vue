<!-- frontend/components/features/about/StaffCard.vue -->
<template>
  <component
    :is="member.user_id ? 'NuxtLink' : 'div'"
    :to="member.user_id ? `/users/${member.user_id}` : undefined"
    class="bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 hover:-translate-y-1 p-5 flex flex-col items-center text-center border border-gray-100 dark:border-gray-700"
  >
    <div class="w-24 h-24 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-2xl font-bold overflow-hidden flex-shrink-0 shadow-md">
      <img v-if="member.display_photo" :src="member.display_photo" :alt="member.full_name" class="w-full h-full object-cover" />
      <span v-else>{{ initials }}</span>
    </div>
    <h3 class="mt-3 font-semibold text-gray-800 dark:text-gray-200 leading-tight">{{ member.full_name }}</h3>
    <p class="text-sm text-gray-500 dark:text-gray-400 mt-0.5">{{ member.position }}</p>
    <span class="mt-2 px-2.5 py-0.5 rounded-full text-[11px] font-medium" :class="categoryClass">
      {{ member.category_display }}
    </span>
  </component>
</template>

<script setup>
const props = defineProps({
  member: {
    type: Object,
    required: true
  }
})

const initials = computed(() => {
  const parts = (props.member.full_name || '?').split(' ')
  if (parts.length >= 2) return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  return (props.member.full_name || '?').substring(0, 2).toUpperCase()
})

const categoryClass = computed(() => {
  switch (props.member.category) {
    case 'aup':
      return 'bg-yellow-100 dark:bg-yellow-900/30 text-yellow-700 dark:text-yellow-300'
    case 'main':
      return 'bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-300'
    case 'technical':
      return 'bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300'
    default:
      return 'bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300'
  }
})
</script>
