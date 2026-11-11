<!-- frontend/components/common/RichText.vue -->
<!-- Безопасный рендер ограниченной разметки: **жирный**, *курсив*, [ссылка](url), списки "- " и "1. " -->
<template>
  <div v-if="!compact" class="rich-text text-gray-700 dark:text-gray-300 leading-relaxed" v-html="html"></div>
  <span v-else v-html="html"></span>
</template>

<script setup>
const props = defineProps({
  text: {
    type: String,
    default: ''
  },
  // compact — для карточек: без блочной вёрстки, всё в одну строку (работает с line-clamp)
  compact: {
    type: Boolean,
    default: false
  }
})

const escapeHtml = (s) =>
  s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;')

// Строка уже экранирована — добавляем инлайн-разметку
const renderInline = (text) => {
  let t = escapeHtml(text)
  // Ссылки [текст](https://...)
  t = t.replace(
    /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
    '<a href="$2" target="_blank" rel="noopener noreferrer" class="text-blue-600 dark:text-blue-400 hover:underline">$1</a>'
  )
  // **жирный**
  t = t.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
  // *курсив*
  t = t.replace(/\*([^*]+)\*/g, '<em>$1</em>')
  return t
}

const html = computed(() => {
  if (!props.text) return ''

  // Компактный режим: схлопываем строки в одну, маркеры списков → «• »
  if (props.compact) {
    const flat = props.text
      .split('\n')
      .map((l) => l.trim())
      .filter(Boolean)
      .map((l) => l.replace(/^-\s+/, '• '))
      .join(' ')
    return renderInline(flat)
  }

  const lines = props.text.split('\n')
  const out = []
  let paragraph = []
  let list = null // { type: 'ul' | 'ol', items: [] }

  const flushParagraph = () => {
    if (paragraph.length) {
      out.push(`<p class="mb-3">${paragraph.map(renderInline).join('<br>')}</p>`)
      paragraph = []
    }
  }
  const flushList = () => {
    if (list) {
      const items = list.items.map((i) => `<li>${renderInline(i)}</li>`).join('')
      const cls = list.type === 'ul' ? 'list-disc' : 'list-decimal'
      out.push(`<${list.type} class="${cls} pl-6 mb-3 space-y-1">${items}</${list.type}>`)
      list = null
    }
  }

  for (const raw of lines) {
    const line = raw.trimEnd()
    const ulMatch = line.match(/^\s*-\s+(.+)$/)
    const olMatch = line.match(/^\s*\d+\.\s+(.+)$/)

    if (ulMatch) {
      flushParagraph()
      if (!list || list.type !== 'ul') {
        flushList()
        list = { type: 'ul', items: [] }
      }
      list.items.push(ulMatch[1])
    } else if (olMatch) {
      flushParagraph()
      if (!list || list.type !== 'ol') {
        flushList()
        list = { type: 'ol', items: [] }
      }
      list.items.push(olMatch[1])
    } else if (line.trim() === '') {
      flushParagraph()
      flushList()
    } else {
      flushList()
      paragraph.push(line)
    }
  }
  flushParagraph()
  flushList()

  return out.join('')
})
</script>
