<template>
  <div class="relative w-full overflow-hidden transition-colors duration-200">
    <div 
      v-if="banner.has_background" 
      class="absolute inset-0 w-full h-full bg-cover bg-center"
      :style="{ backgroundImage: `url(${banner.background_image_url_display})` }"
    >
      <div class="absolute inset-0 bg-black bg-opacity-40"></div>
    </div>
    
    <div 
      v-else
      class="absolute inset-0 w-full h-full bg-gradient-to-r from-blue-600 to-purple-600 dark:from-blue-800 dark:to-purple-800"
    ></div>
    
    <div class="relative container mx-auto px-4 py-20 md:py-28 text-center text-white">
      <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-4">
        {{ banner.title }}
      </h1>
      <p class="text-lg md:text-xl text-blue-100 dark:text-blue-200 max-w-2xl mx-auto">
        {{ banner.subtitle }}
      </p>
      
      <NuxtLink 
        v-if="banner.button_enabled !== false && banner.button_text && banner.button_link"
        :to="banner.button_link"
        class="inline-block mt-6 bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-blue-50 transition shadow-lg"
      >
        {{ banner.button_text }} →
      </NuxtLink>
    </div>
  </div>
</template>

<script setup>
defineProps({
  banner: {
    type: Object,
    required: true,
    default: () => ({
      title: '🏛️ Добро пожаловать в Центр Культуры',
      subtitle: 'Место, где искусство, традиции и творчество объединяются',
      has_background: false,
      background_image_url_display: '',
      button_text: '',
      button_link: '',
      button_enabled: true,
      is_active: true
    })
  }
})
</script>