<!-- frontend/pages/settings/documents.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4 pb-16">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-indigo-500 dark:text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
        </svg>
        Документы
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
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут управлять документами.</p>
    </div>

    <template v-else>
      <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow mb-6">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">Список документов ({{ documents.length }})</h2>
          <button
            v-if="!formVisible"
            @click="openCreateForm"
            class="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-indigo-500 to-indigo-600 text-white rounded-xl hover:from-indigo-600 hover:to-indigo-700 transition-all duration-300 text-sm font-medium"
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

        <p v-else-if="documents.length === 0" class="text-gray-500 dark:text-gray-400 text-sm py-4">
          Документов пока нет. Нажмите «Добавить», чтобы загрузить первый.
        </p>

        <div v-else class="space-y-2">
          <div
            v-for="doc in documents"
            :key="doc.id"
            class="flex items-center gap-3 p-3 rounded-xl border border-gray-100 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700/40 transition"
          >
            <div
              class="w-10 h-10 rounded-lg flex items-center justify-center flex-shrink-0 text-white text-[10px] font-bold uppercase"
              :class="extColor(doc.file_ext)"
            >
              {{ doc.file_ext || 'doc' }}
            </div>
            <div class="flex-1 min-w-0">
              <p class="font-medium text-gray-800 dark:text-gray-200 truncate">
                {{ doc.title }}
                <span v-if="!doc.is_published" class="ml-2 text-xs text-amber-600 dark:text-amber-400">(скрыт)</span>
              </p>
              <p class="text-sm text-gray-500 dark:text-gray-400 truncate">
                {{ doc.description || '—' }}<template v-if="doc.file_size"> · {{ formatSize(doc.file_size) }}</template>
              </p>
            </div>
            <a
              :href="doc.file_display"
              target="_blank"
              rel="noopener"
              class="px-3 py-1.5 text-sm text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition"
            >
              Открыть
            </a>
            <button
              @click="openEditForm(doc)"
              class="px-3 py-1.5 text-sm text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/20 rounded-lg transition"
            >
              Изменить
            </button>
            <button
              @click="removeDocument(doc)"
              class="px-3 py-1.5 text-sm text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
            >
              Удалить
            </button>
          </div>
        </div>
      </div>

      <div v-if="formVisible" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 mb-4">
          {{ editingId ? 'Редактировать документ' : 'Новый документ' }}
        </h2>

        <form @submit.prevent="submitForm" enctype="multipart/form-data" class="space-y-4">
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Название документа <span class="text-red-500">*</span></label>
            <input v-model="form.title" type="text" required placeholder="Устав учреждения"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
          </div>

          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Краткое описание</label>
            <input v-model="form.description" type="text" placeholder="Необязательно: пара слов о документе"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
          </div>

          <!-- Файл -->
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
              <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"/>
              </svg>
              Файл документа {{ editingId ? '' : '*' }}
            </label>

            <div v-if="form.file_display && !fileRemoved && !filePreviewName" class="mb-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
              <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Текущий файл:</p>
              <div class="flex items-center gap-3">
                <a :href="form.file_display" target="_blank" rel="noopener" class="text-sm text-indigo-600 dark:text-indigo-400 hover:underline truncate">
                  {{ form.title }}.{{ form.file_ext }}
                </a>
                <button
                  type="button"
                  @click="fileRemoved = true"
                  class="px-3 py-1.5 text-sm text-red-500 hover:text-red-700 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition flex-shrink-0"
                >
                  Удалить
                </button>
              </div>
            </div>

            <div class="flex flex-col gap-2">
              <input
                type="file"
                accept=".pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt,.odt"
                @change="onFileSelected"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100 dark:file:bg-indigo-900/30 dark:file:text-indigo-400"
              />
              <div class="flex items-center gap-2">
                <span class="text-gray-400 dark:text-gray-500 text-sm">или</span>
                <input
                  v-model="form.file_url"
                  type="url"
                  placeholder="https://example.com/document.pdf"
                  class="flex-1 border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
                  @input="onUrlInput"
                />
              </div>
            </div>
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Форматы: PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT, ODT. Максимум 20 МБ.</p>

            <div v-if="filePreviewName" class="mt-2 flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
              <div class="flex-1 min-w-0">
                <p class="text-sm font-medium text-gray-700 dark:text-gray-300 truncate">{{ filePreviewName }}</p>
                <p class="text-xs text-gray-400 dark:text-gray-500">{{ file ? formatSize(file.size) : 'Загружено по URL' }}</p>
              </div>
              <button
                type="button"
                @click="clearFile"
                class="px-3 py-1.5 text-sm text-red-500 hover:text-red-700 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
              >
                Удалить
              </button>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Порядок сортировки</label>
              <input v-model.number="form.order" type="number" min="0"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" />
            </div>
            <div class="flex items-end pb-2">
              <label class="flex items-center gap-2 cursor-pointer">
                <input v-model="form.is_published" type="checkbox" class="w-4 h-4 text-indigo-500 rounded focus:ring-2 focus:ring-indigo-500 cursor-pointer" />
                <span class="text-gray-700 dark:text-gray-300 text-sm">Опубликовано (видно на сайте)</span>
              </label>
            </div>
          </div>

          <div class="flex flex-wrap gap-3 pt-4 border-t border-gray-100 dark:border-gray-700">
            <button type="submit" :disabled="submitting"
              class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-indigo-500 to-indigo-600 text-white rounded-xl hover:from-indigo-600 hover:to-indigo-700 transition-all duration-300 font-medium shadow-lg shadow-indigo-500/25 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed">
              {{ submitting ? 'Сохранение...' : (editingId ? 'Сохранить изменения' : 'Добавить документ') }}
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

