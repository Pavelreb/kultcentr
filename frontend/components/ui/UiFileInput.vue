<template>
  <div class="mb-4">
    <label v-if="label" class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>
    
    <div 
      class="relative border-2 border-dashed rounded-lg p-6 transition bg-white dark:bg-gray-700"
      :class="[
        isDragging ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20' : 'border-gray-300 dark:border-gray-600',
        disabled ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer hover:border-blue-400'
      ]"
      @dragover.prevent="isDragging = true"
      @dragleave.prevent="isDragging = false"
      @drop.prevent="handleDrop"
      @click="triggerFileInput"
    >
      <div class="text-center">
        <div class="text-4xl mb-2">
          {{ multiple ? '📁' : '📄' }}
        </div>
        <p class="text-gray-600 dark:text-gray-300">
          {{ multiple ? 'Перетащите файлы сюда или кликните для выбора' : 'Перетащите файл сюда или кликните для выбора' }}
        </p>
        <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">
          {{ accept ? `Поддерживаемые форматы: ${accept}` : 'Любые форматы' }}
          {{ maxSize ? ` • Максимум: ${formatFileSize(maxSize)}` : '' }}
        </p>
        <p v-if="multiple" class="text-sm text-gray-400 dark:text-gray-500">
          Можно выбрать несколько файлов
        </p>
      </div>
      
      <input
        ref="fileInputRef"
        type="file"
        :accept="accept"
        :multiple="multiple"
        :disabled="disabled"
        class="absolute inset-0 opacity-0 cursor-pointer"
        @change="handleFileSelect"
      />
    </div>
    
    <!-- Предпросмотр файлов -->
    <div v-if="filePreviews.length > 0" class="mt-3">
      <div class="flex flex-wrap gap-2">
        <div 
          v-for="(file, index) in filePreviews" 
          :key="index"
          class="relative group"
        >
          <div v-if="file.preview" class="relative">
            <img 
              :src="file.preview" 
              :alt="file.name"
              class="w-20 h-20 object-cover rounded-lg border border-gray-200 dark:border-gray-600"
            />
            <button
              v-if="!disabled && removable"
              type="button"
              class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-5 h-5 flex items-center justify-center hover:bg-red-600 transition text-xs opacity-0 group-hover:opacity-100"
              @click="removeFile(index)"
            >
              ✕
            </button>
          </div>
          
          <div v-else class="relative">
            <div class="w-20 h-20 bg-gray-100 dark:bg-gray-600 rounded-lg border border-gray-200 dark:border-gray-600 flex items-center justify-center">
              <span class="text-3xl">📄</span>
            </div>
            <button
              v-if="!disabled && removable"
              type="button"
              class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-5 h-5 flex items-center justify-center hover:bg-red-600 transition text-xs opacity-0 group-hover:opacity-100"
              @click="removeFile(index)"
            >
              ✕
            </button>
          </div>
          
          <p class="text-xs text-gray-500 dark:text-gray-400 mt-1 truncate max-w-[80px] text-center">
            {{ file.name }}
          </p>
        </div>
      </div>
      
      <p v-if="multiple && filePreviews.length > 0" class="text-xs text-gray-400 dark:text-gray-500 mt-2">
        Выбрано файлов: {{ filePreviews.length }}
      </p>
    </div>
    
    <p v-if="error" class="text-red-500 text-sm mt-1">{{ error }}</p>
    <p v-if="hint" class="text-gray-400 dark:text-gray-500 text-sm mt-1">{{ hint }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: [File, Array, null],
    default: null
  },
  label: {
    type: String,
    default: ''
  },
  hint: {
    type: String,
    default: ''
  },
  error: {
    type: String,
    default: ''
  },
  required: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  },
  multiple: {
    type: Boolean,
    default: false
  },
  accept: {
    type: String,
    default: ''
  },
  maxSize: {
    type: Number,
    default: 5 * 1024 * 1024
  },
  removable: {
    type: Boolean,
    default: true
  }
})

const emit = defineEmits(['update:modelValue', 'change', 'remove'])

const fileInputRef = ref(null)
const isDragging = ref(false)
const filePreviews = ref([])

const formatFileSize = (bytes) => {
  if (bytes === 0) return '0 Б'
  const k = 1024
  const sizes = ['Б', 'КБ', 'МБ', 'ГБ']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i]
}

const validateFileSize = (file) => {
  if (props.maxSize && file.size > props.maxSize) {
    return {
      valid: false,
      message: `Файл "${file.name}" слишком большой. Максимум: ${formatFileSize(props.maxSize)}`
    }
  }
  return { valid: true, message: '' }
}

const isImageFile = (file) => {
  if (!file) return false
  if (file.type && file.type.startsWith('image/')) return true
  if (file.name) {
    const ext = file.name.split('.').pop().toLowerCase()
    return ['jpg', 'jpeg', 'png', 'gif', 'webp', 'svg', 'bmp', 'ico'].includes(ext)
  }
  return false
}

const createPreview = (file, callback) => {
  if (isImageFile(file)) {
    try {
      const reader = new FileReader()
      reader.onload = (e) => {
        const fileData = {
          file: file,
          preview: e.target.result,
          name: file.name,
          type: file.type,
          size: file.size
        }
        callback(fileData)
      }
      reader.readAsDataURL(file)
    } catch (e) {
      console.error('Ошибка создания превью:', e)
      callback(file)
    }
  } else {
    callback(file)
  }
}

const handleFileSelect = (event) => {
  const files = event.target.files
  if (!files || files.length === 0) return
  
  const filesArray = Array.from(files)
  processFiles(filesArray)
  event.target.value = ''
}

const handleDrop = (event) => {
  isDragging.value = false
  const files = event.dataTransfer.files
  if (!files || files.length === 0) return
  
  const filesArray = Array.from(files)
  processFiles(filesArray)
}

const processFiles = (filesArray) => {
  const errors = []
  
  if (!props.multiple) {
    filePreviews.value = []
  }
  
  let processedCount = 0
  
  for (const file of filesArray) {
    const sizeCheck = validateFileSize(file)
    if (!sizeCheck.valid) {
      errors.push(sizeCheck.message)
      continue
    }
    
    createPreview(file, (fileData) => {
      if (props.multiple) {
        filePreviews.value = [...filePreviews.value, fileData]
      } else {
        filePreviews.value = [fileData]
      }
      processedCount++
      
      if (processedCount === filesArray.length) {
        updateModel()
        emit('change', filePreviews.value)
      }
    })
  }
  
  if (errors.length > 0) {
    alert(errors.join('\n'))
  }
  
  if (filesArray.length === 0) {
    updateModel()
    emit('change', filePreviews.value)
  }
}

const updateModel = () => {
  if (props.multiple) {
    const files = filePreviews.value.map(f => f.file || f)
    emit('update:modelValue', files)
  } else {
    const first = filePreviews.value[0]
    if (first) {
      const fileData = first.file || first
      emit('update:modelValue', fileData)
    } else {
      emit('update:modelValue', null)
    }
  }
}

const triggerFileInput = () => {
  if (!props.disabled && fileInputRef.value) {
    fileInputRef.value.click()
  }
}

const removeFile = (index) => {
  filePreviews.value.splice(index, 1)
  updateModel()
  emit('remove', index)
  emit('change', filePreviews.value)
}

const reset = () => {
  filePreviews.value = []
  updateModel()
}

defineExpose({
  filePreviews,
  reset
})
</script>