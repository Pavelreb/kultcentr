<!-- frontend/components/features/posts/QuizEditor.vue -->
<!-- Редактор теста для формы поста. v-model: null или { title, description, questions: [{ text, answers: [{ text, is_correct }] }] } -->
<template>
  <div class="border border-gray-200 dark:border-gray-700 rounded-xl p-4 bg-gray-50 dark:bg-gray-700/30">
    <label class="flex items-center gap-2 cursor-pointer select-none">
      <input
        type="checkbox"
        :checked="enabled"
        @change="toggle"
        class="w-4 h-4 text-emerald-500 rounded"
      />
      <span class="text-sm font-medium text-gray-700 dark:text-gray-300 flex items-center gap-1.5">
        <svg class="w-4 h-4 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/>
        </svg>
        Добавить тест
      </span>
    </label>

    <div v-if="enabled" class="mt-4 space-y-4">
      <div>
        <label class="block text-gray-700 dark:text-gray-300 mb-1.5 text-sm font-medium">
          Название теста <span class="text-red-500">*</span>
        </label>
        <input
          :value="modelValue.title"
          @input="update({ title: $event.target.value })"
          type="text"
          placeholder="Например: Проверь свои знания..."
          class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
        />
      </div>

      <div>
        <label class="block text-gray-700 dark:text-gray-300 mb-1.5 text-sm font-medium">Описание</label>
        <input
          :value="modelValue.description"
          @input="update({ description: $event.target.value })"
          type="text"
          placeholder="Краткое описание теста (необязательно)"
          class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
        />
      </div>

      <!-- Вопросы -->
      <div class="space-y-3">
        <div
          v-for="(q, qi) in modelValue.questions"
          :key="qi"
          class="p-4 rounded-xl bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-600"
        >
          <div class="flex items-center justify-between gap-2 mb-2">
            <span class="text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wide">Вопрос {{ qi + 1 }}</span>
            <button
              v-if="modelValue.questions.length > 1"
              type="button"
              @click="removeQuestion(qi)"
              class="p-1 text-red-400 hover:text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition"
              title="Удалить вопрос"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
              </svg>
            </button>
          </div>

          <input
            :value="q.text"
            @input="setQuestionText(qi, $event.target.value)"
            type="text"
            placeholder="Текст вопроса..."
            class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 mb-3"
          />

          <div class="space-y-2">
            <div v-for="(a, ai) in q.answers" :key="ai" class="flex items-center gap-2">
              <label class="flex items-center cursor-pointer flex-shrink-0" title="Отметить как правильный">
                <input
                  type="radio"
                  :name="`quiz-q-${qi}`"
                  :checked="!!a.is_correct"
                  @change="setCorrect(qi, ai)"
                  class="w-4 h-4 text-emerald-500"
                />
              </label>
              <input
                :value="a.text"
                @input="setAnswerText(qi, ai, $event.target.value)"
                type="text"
                :placeholder="`Ответ ${ai + 1}`"
                class="flex-1 border border-gray-300 dark:border-gray-600 rounded-xl p-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              />
              <button
                v-if="q.answers.length > 2"
                type="button"
                @click="removeAnswer(qi, ai)"
                class="p-1.5 text-red-400 hover:text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition flex-shrink-0"
                title="Удалить ответ"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                </svg>
              </button>
            </div>
          </div>

          <button
            type="button"
            @click="addAnswer(qi)"
            class="mt-2 inline-flex items-center gap-1.5 px-3 py-1.5 text-sm text-emerald-600 dark:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-900/20 rounded-lg transition"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
            </svg>
            Добавить ответ
          </button>
          <p class="mt-1 text-xs text-gray-400 dark:text-gray-500">Отметьте переключателем правильный ответ.</p>
        </div>
      </div>

      <button
        type="button"
        @click="addQuestion"
        class="inline-flex items-center gap-1.5 px-4 py-2 text-sm font-medium text-emerald-600 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-800 hover:bg-emerald-50 dark:hover:bg-emerald-900/20 rounded-xl transition"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
        </svg>
        Добавить вопрос
      </button>
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

const blankQuestion = () => ({
  text: '',
  answers: [
    { text: '', is_correct: true },
    { text: '', is_correct: false }
  ]
})

const update = (patch) => {
  emit('update:modelValue', { ...props.modelValue, ...patch })
}

const toggle = () => {
  if (enabled.value) {
    emit('update:modelValue', null)
  } else {
    emit('update:modelValue', {
      title: '',
      description: '',
      questions: [blankQuestion()]
    })
  }
}

const setQuestionText = (qi, text) => {
  const questions = props.modelValue.questions.map((q, i) =>
    i === qi ? { ...q, text } : q
  )
  update({ questions })
}

const addQuestion = () => {
  update({ questions: [...props.modelValue.questions, blankQuestion()] })
}

const removeQuestion = (qi) => {
  update({ questions: props.modelValue.questions.filter((_, i) => i !== qi) })
}

const setAnswerText = (qi, ai, text) => {
  const questions = props.modelValue.questions.map((q, i) => {
    if (i !== qi) return q
    const answers = q.answers.map((a, j) => (j === ai ? { ...a, text } : a))
    return { ...q, answers }
  })
  update({ questions })
}

const setCorrect = (qi, ai) => {
  const questions = props.modelValue.questions.map((q, i) => {
    if (i !== qi) return q
    const answers = q.answers.map((a, j) => ({ ...a, is_correct: j === ai }))
    return { ...q, answers }
  })
  update({ questions })
}

const addAnswer = (qi) => {
  const questions = props.modelValue.questions.map((q, i) => {
    if (i !== qi) return q
    return { ...q, answers: [...q.answers, { text: '', is_correct: false }] }
  })
  update({ questions })
}

const removeAnswer = (qi, ai) => {
  const questions = props.modelValue.questions.map((q, i) => {
    if (i !== qi) return q
    return { ...q, answers: q.answers.filter((_, j) => j !== ai) }
  })
  update({ questions })
}
</script>
