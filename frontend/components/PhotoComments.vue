<template>
  <div class="mt-4">
    <h4 class="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">
      💬 Комментарии ({{ totalCommentsCount }})
    </h4>
    
    <!-- Список комментариев -->
    <div v-if="comments.length > 0" class="space-y-3 max-h-60 overflow-y-auto">
      <div 
        v-for="comment in comments" 
        :key="comment.id"
        class="bg-gray-50 dark:bg-gray-700 rounded-lg p-3"
      >
        <div class="flex justify-between items-start">
          <div class="flex items-center gap-2">
            <img 
              v-if="comment.user_avatar" 
              :src="comment.user_avatar" 
              :alt="comment.user_name"
              class="w-6 h-6 rounded-full object-cover"
            >
            <div 
              v-else
              class="w-6 h-6 rounded-full bg-blue-500 flex items-center justify-center text-white text-[10px] font-bold"
            >
              {{ getInitials(comment.user_name) }}
            </div>
            <span class="text-sm font-medium text-gray-800 dark:text-gray-200">
              {{ comment.user_name }}
            </span>
            <span class="text-xs text-gray-400 dark:text-gray-500">
              {{ formatDate(comment.created_at) }}
            </span>
          </div>
          
          <div v-if="comment.can_edit || comment.can_delete" class="flex gap-1">
            <button 
              v-if="comment.can_edit && editingId !== comment.id"
              @click="startEdit(comment)"
              class="text-yellow-500 hover:text-yellow-700 transition text-xs"
            >
              ✏️
            </button>
            <button 
              v-if="comment.can_delete"
              @click="$emit('delete-comment', comment.id)"
              class="text-red-500 hover:text-red-700 transition text-xs"
            >
              🗑️
            </button>
          </div>
        </div>
        
        <!-- Режим редактирования -->
        <div v-if="editingId === comment.id">
          <textarea 
            v-model="editContent"
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 mt-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-600 text-gray-800 dark:text-gray-200"
            rows="2"
          ></textarea>
          <div class="flex gap-2 mt-2">
            <button 
              @click="$emit('save-comment', comment.id, editContent)"
              class="bg-blue-500 text-white px-3 py-1 rounded text-sm hover:bg-blue-600 transition"
              :disabled="savingEdit"
            >
              {{ savingEdit ? 'Сохранение...' : 'Сохранить' }}
            </button>
            <button 
              @click="cancelEdit"
              class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-300 px-3 py-1 rounded text-sm hover:bg-gray-400 dark:hover:bg-gray-500 transition"
            >
              Отмена
            </button>
          </div>
        </div>
        
        <!-- Текст комментария -->
        <p v-else class="text-sm text-gray-700 dark:text-gray-300 mt-1">
          {{ comment.content }}
        </p>
        
        <!-- Ответы -->
        <div v-if="comment.replies && comment.replies.length > 0" class="ml-6 mt-2 pl-3 border-l-2 border-gray-200 dark:border-gray-600 space-y-2">
          <div 
            v-for="reply in comment.replies" 
            :key="reply.id"
            class="bg-gray-50 dark:bg-gray-700 rounded-lg p-2"
          >
            <div class="flex justify-between items-start">
              <div class="flex items-center gap-2">
                <img 
                  v-if="reply.user_avatar" 
                  :src="reply.user_avatar" 
                  :alt="reply.user_name"
                  class="w-5 h-5 rounded-full object-cover"
                >
                <div 
                  v-else
                  class="w-5 h-5 rounded-full bg-blue-500 flex items-center justify-center text-white text-[8px] font-bold"
                >
                  {{ getInitials(reply.user_name) }}
                </div>
                <span class="text-xs font-medium text-gray-800 dark:text-gray-200">
                  {{ reply.user_name }}
                </span>
                <span class="text-xs text-gray-400 dark:text-gray-500">
                  {{ formatDate(reply.created_at) }}
                </span>
              </div>
              
              <div v-if="reply.can_edit || reply.can_delete" class="flex gap-1">
                <button 
                  v-if="reply.can_edit && editingId !== reply.id"
                  @click="startEdit(reply)"
                  class="text-yellow-500 hover:text-yellow-700 transition text-xs"
                >
                  ✏️
                </button>
                <button 
                  v-if="reply.can_delete"
                  @click="$emit('delete-comment', reply.id)"
                  class="text-red-500 hover:text-red-700 transition text-xs"
                >
                  🗑️
                </button>
              </div>
            </div>
            
            <div v-if="editingId === reply.id">
              <textarea 
                v-model="editContent"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 mt-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-600 text-gray-800 dark:text-gray-200"
                rows="2"
              ></textarea>
              <div class="flex gap-2 mt-2">
                <button 
                  @click="$emit('save-comment', reply.id, editContent)"
                  class="bg-blue-500 text-white px-3 py-1 rounded text-sm hover:bg-blue-600 transition"
                  :disabled="savingEdit"
                >
                  {{ savingEdit ? 'Сохранение...' : 'Сохранить' }}
                </button>
                <button 
                  @click="cancelEdit"
                  class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-300 px-3 py-1 rounded text-sm hover:bg-gray-400 dark:hover:bg-gray-500 transition"
                >
                  Отмена
                </button>
              </div>
            </div>
            
            <p v-else class="text-xs text-gray-600 dark:text-gray-400 mt-1">
              {{ reply.content }}
            </p>
          </div>
        </div>
        
        <!-- Кнопка ответа -->
        <button 
          v-if="authStore.isAuthenticated && editingId !== comment.id"
          @click="$emit('start-reply', comment.id, comment.user_name)"
          class="text-xs text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition mt-1"
        >
          Ответить
        </button>
      </div>
    </div>
    
    <div v-else class="text-sm text-gray-400 dark:text-gray-500">
      Пока нет комментариев
    </div>
    
    <!-- Форма добавления комментария -->
    <div class="mt-4">
      <div v-if="replyToId" class="text-xs text-gray-500 dark:text-gray-400 mb-2">
        Ответ для <span class="font-semibold">{{ replyToName }}</span>
        <button 
          @click="cancelReply"
          class="text-red-500 hover:text-red-700 transition ml-2"
        >
          ✕
        </button>
      </div>
      
      <div v-if="authStore.isAuthenticated" class="flex gap-2">
        <input 
          v-model="newComment"
          type="text"
          :placeholder="replyToId ? 'Напишите ответ...' : 'Напишите комментарий...'"
          class="flex-1 border border-gray-300 dark:border-gray-600 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          @keyup.enter="submitComment"
        />
        <button 
          @click="submitComment"
          class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition text-sm disabled:opacity-50"
          :disabled="submitting || !newComment.trim()"
        >
          {{ submitting ? '...' : '📤' }}
        </button>
      </div>
      <p v-else class="text-sm text-gray-400 dark:text-gray-500">
        <NuxtLink to="/auth/login" class="text-blue-500 dark:text-blue-400 hover:underline">
          Войдите
        </NuxtLink>, чтобы оставить комментарий
      </p>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const props = defineProps({
  albumId: {
    type: Number,
    required: true
  },
  photoId: {
    type: Number,
    required: true
  },
  comments: {
    type: Array,
    required: true,
    default: () => []
  }
})

