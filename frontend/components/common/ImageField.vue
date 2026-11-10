<!-- frontend/components/common/ImageField.vue -->
<template>
  <div>
    <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
      <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
      </svg>
      {{ label }}
    </label>

    <!-- Текущее изображение -->
    <div v-if="currentUrl && !removed && !preview" class="mb-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
      <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Текущее изображение:</p>
      <div class="flex items-center gap-3">
        <img :src="currentUrl" :alt="label" class="w-20 h-20 rounded-lg object-cover border border-gray-200 dark:border-gray-600" />
        <button
          type="button"
          @click="onRemoveCurrent"
          class="px-3 py-1.5 text-sm text-red-500 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
        >
          Удалить
        </button>
      </div>
    </div>

    <div class="flex flex-col gap-2">
      <input
        type="file"
        accept="image/jpeg,image/png,image/gif,image/webp"
        @change="onFileSelected"
        class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-teal-50 file:text-teal-700 hover:file:bg-teal-100 dark:file:bg-teal-900/30 dark:file:text-teal-400"
      />
      <div class="flex items-center gap-2">
        <span class="text-gray-400 dark:text-gray-500 text-sm">или</span>
        <input
          :value="url"
          @input="onUrlInput"
          type="url"
          placeholder="https://example.com/image.jpg"
          class="flex-1 border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-teal-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
        />
      </div>
    </div>
    <p v-if="hint" class="text-xs text-gray-400 dark:text-gray-500 mt-1">{{ hint }}</p>

    <!-- Превью нового изображения -->
    <div v-if="preview" class="mt-2 flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl border border-gray-200 dark:border-gray-700">
      <img :src="preview" :alt="label" class="w-20 h-20 rounded-lg object-cover border border-gray-200 dark:border-gray-600" />
      <div class="flex-1 min-w-0">
        <p class="text-sm font-medium text-gray-700 dark:text-gray-300 truncate">
          {{ file ? file.name : 'Изображение по ссылке' }}
        </p>
        <p class="text-xs text-gray-400 dark:text-gray-500">
          {{ file ? (file.size / 1024).toFixed(0) + ' KB' : 'Загружено по URL' }}
        </p>
      </div>
      <button
        type="button"
        @click="clearSelection"
        class="px-3 py-1.5 text-sm text-red-500 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
      >
        Удалить
      </button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  label: { type: String, default: 'Изображение' },
  hint: { type: String, default: '' },
  currentUrl: { type: String, default: '' },
  file: { type: [Object, null], default: null },
  url: { type: String, default: '' }
})

const emit = defineEmits(['update:file', 'update:url', 'remove'])

const preview = ref('')
const removed = ref(false)

watch(() => props.currentUrl, () => {
  if (props.currentUrl) removed.value = false
})

const isValidUrl = (string) => {
  try {
    const u = new URL(string)
    return u.protocol === 'http:' || u.protocol === 'https:'
  } catch (_) {
    return false
  }
}

const onFileSelected = (event) => {
  const f = event.target.files[0]
  if (!f) return
  if (f.size > 5 * 1024 * 1024) {
    alert('Файл слишком большой. Максимум 5MB.')
    event.target.value = ''
    return
  }
  const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
  if (!allowedTypes.includes(f.type)) {
    alert('Неподдерживаемый формат. Используйте JPEG, PNG, GIF или WEBP.')
    event.target.value = ''
    return
  }
  emit('update:file', f)
  emit('update:url', '')
  preview.value = URL.createObjectURL(f)
  removed.value = false
}

const onUrlInput = (event) => {
  const value = event.target.value
  emit('update:url', value)
  if (value && isValidUrl(value)) {
    emit('update:file', null)
    preview.value = value
    removed.value = false
  } else if (!value) {
    if (!props.file) preview.value = ''
  }
}

const onRemoveCurrent = () => {
  removed.value = true
  preview.value = ''
  emit('update:file', null)
  emit('update:url', '')
  emit('remove')
}

const clearSelection = () => {
  preview.value = ''
  emit('update:file', null)
  emit('update:url', '')
}
</script>
