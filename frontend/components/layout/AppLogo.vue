<!-- frontend/components/layout/AppLogo.vue -->
<template>
  <NuxtLink to="/" class="flex items-center gap-2 text-xl font-bold text-gray-800 dark:text-white hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
    <img
      v-if="logoUrl"
      :src="logoUrl"
      :alt="name"
      class="w-8 h-8 rounded-full object-cover"
    />
    <!-- SVG-заглушка, если логотип не задан в настройках -->
    <svg v-else class="w-8 h-8 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z"/>
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 21v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4"/>
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v4a2 2 0 002 2h2a2 2 0 002-2V3"/>
    </svg>
    <span class="hidden sm:inline">{{ name }}</span>
    <span class="sm:hidden">{{ shortName }}</span>
  </NuxtLink>
</template>

<script setup>
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const name = ref('Центр Культуры')
const logoUrl = ref('')

// Короткое название для маленьких экранов — инициалы из слов
const shortName = computed(() => {
  const words = name.value.trim().split(/\s+/).filter(Boolean)
  if (words.length === 1) return words[0].slice(0, 2).toUpperCase()
  return words.map(w => w[0]).join('').toUpperCase()
})

onMounted(async () => {
  await loadInfo()
  window.addEventListener('institution-updated', loadInfo)
})

onUnmounted(() => {
  window.removeEventListener('institution-updated', loadInfo)
})

async function loadInfo() {
  try {
    const res = await fetch(`${API_URL}/about/info/`)
    if (res.ok) {
      const data = await res.json()
      if (data.name) name.value = data.name
      if (data.logo_display) logoUrl.value = data.logo_display
    }
  } catch (e) {
    // Оставляем значения по умолчанию
  }
}
</script>