const emit = defineEmits([
  'comment-added',
  'comment-deleted',
  'comment-updated'
])

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()

const newComment = ref('')
const submitting = ref(false)
const replyToId = ref(null)
const replyToName = ref('')
const editingId = ref(null)
const editContent = ref('')
const savingEdit = ref(false)

const totalCommentsCount = computed(() => {
  let count = 0
  const countComments = (comments) => {
    comments.forEach(c => {
      count++
      if (c.replies && c.replies.length > 0) {
        countComments(c.replies)
      }
    })
  }
  countComments(props.comments)
  return count
})

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'short',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const submitComment = async () => {
  if (!newComment.value.trim()) return
  
  submitting.value = true
  
  try {
    const body = {
      content: newComment.value.trim()
    }
    
    if (replyToId.value) {
      body.parent = replyToId.value
    }
    
    const res = await apiFetch(`${API_URL}/albums/${props.albumId}/photos/${props.photoId}/comment/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    })
    
    if (res.ok) {
      const comment = await res.json()
      emit('comment-added', comment)
      newComment.value = ''
      cancelReply()
    } else {
      const error = await res.json()
      console.error('Ошибка:', error)
      alert('Ошибка при отправке комментария')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    submitting.value = false
  }
}

const startReply = (commentId, userName) => {
  replyToId.value = commentId
  replyToName.value = userName
}

const cancelReply = () => {
  replyToId.value = null
  replyToName.value = ''
}

const startEdit = (comment) => {
  editingId.value = comment.id
  editContent.value = comment.content
}

const cancelEdit = () => {
  editingId.value = null
  editContent.value = ''
}

// Обработка Enter
const handleKeydown = (event) => {
  if (event.key === 'Escape') {
    cancelEdit()
    cancelReply()
  }
}

onMounted(() => {
  document.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  document.removeEventListener('keydown', handleKeydown)
})
</script>