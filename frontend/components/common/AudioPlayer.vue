<!-- frontend/components/common/AudioPlayer.vue -->
<!-- Компактный аудиоплеер: play/pause, прогресс, время, громкость -->
<template>
  <div class="flex items-center gap-3">
    <!-- Play/Pause -->
    <button
      type="button"
      @click.stop.prevent="toggle"
      class="w-10 h-10 flex-shrink-0 rounded-full bg-gradient-to-br from-teal-500 to-emerald-600 text-white flex items-center justify-center shadow-md hover:shadow-lg hover:scale-105 transition-all duration-200"
      :aria-label="playing ? 'Пауза' : 'Слушать'"
    >
      <svg v-if="!playing" class="w-4 h-4 ml-0.5" fill="currentColor" viewBox="0 0 24 24">
        <path d="M8 5v14l11-7z"/>
      </svg>
      <svg v-else class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
        <path d="M6 4h4v16H6zM14 4h4v16h-4z"/>
      </svg>
    </button>

    <!-- Прогресс -->
    <div class="flex-1 min-w-0">
      <div
        ref="barEl"
        class="h-2 bg-gray-200 dark:bg-gray-600 rounded-full cursor-pointer group/bar"
        @click.stop.prevent="seek"
      >
        <div
          class="h-full bg-gradient-to-r from-teal-500 to-emerald-500 rounded-full relative transition-[width] duration-100"
          :style="{ width: progress + '%' }"
        >
          <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-3.5 h-3.5 bg-white border-2 border-teal-500 rounded-full shadow opacity-0 group-hover/bar:opacity-100 transition-opacity"></div>
        </div>
      </div>
      <div class="flex justify-between mt-1 text-[10px] text-gray-400 dark:text-gray-500 tabular-nums">
        <span>{{ fmt(currentTime) }}</span>
        <span>{{ fmt(total) }}</span>
      </div>
    </div>

    <!-- Громкость (только десктоп) -->
    <div class="hidden sm:flex items-center gap-1.5 flex-shrink-0">
      <button type="button" @click.stop.prevent="toggleMute" class="text-gray-400 hover:text-teal-500 transition-colors" :aria-label="muted ? 'Включить звук' : 'Выключить звук'">
        <svg v-if="muted || volume === 0" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z M17 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2"/>
        </svg>
        <svg v-else class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072M18.364 5.636a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/>
        </svg>
      </button>
      <input
        type="range"
        min="0" max="1" step="0.05"
        :value="muted ? 0 : volume"
        @input.stop.prevent="setVolume"
        @click.stop
        class="w-16 h-1 accent-teal-500 cursor-pointer"
      >
    </div>

    <audio
      ref="audioEl"
      :src="src"
      preload="metadata"
      @timeupdate="onTimeUpdate"
      @loadedmetadata="onLoaded"
      @ended="onEnded"
    ></audio>
  </div>
</template>

<script setup>
const props = defineProps({
  src: {
    type: String,
    required: true
  },
  durationHint: {
    type: Number,
    default: null
  }
})

const audioEl = ref(null)
const barEl = ref(null)
const playing = ref(false)
const currentTime = ref(0)
const total = ref(props.durationHint || 0)
const volume = ref(1)
const muted = ref(false)

// Уникальный id плеера, чтобы при старте одного остальные вставали на паузу
const uid = Math.random().toString(36).slice(2)

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
  const el = audioEl.value
  if (!el) return
  if (playing.value) {
    el.pause()
  } else {
    window.dispatchEvent(new CustomEvent('medialib:audio-play', { detail: uid }))
    el.play()
  }
}

const toggleMute = () => {
  muted.value = !muted.value
  if (audioEl.value) audioEl.value.muted = muted.value
}

const setVolume = (e) => {
  const v = parseFloat(e.target.value)
  volume.value = v
  muted.value = v === 0
  if (audioEl.value) {
    audioEl.value.volume = v
    audioEl.value.muted = v === 0
  }
}

const seek = (e) => {
  const el = audioEl.value
  const bar = barEl.value
  if (!el || !bar || !el.duration) return
  const rect = bar.getBoundingClientRect()
  const ratio = Math.min(1, Math.max(0, (e.clientX - rect.left) / rect.width))
  el.currentTime = ratio * el.duration
}

const onTimeUpdate = () => {
  if (audioEl.value) currentTime.value = audioEl.value.currentTime
}

const onLoaded = () => {
  if (audioEl.value && isFinite(audioEl.value.duration)) {
    total.value = audioEl.value.duration
  }
}

const onEnded = () => {
  playing.value = false
  currentTime.value = 0
}

const onOtherPlay = (e) => {
  if (e.detail !== uid && playing.value && audioEl.value) {
    audioEl.value.pause()
  }
}

onMounted(() => {
  if (audioEl.value) audioEl.value.volume = volume.value
  audioEl.value?.addEventListener('play', () => { playing.value = true })
  audioEl.value?.addEventListener('pause', () => { playing.value = false })
  window.addEventListener('medialib:audio-play', onOtherPlay)
})

onUnmounted(() => {
  window.removeEventListener('medialib:audio-play', onOtherPlay)
})
</script>
