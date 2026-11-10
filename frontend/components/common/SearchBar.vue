<!-- frontend/components/common/SearchBar.vue -->
<template>
  <form
    role="search"
    class="flex items-center rounded-full transition-shadow duration-300 focus-within:ring-2 focus-within:ring-blue-500"
    :class="block ? 'w-full' : ''"
    @submit.prevent="submit"
  >
    <input
      v-model="query"
      type="text"
      placeholder="Поиск по сайту…"
      aria-label="Поиск по сайту"
      class="px-4 py-2 text-sm rounded-l-full border border-r-0 border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-gray-700 text-gray-800 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:outline-none"
      :class="block ? 'flex-1 min-w-0' : 'w-44 md:w-52'"
      @keyup.esc="query = ''"
    />
    <button
      type="submit"
      aria-label="Найти"
      class="px-3 py-2 rounded-r-full border border-l-0 border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-gray-700 text-gray-400 dark:text-gray-500 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-gray-100 dark:hover:bg-gray-600 transition-colors"
    >
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35M17 11a6 6 0 11-12 0 6 6 0 0112 0z"/>
      </svg>
    </button>
  </form>
</template>

<script setup>
const props = defineProps({
  // block=true — поле на всю ширину (в бургер-меню на мобильных)
  block: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['submitted'])

const router = useRouter()
const query = ref('')

const submit = () => {
  const q = query.value.trim()
  if (q.length < 2) return
  router.push({ path: '/search', query: { q } })
  query.value = ''
  emit('submitted')
}
</script>
