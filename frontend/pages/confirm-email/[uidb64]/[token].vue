<template>
  <div style="margin-top: 120px;">
    <div class="max-w-md mx-auto bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
      <div v-if="loading" class="text-center py-10">
        <p class="text-gray-500 dark:text-gray-400">Подтверждение...</p>
      </div>
      
      <div v-else-if="success" class="text-center py-10">
        <div class="text-green-500 text-6xl mb-4">✅</div>
        <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Email подтверждён!</h2>
        <p class="text-gray-600 dark:text-gray-400">Теперь вы можете войти в систему.</p>
        <NuxtLink 
          to="/auth/login" 
          class="mt-6 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
        >
          Перейти к входу
        </NuxtLink>
      </div>
      
      <div v-else class="text-center py-10">
        <div class="text-red-500 text-6xl mb-4">❌</div>
        <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Ошибка подтверждения</h2>
        <p class="text-gray-600 dark:text-gray-400">{{ errorMessage || 'Неверная ссылка подтверждения' }}</p>
        <NuxtLink 
          to="/auth/login" 
          class="mt-6 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
        >
          На страницу входа
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const loading = ref(true)
const success = ref(false)
const errorMessage = ref('')

onMounted(async () => {
  try {
    const { uidb64, token } = route.params
    console.log('📡 Подтверждение email:', uidb64, token)
    
    const res = await fetch(`${API_URL}/auth/confirm-email/${uidb64}/${token}/`)
    const data = await res.json()
    console.log('📡 Ответ сервера:', res.status, data)
    
    if (res.ok) {
      success.value = true
    } else {
      errorMessage.value = data.detail || 'Неверная ссылка подтверждения'
    }
  } catch (e) {
    errorMessage.value = 'Ошибка подключения к серверу'
    console.error('❌ Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>