<template>
  <div class="bg-white dark:bg-gray-800 rounded-lg shadow" :class="paddingClass">
    <slot />
  </div>
</template>

<script setup>
const props = defineProps({
  padding: {
    type: String,
    default: 'md',
    validator: (value) => ['none', 'sm', 'md', 'lg'].includes(value)
  }
})

const paddingClass = computed(() => {
  const paddings = {
    none: 'p-0',
    sm: 'p-3',
    md: 'p-6',
    lg: 'p-8'
  }
  return paddings[props.padding] || paddings.md
})
</script>