<!-- frontend/pages/settings/staff.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4 pb-16">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-green-500 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/>
        </svg>
        Сотрудники
      </h1>
      <NuxtLink
        to="/settings"
        class="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 hover:-translate-y-0.5"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
        </svg>
        Все настройки
      </NuxtLink>
    </div>

    <div v-if="!authStore.isEditor" class="bg-white dark:bg-gray-800 p-8 rounded-lg shadow text-center py-20">
      <svg class="w-24 h-24 mx-auto text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
      </svg>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут управлять сотрудниками.</p>
    </div>

    <template v-else>
      <!-- Список -->
      <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow mb-6">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">Список сотрудников ({{ staff.length }})</h2>
          <button
            v-if="!formVisible"
            @click="openCreateForm"
            class="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-green-500 to-green-600 text-white rounded-xl hover:from-green-600 hover:to-green-700 transition-all duration-300 text-sm font-medium"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
            </svg>
            Добавить
          </button>
        </div>

        <div v-if="loading" class="space-y-2">
          <div v-for="n in 4" :key="n" class="h-14 bg-gray-100 dark:bg-gray-700 rounded-lg animate-pulse"></div>
        </div>

        <p v-else-if="staff.length === 0" class="text-gray-500 dark:text-gray-400 text-sm py-4">
          Сотрудников пока нет. Нажмите «Добавить», чтобы создать первую карточку.
        </p>

        <div v-else class="space-y-2">
          <div
            v-for="member in staff"
            :key="member.id"
            class="flex items-center gap-3 p-3 rounded-xl border border-gray-100 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700/40 transition"
          >
            <img
              v-if="member.display_photo"
              :src="member.display_photo"
              :alt="member.full_name"
              class="w-11 h-11 rounded-full object-cover border border-gray-200 dark:border-gray-600 flex-shrink-0"
            />
            <div v-else class="w-11 h-11 rounded-full bg-gray-200 dark:bg-gray-600 flex items-center justify-center text-gray-500 dark:text-gray-300 font-bold flex-shrink-0">
              {{ member.full_name?.charAt(0) }}
            </div>
            <div class="flex-1 min-w-0">
              <p class="font-medium text-gray-800 dark:text-gray-200 truncate">
                {{ member.full_name }}
                <span v-if="!member.is_published" class="ml-2 text-xs text-amber-600 dark:text-amber-400">(скрыт)</span>
              </p>
              <p class="text-sm text-gray-500 dark:text-gray-400 truncate">{{ member.position }} · {{ member.category_display }}</p>
            </div>
            <button
              @click="openEditForm(member)"
              class="px-3 py-1.5 text-sm text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/20 rounded-lg transition"
            >
              Изменить
            </button>
            <button
              @click="removeMember(member)"
              class="px-3 py-1.5 text-sm text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
            >
              Удалить
            </button>
          </div>
        </div>
      </div>

      <!-- Форма -->
      <div v-if="formVisible" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 mb-4">
          {{ editingId ? 'Редактировать сотрудника' : 'Новый сотрудник' }}
        </h2>

        <form @submit.prevent="submitForm" enctype="multipart/form-data" class="space-y-4">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">ФИО <span class="text-red-500">*</span></label>
              <input v-model="form.full_name" type="text" required placeholder="Иванова Мария Петровна"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-green-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
            </div>
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Должность <span class="text-red-500">*</span></label>
              <input v-model="form.position" type="text" required placeholder="Директор"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-green-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Категория <span class="text-red-500">*</span></label>
              <select v-model="form.category" required
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-green-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200">
                <option value="aup">Административно-управленческий персонал</option>
                <option value="main">Основной персонал</option>
                <option value="technical">Технический персонал</option>
                <option value="auxiliary">Вспомогательный персонал</option>
              </select>
            </div>
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Пользователь сайта (необязательно)</label>
              <select v-model="form.user"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-green-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200">
                <option :value="null">— Не привязан —</option>
                <option v-for="u in users" :key="u.id" :value="u.id">
                  {{ u.first_name || u.last_name ? `${u.first_name} ${u.last_name}`.trim() + ` (@${u.username})` : `@${u.username}` }}
                </option>
              </select>
              <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Карточка станет ссылкой на профиль пользователя.</p>
            </div>
          </div>

          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">О сотруднике</label>
            <textarea v-model="form.bio" rows="3" placeholder="Краткая информация (необязательно)"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-green-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"></textarea>
          </div>

          <ImageField
            label="Фото сотрудника"
            hint="До 5MB. Если не указано и пользователь привязан — берётся его аватар."
            :current-url="form.display_photo"
            v-model:file="photoFile"
            v-model:url="form.photo_url"
            @remove="photoRemoved = true"
          />

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Порядок сортировки</label>
              <input v-model.number="form.order" type="number" min="0"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-green-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
            </div>
            <div class="flex items-end pb-2">
              <label class="flex items-center gap-2 cursor-pointer">
                <input v-model="form.is_published" type="checkbox" class="w-4 h-4 text-green-500 rounded focus:ring-2 focus:ring-green-500 cursor-pointer" />
                <span class="text-gray-700 dark:text-gray-300 text-sm">Опубликовано (видно на сайте)</span>
              </label>
            </div>
          </div>

          <div class="flex flex-wrap gap-3 pt-4 border-t border-gray-100 dark:border-gray-700">
            <button type="submit" :disabled="submitting"
              class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-green-500 to-green-600 text-white rounded-xl hover:from-green-600 hover:to-green-700 transition-all duration-300 font-medium shadow-lg shadow-green-500/25 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed">
              {{ submitting ? 'Сохранение...' : (editingId ? 'Сохранить изменения' : 'Добавить сотрудника') }}
            </button>
            <button type="button" @click="closeForm"
              class="px-6 py-3 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 font-medium">
              Отмена
            </button>
          </div>

          <p v-if="error" class="text-red-500 text-sm">{{ error }}</p>
        </form>
      </div>

      <p v-if="success" class="mt-4 text-green-500 text-sm">{{ success }}</p>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import ImageField from '~/components/common/ImageField.vue'

