<template>
  <div class="flex flex-col min-h-screen">
    <!-- HEADER -->
    <AppHeader />

    <!-- MAIN -->
    <main class="flex-1">
      <NuxtPage />
    </main>

    <!-- FOOTER -->
    <AppFooter />
  </div>
</template>

<script setup>
import AppHeader from '~/components/layout/AppHeader.vue'
import AppFooter from '~/components/layout/AppFooter.vue'
</script>