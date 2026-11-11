<!-- frontend/components/features/posts/PollEditor.vue -->
<!-- Редактор голосования для формы поста. v-model: null или { question, options: [строки] } -->
<template>
  <div class="border border-gray-200 dark:border-gray-700 rounded-xl p-4 bg-gray-50 dark:bg-gray-700/30">
    <label class="flex items-center gap-2 cursor-pointer select-none">
      <input
        type="checkbox"
        :checked="enabled"
        @change="toggle"
        class="w-4 h-4 text-blue-500 rounded"
      />
      <span class="text-sm font-medium text-gray-700 dark:text-gray-300 flex items-center gap-1.5">
        <svg class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
        </svg>
        Добавить голосование
      </span>
    </label>

    <div v-if="enabled" class="mt-4 space-y-3">
      <div>
        <label class="block text-gray-700 dark:text-gray-300 mb-1.5 text-sm font-medium">
          Вопрос <span class="text-red-500">*</span>
        </label>
        <input
          v-model="question"
          type="text"
          placeholder="Задайте вопрос..."
          class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
        />
      </div>

      <div>
        <label class="block text-gray-700 dark:text-gray-300 mb-1.5 text-sm font-medium">
          Варианты ответов <span class="text-red-500">*</span>
          <span class="text-xs font-normal text-gray-400 dark:text-gray-500">(минимум 2)</span>
        </label>
        <div class="space-y-2">
          <div v-for="(opt, i) in options" :key="i" class="flex items-center gap-2">
            <span class="w-6 text-center text-xs text-gray-400 dark:text-gray-500 flex-shrink-0">{{ i + 1 }}</span>
            <input
              :value="opt"
              @input="setOption(i, $event.target.value)"
              type="text"
              :placeholder="`Вариант ${i + 1}`"
              class="flex-1 border border-gray-300 dark:border-gray-600 rounded-xl p-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            />
            <button
              v-if="options.length > 2"
              type="button"
              @click="removeOption(i)"
              class="p-1.5 text-red-400 hover:text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition flex-shrink-0"
              title="Удалить вариант"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
            </button>
          </div>
        </div>
        <button
          type="button"
          @click="addOption"
          class="mt-2 inline-flex items-center gap-1.5 px-3 py-1.5 text-sm text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/20 rounded-lg transition"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
          </svg>
          Добавить вариант
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['update:modelValue'])

const enabled = computed(() => props.modelValue !== null)

const question = computed({
  get: () => props.modelValue?.question || '',
  set: (v) => update({ question: v })
})

const options = computed(() => props.modelValue?.options || ['', ''])

const update = (patch) => {
  emit('update:modelValue', {
    question: props.modelValue?.question || '',
    options: [...(props.modelValue?.options || ['', ''])],
    ...patch
  })
}

const toggle = () => {
  if (enabled.value) {
    emit('update:modelValue', null)
  } else {
    emit('update:modelValue', { question: '', options: ['', ''] })
  }
}

const setOption = (i, value) => {
  const next = [...options.value]
  next[i] = value
  update({ options: next })
}

const addOption = () => {
  update({ options: [...options.value, ''] })
}

const removeOption = (i) => {
  const next = options.value.filter((_, idx) => idx !== i)
  update({ options: next })
}
</script>