definePageMeta({
  middleware: ['auth', 'editor']
})

useSeoMeta({
  title: 'Настройки: сотрудники'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()

const staff = ref([])
const users = ref([])
const loading = ref(true)
const submitting = ref(false)
const error = ref('')
const success = ref('')

const formVisible = ref(false)
const editingId = ref(null)
const photoFile = ref(null)
const photoRemoved = ref(false)

const emptyForm = () => ({
  full_name: '',
  position: '',
  category: 'main',
  user: null,
  bio: '',
  photo_url: '',
  display_photo: '',
  order: 0,
  is_published: true
})

const form = ref(emptyForm())

const isValidUrl = (string) => {
  try {
    const u = new URL(string)
    return u.protocol === 'http:' || u.protocol === 'https:'
  } catch (_) {
    return false
  }
}

const loadStaff = async () => {
  loading.value = true
  try {
    const res = await apiFetch(`${API_URL}/about/staff/`)
    if (res.ok) staff.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки сотрудников:', e)
  } finally {
    loading.value = false
  }
}

const loadUsers = async () => {
  try {
    const res = await apiFetch(`${API_URL}/auth/users/`)
    if (res.ok) users.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки пользователей:', e)
  }
}

const openCreateForm = () => {
  editingId.value = null
  form.value = emptyForm()
  photoFile.value = null
  photoRemoved.value = false
  error.value = ''
  formVisible.value = true
}

const openEditForm = (member) => {
  editingId.value = member.id
  form.value = {
    full_name: member.full_name || '',
    position: member.position || '',
    category: member.category || 'main',
    user: member.user_id || null,
    bio: member.bio || '',
    photo_url: member.photo_url || '',
    display_photo: member.display_photo || '',
    order: member.order ?? 0,
    is_published: member.is_published !== undefined ? member.is_published : true
  }
  photoFile.value = null
  photoRemoved.value = false
  error.value = ''
  formVisible.value = true
}

const closeForm = () => {
  formVisible.value = false
  editingId.value = null
  error.value = ''
}

const submitForm = async () => {
  if (!form.value.full_name || !form.value.position) {
    error.value = 'Заполните ФИО и должность'
    return
  }

  submitting.value = true
  error.value = ''

  try {
    const formData = new FormData()
    formData.append('full_name', form.value.full_name)
    formData.append('position', form.value.position)
    formData.append('category', form.value.category)
    if (form.value.user) formData.append('user', form.value.user)
    else formData.append('user', '')
    formData.append('bio', form.value.bio || '')
    formData.append('order', form.value.order ?? 0)
    formData.append('is_published', form.value.is_published ? 'true' : 'false')

    if (photoRemoved.value) {
      formData.append('photo_url', '')
    } else if (photoFile.value) {
      formData.append('photo', photoFile.value)
    } else if (form.value.photo_url && isValidUrl(form.value.photo_url)) {
      formData.append('photo_url', form.value.photo_url)
    }

    const url = editingId.value ? `${API_URL}/about/staff/${editingId.value}/` : `${API_URL}/about/staff/`
    const res = await apiFetch(url, { method: editingId.value ? 'PUT' : 'POST', body: formData })

    if (res.ok) {
      success.value = editingId.value ? 'Сотрудник обновлён!' : 'Сотрудник добавлен!'
      setTimeout(() => { success.value = '' }, 3000)
      closeForm()
      await loadStaff()
    } else {
      const data = await res.json().catch(() => ({}))
      error.value = data.detail || 'Ошибка сохранения'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}

const removeMember = async (member) => {
  if (!confirm(`Удалить сотрудника «${member.full_name}»?`)) return
  try {
    const res = await apiFetch(`${API_URL}/about/staff/${member.id}/`, { method: 'DELETE' })
    if (res.ok || res.status === 204) {
      success.value = 'Сотрудник удалён.'
      setTimeout(() => { success.value = '' }, 3000)
      await loadStaff()
    } else {
      error.value = 'Ошибка удаления'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  }
}

onMounted(async () => {
  authStore.restoreAuth()
  if (authStore.isEditor) {
    await Promise.all([loadStaff(), loadUsers()])
  }
})
</script>
