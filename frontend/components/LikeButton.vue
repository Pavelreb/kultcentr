<template>
  <button 
    @click="toggleLike"
    :disabled="loading"
    class="flex items-center gap-1 transition hover:scale-110"
    :class="[
      isLiked ? 'text-red-500' : 'text-gray-400 hover:text-red-400',
      loading ? 'opacity-50 cursor-not-allowed' : ''
    ]"
  >
    <span class="text-sm">{{ isLiked ? '❤️' : '🤍' }}</span>
    <span class="text-sm font-medium">{{ likesCount }}</span>
  </button>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const props = defineProps({
  postId: {
    type: Number,
    default: null
  },
  commentId: {
    type: Number,
    default: null
  },
  initialLikesCount: {
    type: Number,
    default: 0
  },
  initialIsLiked: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update'])

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()

const likesCount = ref(props.initialLikesCount)
const isLiked = ref(props.initialIsLiked)
const loading = ref(false)

const toggleLike = async () => {
  if (!authStore.isAuthenticated) {
    alert('Войдите в систему, чтобы ставить лайки')
    return
  }
  
  loading.value = true
  
  try {
    const body = {}
    if (props.postId) {
      body.post = props.postId
    } else if (props.commentId) {
      body.comment = props.commentId
    } else {
      console.error('Не указан postId или commentId')
      loading.value = false
      return
    }
    
    const res = await apiFetch(`${API_URL}/likes/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    })
    
    if (res.ok) {
      const data = await res.json()
      
      if (data.action === 'liked') {
        isLiked.value = true
        likesCount.value += 1
      } else if (data.action === 'unliked') {
        isLiked.value = false
        likesCount.value -= 1
      }
      
      emit('update', {
        likesCount: likesCount.value,
        isLiked: isLiked.value
      })
    } else {
      const error = await res.json()
      console.error('Ошибка:', error)
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
}
</script>