<template>
  <div class="mb-4">
    <label v-if="label" class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>
    <textarea 
      :value="modelValue"
      :placeholder="placeholder"
      :rows="rows"
      :required="required"
      :disabled="disabled"
      class="w-full border rounded-lg p-2 focus:outline-none focus:ring-2 transition resize-y min-h-[60px] bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
      :class="inputClasses"
      @input="$emit('update:modelValue', $event.target.value)"
      @blur="$emit('blur')"
      @focus="$emit('focus')"
    ></textarea>
    <p v-if="error" class="text-red-500 text-sm mt-1">{{ error }}</p>
    <p v-if="hint" class="text-gray-400 dark:text-gray-500 text-sm mt-1">{{ hint }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  },
  label: {
    type: String,
    default: ''
  },
  placeholder: {
    type: String,
    default: ''
  },
  rows: {
    type: Number,
    default: 3
  },
  required: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  },
  error: {
    type: String,
    default: ''
  },
  hint: {
    type: String,
    default: ''
  },
  variant: {
    type: String,
    default: 'default',
    validator: (value) => ['default', 'success', 'error'].includes(value)
  }
})

defineEmits(['update:modelValue', 'blur', 'focus'])

const inputClasses = computed(() => {
  const variants = {
    default: 'border-gray-300 dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500',
    success: 'border-green-500 focus:ring-green-500 focus:border-green-500',
    error: 'border-red-500 focus:ring-red-500 focus:border-red-500'
  }
  return variants[props.variant] || variants.default
})
</script>