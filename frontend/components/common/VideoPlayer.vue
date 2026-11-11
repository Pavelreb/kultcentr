<!-- frontend/components/common/VideoPlayer.vue -->
<!-- Кастомный видеоплеер: без кнопки скачивания, рабочая перемотка, ползунок громкости -->
<template>
  <div
    ref="wrapEl"
    class="relative bg-black select-none group/player"
    @mousemove="onActivity"
    @mouseleave="hideControlsSoon"
  >
    <video
      ref="videoEl"
      :src="src"
      :poster="poster || undefined"
      preload="metadata"
      class="w-full aspect-video"
      @click="toggle"
      @timeupdate="onTimeUpdate"
      @loadedmetadata="onLoaded"
      @ended="onEnded"
      @play="playing = true"
      @pause="playing = false"
    ></video>

    <!-- Большая кнопка play по центру (когда на паузе) -->
    <button
      v-if="!playing"
      type="button"
      @click="toggle"
      class="absolute inset-0 flex items-center justify-center bg-black/30 transition-opacity"
      aria-label="Смотреть"
    >
      <span class="w-16 h-16 md:w-20 md:h-20 rounded-full bg-white/90 flex items-center justify-center shadow-xl hover:scale-105 transition-transform">
        <svg class="w-8 h-8 md:w-9 md:h-9 text-rose-600 ml-1" fill="currentColor" viewBox="0 0 24 24">
          <path d="M8 5v14l11-7z"/>
        </svg>
      </span>
    </button>

    <!-- Панель управления -->
    <div
      class="absolute bottom-0 left-0 right-0 px-3 pb-2 pt-8 bg-gradient-to-t from-black/80 to-transparent transition-opacity duration-200"
      :class="controlsVisible || !playing ? 'opacity-100' : 'opacity-0'"
    >
      <!-- Ползунок перемотки -->
      <div
        ref="barEl"
        class="h-1.5 hover:h-2.5 transition-all bg-white/25 rounded-full cursor-pointer mb-2 group/seek"
        @click="seek"
        @mousedown="startDrag"
      >
        <div
          class="h-full bg-rose-500 rounded-full relative"
          :style="{ width: progress + '%' }"
        >
          <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-3.5 h-3.5 bg-white rounded-full shadow opacity-0 group-hover/seek:opacity-100 transition-opacity"></div>
        </div>
      </div>

      <div class="flex items-center gap-3">
        <!-- Play/Pause -->
        <button
          type="button"
          @click="toggle"
          class="w-9 h-9 flex items-center justify-center rounded-full text-white hover:bg-white/15 transition"
          :aria-label="playing ? 'Пауза' : 'Смотреть'"
        >
          <svg v-if="!playing" class="w-5 h-5 ml-0.5" fill="currentColor" viewBox="0 0 24 24">
            <path d="M8 5v14l11-7z"/>
          </svg>
          <svg v-else class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
            <path d="M6 4h4v16H6zM14 4h4v16h-4z"/>
          </svg>
        </button>

        <!-- Время -->
        <span class="text-white/90 text-xs tabular-nums whitespace-nowrap">
          {{ fmt(currentTime) }} / {{ fmt(total) }}
        </span>

        <div class="flex-1"></div>

        <!-- Громкость -->
        <div class="hidden sm:flex items-center gap-1.5">
          <button
            type="button"
            @click="toggleMute"
            class="w-8 h-8 flex items-center justify-center rounded-full text-white hover:bg-white/15 transition"
            :aria-label="muted ? 'Включить звук' : 'Выключить звук'"
          >
            <svg v-if="muted || volume === 0" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z M17 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2"/>
            </svg>
            <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072M18.364 5.636a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/>
            </svg>
          </button>
          <input
            type="range"
            min="0" max="1" step="0.05"
            :value="muted ? 0 : volume"
            @input="setVolume"
            class="w-20 h-1 accent-rose-500 cursor-pointer"
            aria-label="Громкость"
          >
        </div>

        <!-- Полный экран -->
        <button
          type="button"
          @click="toggleFullscreen"
          class="w-9 h-9 flex items-center justify-center rounded-full text-white hover:bg-white/15 transition"
          aria-label="Полный экран"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"/>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  src: {
    type: String,
    required: true
  },
  poster: {
    type: String,
    default: ''
  }
})

const wrapEl = ref(null)
const videoEl = ref(null)
const barEl = ref(null)

const playing = ref(false)
const currentTime = ref(0)
const total = ref(0)
const volume = ref(1)
const muted = ref(false)
const controlsVisible = ref(true)

let hideTimer = null
let dragging = false

const progress = computed(() => {
  if (!total.value) return 0
  return Math.min(100, (currentTime.value / total.value) * 100)
})

const fmt = (sec) => {
  if (!sec && sec !== 0) return '0:00'
  sec = Math.floor(sec)
  const m = Math.floor(sec / 60)
  const s = sec % 60
  return `${m}:${String(s).padStart(2, '0')}`
}

const toggle = () => {
  const el = videoEl.value
  if (!el) return
  if (el.paused) {
    el.play()
  } else {
    el.pause()
  }
}

const toggleMute = () => {
  muted.value = !muted.value
  if (videoEl.value) videoEl.value.muted = muted.value
}

const setVolume = (e) => {
  const v = parseFloat(e.target.value)
  volume.value = v
  muted.value = v === 0
  if (videoEl.value) {
    videoEl.value.volume = v
    videoEl.value.muted = v === 0
  }
}

const seekToRatio = (ratio) => {
  const el = videoEl.value
  if (!el || !el.duration) return
  el.currentTime = Math.min(1, Math.max(0, ratio)) * el.duration
}

const seek = (e) => {
  const bar = barEl.value
  if (!bar) return
  const rect = bar.getBoundingClientRect()
  seekToRatio((e.clientX - rect.left) / rect.width)
}

const startDrag = (e) => {
  dragging = true
  seek(e)
}

const onDrag = (e) => {
  if (dragging) seek(e)
}

const stopDrag = () => {
  dragging = false
}

const toggleFullscreen = () => {
  if (document.fullscreenElement) {
    document.exitFullscreen()
  } else {
    wrapEl.value?.requestFullscreen()
  }
}

const onTimeUpdate = () => {
  if (videoEl.value) currentTime.value = videoEl.value.currentTime
}

const onLoaded = () => {
  if (videoEl.value && isFinite(videoEl.value.duration)) {
    total.value = videoEl.value.duration
  }
}

const onEnded = () => {
  playing.value = false
  controlsVisible.value = true
}

const onActivity = () => {
  controlsVisible.value = true
  hideControlsSoon()
}

const hideControlsSoon = () => {
  if (hideTimer) clearTimeout(hideTimer)
  hideTimer = setTimeout(() => {
    if (playing.value) controlsVisible.value = false
  }, 2500)
}

onMounted(() => {
  if (videoEl.value) videoEl.value.volume = volume.value
  document.addEventListener('mousemove', onDrag)
  document.addEventListener('mouseup', stopDrag)
})

onUnmounted(() => {
  if (hideTimer) clearTimeout(hideTimer)
  document.removeEventListener('mousemove', onDrag)
  document.removeEventListener('mouseup', stopDrag)
})
</script>
