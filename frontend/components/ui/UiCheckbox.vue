<template>
  <label class="flex items-center gap-2 cursor-pointer group">
    <div class="relative">
      <input 
        type="checkbox"
        :checked="modelValue"
        :disabled="disabled"
        class="w-4 h-4 text-blue-500 rounded focus:ring-2 focus:ring-blue-500 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed"
        @change="$emit('update:modelValue', $event.target.checked)"
      />
    </div>
    <span class="text-gray-700 dark:text-gray-300 select-none" :class="disabled ? 'opacity-50' : ''">
      <slot />
    </span>
  </label>
</template>

<script setup>
defineProps({
  modelValue: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  }
})

defineEmits(['update:modelValue'])
</script>