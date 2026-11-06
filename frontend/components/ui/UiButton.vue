<!-- frontend/components/ui/UiButton.vue -->
<template>
  <button 
    :type="type"
    :disabled="disabled"
    class="px-6 py-2.5 rounded-xl transition-all duration-300 font-medium inline-flex items-center justify-center gap-2 shadow-sm hover:shadow-md active:scale-95"
    :class="[variantClasses, sizeClasses, widthClass]"
    @click="$emit('click')"
  >
    <slot />
  </button>
</template>

<script setup>
const props = defineProps({
  variant: {
    type: String,
    default: 'primary',
    validator: (value) => ['primary', 'secondary', 'danger', 'warning', 'outline', 'success', 'ghost'].includes(value)
  },
  type: {
    type: String,
    default: 'button'
  },
  disabled: {
    type: Boolean,
    default: false
  },
  size: {
    type: String,
    default: 'md',
    validator: (value) => ['sm', 'md', 'lg'].includes(value)
  },
  fullWidth: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['click'])

const variantClasses = computed(() => {
  const variants = {
    primary: 'bg-gradient-to-r from-blue-500 to-blue-600 text-white hover:from-blue-600 hover:to-blue-700 disabled:from-blue-300 disabled:to-blue-400 dark:disabled:from-blue-800 dark:disabled:to-blue-900 shadow-blue-500/25 hover:shadow-blue-500/40',
    
    secondary: 'bg-gradient-to-r from-gray-500 to-gray-600 text-white hover:from-gray-600 hover:to-gray-700 disabled:from-gray-300 disabled:to-gray-400 dark:disabled:from-gray-700 dark:disabled:to-gray-800 shadow-gray-500/25 hover:shadow-gray-500/40',
    
    success: 'bg-gradient-to-r from-emerald-500 to-green-600 text-white hover:from-emerald-600 hover:to-green-700 disabled:from-emerald-300 disabled:to-green-400 dark:disabled:from-emerald-800 dark:disabled:to-green-900 shadow-emerald-500/25 hover:shadow-emerald-500/40',
    
    danger: 'bg-gradient-to-r from-red-500 to-red-600 text-white hover:from-red-600 hover:to-red-700 disabled:from-red-300 disabled:to-red-400 dark:disabled:from-red-800 dark:disabled:to-red-900 shadow-red-500/25 hover:shadow-red-500/40',
    
    warning: 'bg-gradient-to-r from-amber-500 to-yellow-600 text-white hover:from-amber-600 hover:to-yellow-700 disabled:from-amber-300 disabled:to-yellow-400 dark:disabled:from-amber-800 dark:disabled:to-yellow-900 shadow-amber-500/25 hover:shadow-amber-500/40',
    
    outline: 'bg-transparent border-2 border-blue-500 text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/20 hover:border-blue-600 dark:hover:border-blue-300 disabled:opacity-50 disabled:cursor-not-allowed',
    
    ghost: 'bg-transparent text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white disabled:opacity-50 disabled:cursor-not-allowed'
  }
  return variants[props.variant] || variants.primary
})

const sizeClasses = computed(() => {
  const sizes = {
    sm: 'px-3.5 py-2 text-sm',
    md: 'px-6 py-2.5 text-base',
    lg: 'px-8 py-3.5 text-lg'
  }
  return sizes[props.size] || sizes.md
})

const widthClass = computed(() => {
  return props.fullWidth ? 'w-full' : ''
})
</script>