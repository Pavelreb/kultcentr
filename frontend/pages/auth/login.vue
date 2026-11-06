<template>
  <div class="max-w-md mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">Вход</h1>
    
    <form @submit.prevent="login">
      <!-- Имя пользователя -->
      <UiInput 
        v-model="username"
        label="Имя пользователя"
        placeholder="Введите имя пользователя"
        required
      />
      
      <!-- Пароль -->
      <UiInput 
        v-model="password"
        label="Пароль"
        type="password"
        placeholder="Введите пароль"
        required
      />
      
      <UiButton 
        type="submit" 
        variant="primary"
        :disabled="loading"
        full-width
      >
        {{ loading ? 'Вход...' : 'Войти' }}
      </UiButton>
      
      <p v-if="error" class="mt-4 text-red-500 text-sm">{{ error }}</p>
      
      <p class="mt-4 text-center text-gray-600 dark:text-gray-400">
        <button 
          @click="showResetPassword = !showResetPassword"
          class="text-blue-500 dark:text-blue-400 hover:underline"
          type="button"
        >
          {{ showResetPassword ? 'Скрыть' : 'Забыли пароль?' }}
        </button>
      </p>
      
      <p class="mt-2 text-center text-gray-600 dark:text-gray-400">
        Нет аккаунта? <NuxtLink to="/auth/register" class="text-blue-500 dark:text-blue-400 hover:underline">Регистрация</NuxtLink>
      </p>
      
      <div v-if="showResetPassword" class="mt-6 pt-6 border-t border-gray-200 dark:border-gray-700">
        <h2 class="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-3">Восстановление пароля</h2>
        <p class="text-sm text-gray-500 dark:text-gray-400 mb-4">
          Введите email или имя пользователя, и мы отправим ссылку для сброса пароля.
        </p>
        
        <form @submit.prevent="requestPasswordReset">
          <UiInput 
            v-model="resetEmail"
            label="Email или имя пользователя"
            placeholder="email@example.com или username"
            required
          />
          
          <UiButton 
            type="submit" 
            variant="primary"
            :disabled="resetLoading"
            full-width
          >
            {{ resetLoading ? 'Отправка...' : 'Отправить ссылку' }}
          </UiButton>
          
          <p v-if="resetSuccess" class="mt-3 text-green-500 text-sm">{{ resetSuccess }}</p>
          <p v-if="resetError" class="mt-3 text-red-500 text-sm">{{ resetError }}</p>
        </form>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase

const authStore = useAuthStore()
const router = useRouter()

const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')

const showResetPassword = ref(false)
const resetEmail = ref('')
const resetLoading = ref(false)
const resetSuccess = ref('')
const resetError = ref('')

const login = async () => {
  if (!username.value || !password.value) return
  
  loading.value = true
  error.value = ''
  
  try {
    const res = await fetch(`${API_URL}/auth/login/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value
      })
    })
    
    if (res.ok) {
      const data = await res.json()
      
      const userRes = await fetch(`${API_URL}/auth/users/me/`, {
        headers: {
          'Authorization': `Bearer ${data.access}`
        }
      })
      
      if (userRes.ok) {
        const user = await userRes.json()
        authStore.setAuth(user, data.access, data.refresh)
        router.push('/')
      }
    } else {
      const data = await res.json()
      error.value = data.detail || 'Неверное имя пользователя или пароль'
    }
  } catch (e) {
    error.value = 'Ошибка подключения к серверу'
    console.error(e)
  } finally {
    loading.value = false
  }
}

const requestPasswordReset = async () => {
  if (!resetEmail.value.trim()) {
    resetError.value = 'Введите email или имя пользователя'
    return
  }
  
  resetLoading.value = true
  resetError.value = ''
  resetSuccess.value = ''
  
  try {
    const isEmail = resetEmail.value.includes('@')
    const requestBody = isEmail 
      ? { email: resetEmail.value } 
      : { username: resetEmail.value }
    
    const res = await fetch(`${API_URL}/auth/password-reset/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestBody)
    })
    
    const data = await res.json()
    
    if (res.ok) {
      resetSuccess.value = data.detail || 'Ссылка отправлена на email'
      resetEmail.value = ''
      setTimeout(() => {
        showResetPassword.value = false
        resetSuccess.value = ''
      }, 5000)
    } else {
      resetError.value = data.detail || data.message || 'Ошибка отправки'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    resetError.value = 'Ошибка подключения к серверу'
  } finally {
    resetLoading.value = false
  }
}
</script>