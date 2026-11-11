<!-- frontend/components/common/RichTextEditor.vue -->
<!-- Текстовое поле с панелью форматирования: жирный, курсив, списки, ссылки -->
<template>
  <div class="border border-gray-300 dark:border-gray-600 rounded-xl overflow-hidden focus-within:ring-2 focus-within:ring-blue-500 transition bg-white dark:bg-gray-700">
    <!-- Панель инструментов -->
    <div class="flex flex-wrap items-center gap-1 px-2 py-1.5 bg-gray-50 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-600">
      <button
        type="button"
        @click="wrapSelection('**', '**')"
        title="Жирный"
        class="toolbar-btn font-bold"
      >B</button>
      <button
        type="button"
        @click="wrapSelection('*', '*')"
        title="Курсив"
        class="toolbar-btn italic"
      >I</button>
      <span class="w-px h-5 bg-gray-300 dark:bg-gray-600 mx-1"></span>
      <button
        type="button"
        @click="prefixLines('- ')"
        title="Маркированный список"
        class="toolbar-btn"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
        <span class="text-xs">•</span>
      </button>
      <button
        type="button"
        @click="prefixLines('1. ')"
        title="Нумерованный список"
        class="toolbar-btn"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
        <span class="text-xs">1.</span>
      </button>
      <span class="w-px h-5 bg-gray-300 dark:bg-gray-600 mx-1"></span>
      <button
        type="button"
        @click="insertLink"
        title="Ссылка"
        class="toolbar-btn"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"/>
        </svg>
      </button>
      <span class="ml-auto text-xs text-gray-400 dark:text-gray-500 hidden sm:inline">
        **жирный** · *курсив* · [текст](ссылка)
      </span>
    </div>

    <!-- Поле ввода -->
    <textarea
      ref="textareaRef"
      :value="modelValue"
      @input="onInput"
      :placeholder="placeholder"
      :rows="rows"
      class="w-full p-3 resize-none focus:outline-none bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
      :required="required"
    ></textarea>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  },
  placeholder: {
    type: String,
    default: ''
  },
  rows: {
    type: [Number, String],
    default: 10
  },
  required: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:modelValue'])

const textareaRef = ref(null)

const onInput = (e) => {
  emit('update:modelValue', e.target.value)
}

// Оборачивает выделенный текст маркерами (или вставляет их в позицию курсора)
const wrapSelection = (before, after) => {
  const ta = textareaRef.value
  if (!ta) return
  const start = ta.selectionStart
  const end = ta.selectionEnd
  const value = props.modelValue || ''
  const selected = value.slice(start, end)
  const replacement = before + selected + after
  const next = value.slice(0, start) + replacement + value.slice(end)
  emit('update:modelValue', next)
  nextTick(() => {
    ta.focus()
    if (selected) {
      ta.setSelectionRange(start, start + replacement.length)
    } else {
      const pos = start + before.length
      ta.setSelectionRange(pos, pos)
    }
  })
}

// Добавляет префикс к каждой выделенной строке (или к текущей строке)
const prefixLines = (prefix) => {
  const ta = textareaRef.value
  if (!ta) return
  const value = props.modelValue || ''
  const start = ta.selectionStart
  const end = ta.selectionEnd

  // Расширяем выделение до границ строк
  const lineStart = value.lastIndexOf('\n', start - 1) + 1
  let lineEnd = value.indexOf('\n', end)
  if (lineEnd === -1) lineEnd = value.length

  const block = value.slice(lineStart, lineEnd)
  const lines = block.split('\n')
  const isNumbered = /^\d+\.\s/.test(prefix)
  const nextBlock = lines
    .map((l, i) => {
      if (!l.trim()) return l
      const p = isNumbered ? `${i + 1}. ` : prefix
      return l.startsWith(p) ? l : p + l
    })
    .join('\n')

  const next = value.slice(0, lineStart) + nextBlock + value.slice(lineEnd)
  emit('update:modelValue', next)
  nextTick(() => {
    ta.focus()
    ta.setSelectionRange(lineStart, lineStart + nextBlock.length)
  })
}

// Вставляет ссылку [текст](url)
const insertLink = () => {
  const ta = textareaRef.value
  if (!ta) return
  const start = ta.selectionStart
  const end = ta.selectionEnd
  const value = props.modelValue || ''
  const selected = value.slice(start, end)

  const url = prompt('Введите адрес ссылки (https://...):', 'https://')
  if (!url || url === 'https://') return
  if (!/^https?:\/\//.test(url)) {
    alert('Ссылка должна начинаться с http:// или https://')
    return
  }

  const text = selected || 'текст ссылки'
  const replacement = `[${text}](${url})`
  const next = value.slice(0, start) + replacement + value.slice(end)
  emit('update:modelValue', next)
  nextTick(() => {
    ta.focus()
    ta.setSelectionRange(start, start + replacement.length)
  })
}
</script>

<style scoped>
.toolbar-btn {
  @apply flex items-center justify-center gap-0.5 min-w-[2rem] h-8 px-2 rounded-lg text-sm text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 transition;
}
</style>
