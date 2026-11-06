<template>
  <div class="max-w-md mx-auto mt-20 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Проверка ссылки...</p>
    </div>
    
    <div v-else-if="error" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">❌</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Ошибка</h2>
      <p class="text-gray-600 dark:text-gray-400">{{ errorMessage }}</p>
      <NuxtLink 
        to="/auth/login" 
        class="mt-6 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
      >
        На страницу входа
      </NuxtLink>
    </div>
    
    <div v-else-if="success" class="text-center py-10">
      <div class="text-green-500 text-6xl mb-4">✅</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Пароль изменён!</h2>
      <p class="text-gray-600 dark:text-gray-400">Теперь вы можете войти с новым паролем.</p>
      <NuxtLink 
        to="/auth/login" 
        class="mt-6 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
      >
        Перейти к входу
      </NuxtLink>
    </div>
    
    <div v-else class="text-center py-10">
      <div class="text-blue-500 text-6xl mb-4">🔑</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Создайте новый пароль</h2>
      
      <form @submit.prevent="resetPassword" class="mt-6 text-left">
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Новый пароль</label>
          <input 
            v-model="newPassword" 
            type="password" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            required
            minlength="8"
          >
        </div>
        
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Подтвердите пароль</label>
          <input 
            v-model="newPassword2" 
            type="password" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            required
            minlength="8"
          >
        </div>
        
        <button 
          type="submit" 
          class="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition"
          :disabled="submitting"
        >
          {{ submitting ? 'Сохранение...' : 'Сохранить новый пароль' }}
        </button>
        
        <p v-if="formError" class="mt-3 text-red-500 text-sm">{{ formError }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const loading = ref(true)
const error = ref(false)
const success = ref(false)
const submitting = ref(false)
const errorMessage = ref('')
const formError = ref('')
const newPassword = ref('')
const newPassword2 = ref('')

onMounted(async () => {
  try {
    const { uidb64, token } = route.params
    console.log('📡 Проверка ссылки сброса:', uidb64, token)
    
    // Проверяем, что ссылка валидна (делаем GET запрос для проверки)
    // Можно сразу показать форму
    loading.value = false
  } catch (e) {
    console.error('❌ Ошибка:', e)
    error.value = true
    errorMessage.value = 'Неверная ссылка для сброса пароля'
    loading.value = false
  }
})

const resetPassword = async () => {
  if (!newPassword.value || !newPassword2.value) {
    formError.value = 'Заполните все поля'
    return
  }
  
  if (newPassword.value !== newPassword2.value) {
    formError.value = 'Пароли не совпадают'
    return
  }
  
  if (newPassword.value.length < 8) {
    formError.value = 'Пароль должен содержать минимум 8 символов'
    return
  }
  
  submitting.value = true
  formError.value = ''
  
  try {
    const { uidb64, token } = route.params
    
    const res = await fetch(`${API_URL}/auth/password-reset/${uidb64}/${token}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        new_password: newPassword.value,
        new_password2: newPassword2.value
      })
    })
    
    const data = await res.json()
    
    if (res.ok) {
      success.value = true
    } else {
      formError.value = data.detail || 'Ошибка сброса пароля'
    }
  } catch (e) {
    console.error('❌ Ошибка:', e)
    formError.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}
</script>