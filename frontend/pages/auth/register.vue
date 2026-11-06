<template>
  <div class="max-w-md mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">Регистрация</h1>
    
    <form @submit.prevent="register">
      <!-- Имя пользователя -->
      <UiInput 
        v-model="username"
        label="Имя пользователя"
        placeholder="Введите имя пользователя"
        required
      />
      
      <!-- Email -->
      <UiInput 
        v-model="email"
        label="Email"
        type="email"
        placeholder="example@mail.com"
        required
      />
      
      <!-- Пароль -->
      <UiInput 
        v-model="password"
        label="Пароль"
        type="password"
        placeholder="Введите пароль"
        required
        hint="Минимум 8 символов"
      />
      
      <!-- Подтверждение пароля -->
      <UiInput 
        v-model="password2"
        label="Подтвердите пароль"
        type="password"
        placeholder="Повторите пароль"
        required
      />
      
      <UiButton 
        type="submit" 
        variant="primary"
        :disabled="loading"
        full-width
      >
        {{ loading ? 'Регистрация...' : 'Зарегистрироваться' }}
      </UiButton>
      
      <p v-if="error" class="mt-4 text-red-500 text-sm">{{ error }}</p>
      <p v-if="successMessage" class="mt-4 text-green-500 text-sm">{{ successMessage }}</p>
      
      <p class="mt-4 text-center text-gray-600 dark:text-gray-400">
        Уже есть аккаунт? <NuxtLink to="/auth/login" class="text-blue-500 dark:text-blue-400 hover:underline">Войти</NuxtLink>
      </p>
    </form>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase

const router = useRouter()

const username = ref('')
const email = ref('')
const password = ref('')
const password2 = ref('')
const loading = ref(false)
const error = ref('')
const successMessage = ref('')

const register = async () => {
  if (!username.value || !email.value || !password.value || !password2.value) {
    error.value = 'Заполните все поля'
    return
  }
  
  if (password.value !== password2.value) {
    error.value = 'Пароли не совпадают'
    return
  }
  
  if (password.value.length < 8) {
    error.value = 'Пароль должен содержать минимум 8 символов'
    return
  }
  
  loading.value = true
  error.value = ''
  successMessage.value = ''
  
  try {
    const res = await fetch(`${API_URL}/auth/register/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username.value,
        email: email.value,
        password: password.value,
        password2: password2.value
      })
    })
    
    const data = await res.json()
    
    if (res.ok) {
      successMessage.value = '✅ Регистрация успешна! Теперь вы можете войти.'
      error.value = ''
      username.value = ''
      email.value = ''
      password.value = ''
      password2.value = ''
      
      setTimeout(() => {
        router.push('/auth/login')
      }, 2000)
    } else {
      if (data.email) {
        error.value = `Email: ${data.email.join(', ')}`
      } else if (data.username) {
        error.value = `Имя пользователя: ${data.username.join(', ')}`
      } else if (data.password) {
        error.value = `Пароль: ${data.password.join(', ')}`
      } else if (data.password2) {
        error.value = `Подтверждение пароля: ${data.password2.join(', ')}`
      } else if (data.detail) {
        error.value = data.detail
      } else {
        error.value = JSON.stringify(data)
      }
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    loading.value = false
  }
}
</script>