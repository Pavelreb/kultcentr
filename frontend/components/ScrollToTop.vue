<template>
  <Transition name="fade">
    <button
      v-show="visible"
      type="button"
      aria-label="Наверх"
      class="fixed bottom-6 right-6 z-40 w-12 h-12 rounded-full bg-indigo-600 hover:bg-indigo-700 dark:bg-indigo-500 dark:hover:bg-indigo-600 text-white shadow-lg flex items-center justify-center transition-colors duration-200"
      @click="scrollToTop"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="w-6 h-6"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        stroke-width="2"
      >
        <path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7" />
      </svg>
    </button>
  </Transition>
</template>

<script setup>
import { smoothScrollTo } from '~/composables/useSmoothScroll'

// Кнопка появляется, когда пользователь прокрутил ниже 400px
const visible = ref(false)
const onScroll = () => {
  visible.value = window.scrollY > 400
}

onMounted(() => {
  onScroll()
  window.addEventListener('scroll', onScroll, { passive: true })
})
onBeforeUnmount(() => {
  window.removeEventListener('scroll', onScroll)
})

const scrollToTop = () => smoothScrollTo(0)
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