definePageMeta({
  middleware: ['auth', 'editor']
})

useSeoMeta({
  title: 'Настройки: документы'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()

const documents = ref([])
const loading = ref(true)
const submitting = ref(false)
const error = ref('')
const success = ref('')

const formVisible = ref(false)
const editingId = ref(null)
const file = ref(null)
const filePreviewName = ref('')
const fileRemoved = ref(false)

const ALLOWED_EXT = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'odt']

const emptyForm = () => ({
  title: '',
  description: '',
  file_url: '',
  file_display: '',
  file_ext: '',
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

const extColor = (ext) => {
  if (ext === 'pdf') return 'bg-red-500'
  if (ext === 'doc' || ext === 'docx') return 'bg-blue-500'
  if (ext === 'xls' || ext === 'xlsx') return 'bg-green-600'
  if (ext === 'ppt' || ext === 'pptx') return 'bg-orange-500'
  return 'bg-gray-500'
}

const formatSize = (bytes) => {
  if (bytes < 1024) return bytes + ' Б'
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(0) + ' КБ'
  return (bytes / (1024 * 1024)).toFixed(1) + ' МБ'
}

const onFileSelected = (event) => {
  const f = event.target.files[0]
  if (!f) return
  const ext = f.name.includes('.') ? f.name.split('.').pop().toLowerCase() : ''
  if (!ALLOWED_EXT.includes(ext)) {
    alert('Неподдерживаемый формат. Разрешены: ' + ALLOWED_EXT.join(', ').toUpperCase())
    event.target.value = ''
    return
  }
  if (f.size > 20 * 1024 * 1024) {
    alert('Файл слишком большой. Максимум 20 МБ.')
    event.target.value = ''
    return
  }
  file.value = f
  filePreviewName.value = f.name
  form.value.file_url = ''
  fileRemoved.value = false
}

const onUrlInput = () => {
  const url = form.value.file_url.trim()
  if (url && isValidUrl(url)) {
    file.value = null
    filePreviewName.value = url.split('/').pop().split('?')[0] || 'Документ по ссылке'
    fileRemoved.value = false
  } else if (!url && !file.value) {
    filePreviewName.value = ''
  }
}

const clearFile = () => {
  file.value = null
  filePreviewName.value = ''
  form.value.file_url = ''
}

const loadDocuments = async () => {
  loading.value = true
  try {
    const res = await apiFetch(`${API_URL}/about/documents/`)
    if (res.ok) documents.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки:', e)
  } finally {
    loading.value = false
  }
}

const openCreateForm = () => {
  editingId.value = null
  form.value = emptyForm()
  file.value = null
  filePreviewName.value = ''
  fileRemoved.value = false
  error.value = ''
  formVisible.value = true
}

const openEditForm = (doc) => {
  editingId.value = doc.id
  form.value = {
    title: doc.title || '',
    description: doc.description || '',
    file_url: doc.file_url || '',
    file_display: doc.file_display || '',
    file_ext: doc.file_ext || '',
    order: doc.order ?? 0,
    is_published: doc.is_published !== undefined ? doc.is_published : true
  }
  file.value = null
  filePreviewName.value = ''
  fileRemoved.value = false
  error.value = ''
  formVisible.value = true
}

const closeForm = () => {
  formVisible.value = false
  editingId.value = null
  error.value = ''
}

const submitForm = async () => {
  if (!form.value.title) {
    error.value = 'Заполните название документа'
    return
  }
  if (!editingId.value && !file.value && !(form.value.file_url && isValidUrl(form.value.file_url))) {
    error.value = 'Выберите файл или укажите ссылку на него'
    return
  }

  submitting.value = true
  error.value = ''

  try {
    const formData = new FormData()
    formData.append('title', form.value.title)
    formData.append('description', form.value.description || '')
    formData.append('order', form.value.order ?? 0)
    formData.append('is_published', form.value.is_published ? 'true' : 'false')

    if (fileRemoved.value) {
      formData.append('file_url', '')
    } else if (file.value) {
      formData.append('file', file.value)
    } else if (form.value.file_url && isValidUrl(form.value.file_url)) {
      formData.append('file_url', form.value.file_url)
    }

    const url = editingId.value ? `${API_URL}/about/documents/${editingId.value}/` : `${API_URL}/about/documents/`
    const res = await apiFetch(url, { method: editingId.value ? 'PUT' : 'POST', body: formData })

    if (res.ok) {
      success.value = editingId.value ? 'Документ обновлён!' : 'Документ добавлен!'
      setTimeout(() => { success.value = '' }, 3000)
      closeForm()
      await loadDocuments()
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

const removeDocument = async (doc) => {
  if (!confirm(`Удалить документ «${doc.title}»?`)) return
  try {
    const res = await apiFetch(`${API_URL}/about/documents/${doc.id}/`, { method: 'DELETE' })
    if (res.ok || res.status === 204) {
      success.value = 'Документ удалён.'
      setTimeout(() => { success.value = '' }, 3000)
      await loadDocuments()
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
  if (authStore.isEditor) await loadDocuments()
})
</script>
