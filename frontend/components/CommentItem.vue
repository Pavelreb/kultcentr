<!-- frontend/components/CommentItem.vue -->
<template>
  <div :id="`comment-${comment.id}`" class="comment-item py-4 border-b border-gray-100 dark:border-gray-700 last:border-0 scroll-mt-24">
    <div class="flex gap-3">
      <!-- Аватар -->
      <NuxtLink :to="`/authors/${comment.author_id || 0}`" class="flex-shrink-0">
        <img 
          v-if="comment.author_avatar" 
          :src="comment.author_avatar" 
          :alt="getAuthorFullName(comment)"
          class="w-10 h-10 rounded-full object-cover"
        >
        <div 
          v-else
          class="w-10 h-10 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-sm font-bold"
        >
          {{ getInitials(getAuthorFullName(comment)) }}
        </div>
      </NuxtLink>
      
      <div class="flex-1 min-w-0">
        <!-- Автор и дата -->
        <div class="flex items-center gap-2 flex-wrap">
          <NuxtLink :to="`/authors/${comment.author_id || 0}`" class="font-semibold text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition">
            {{ getAuthorFullName(comment) }}
          </NuxtLink>
          <span class="text-xs text-gray-400 dark:text-gray-500">{{ formatDate(comment.created_at) }}</span>
          <span v-if="comment.updated_at !== comment.created_at" class="text-xs text-gray-400 dark:text-gray-500">(изменено)</span>
        </div>
        
        <!-- Текст комментария -->
        <div v-if="editingId === comment.id" class="mt-2">
          <textarea 
            v-model="editContent" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            rows="3"
          ></textarea>
          <div class="flex gap-2 mt-2">
            <button 
              @click="saveEdit"
              :disabled="savingEdit"
              class="px-3 py-1.5 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition text-sm"
            >
              {{ savingEdit ? 'Сохранение...' : 'Сохранить' }}
            </button>
            <button 
              @click="cancelEdit"
              class="px-3 py-1.5 bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600 transition text-sm"
            >
              Отмена
            </button>
          </div>
        </div>
        <p v-else class="text-gray-700 dark:text-gray-300 mt-1 leading-relaxed break-words">
          {{ comment.content }}
        </p>
        
        <!-- Действия -->
        <div class="flex items-center gap-4 mt-2 text-xs">
          <!-- Лайк -->
          <button 
            v-if="authStore.isAuthenticated"
            @click="toggleLike"
            class="flex items-center gap-1 text-gray-400 dark:text-gray-500 hover:text-red-500 dark:hover:text-red-400 transition"
          >
            <svg 
              class="w-4 h-4 transition"
              :class="comment.user_has_liked ? 'text-red-500 fill-red-500' : 'fill-none'"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <span>{{ comment.likes_count || 0 }}</span>
          </button>
          <span v-else class="flex items-center gap-1 text-gray-400 dark:text-gray-500">
            <svg class="w-4 h-4 fill-none" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <span>{{ comment.likes_count || 0 }}</span>
          </span>
          
          <!-- Ответить -->
          <button 
            v-if="authStore.isAuthenticated"
            @click="startReply"
            class="text-gray-400 dark:text-gray-500 hover:text-blue-600 dark:hover:text-blue-400 transition"
          >
            Ответить
          </button>
          
          <!-- Редактировать -->
          <button 
            v-if="comment.can_edit"
            @click="startEdit"
            class="text-gray-400 dark:text-gray-500 hover:text-blue-600 dark:hover:text-blue-400 transition"
          >
            Редактировать
          </button>
          
          <!-- Удалить -->
          <button 
            v-if="comment.can_delete"
            @click="deleteComment"
            class="text-gray-400 dark:text-gray-500 hover:text-red-600 dark:hover:text-red-400 transition"
          >
            Удалить
          </button>
        </div>
        
        <!-- Вложенные комментарии -->
        <div v-if="comment.replies && comment.replies.length > 0" class="mt-4 pl-4 border-l-2 border-gray-200 dark:border-gray-700 space-y-4">
          <CommentItem 
            v-for="reply in comment.replies" 
            :key="reply.id"
            :comment="reply"
            :editing-id="editingId"
            :saving-edit="savingEdit"
            @start-edit="startEdit"
            @start-reply="startReply"
            @save-edit="saveEdit"
            @cancel-edit="cancelEdit"
            @delete-comment="deleteComment"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const authStore = useAuthStore()
const { apiFetch } = useApi()

const props = defineProps({
  comment: {
    type: Object,
    required: true
  },
  editingId: {
    type: Number,
    default: null
  },
  savingEdit: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['start-edit', 'start-reply', 'save-edit', 'cancel-edit', 'delete-comment'])

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const editContent = ref('')

// ============================================
// ПОЛНОЕ ИМЯ АВТОРА
// ============================================
const getAuthorFullName = (comment) => {
  if (!comment) return 'Пользователь'
  
  // Если есть first_name и last_name
  if (comment.author_first_name || comment.author_last_name) {
    const parts = []
    if (comment.author_last_name) parts.push(comment.author_last_name)
    if (comment.author_first_name) parts.push(comment.author_first_name)
    if (parts.length > 0) return parts.join(' ')
  }
  // Если есть full_name
  if (comment.author_full_name) {
    return comment.author_full_name
  }
  // Fallback - username
  return comment.author_name || 'Пользователь'
}

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

// ============================================
// ФОРМАТИРОВАНИЕ ДАТЫ
// ============================================
const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'short',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

// ============================================
// ДЕЙСТВИЯ
// ============================================
const startReply = () => {
  emit('start-reply', props.comment.id, getAuthorFullName(props.comment))
}

const startEdit = () => {
  editContent.value = props.comment.content
  emit('start-edit', props.comment)
}

const cancelEdit = () => {
  editContent.value = ''
  emit('cancel-edit')
}

const saveEdit = () => {
  if (!editContent.value.trim()) return
  emit('save-edit', props.comment.id, editContent.value.trim())
}

const deleteComment = () => {
  emit('delete-comment', props.comment.id)
}

// ============================================
// ЛАЙК
// ============================================
const toggleLike = async () => {
  if (!authStore.isAuthenticated) {
    return
  }
  
  try {
    const res = await apiFetch(`${API_URL}/likes/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        comment: props.comment.id
      })
    })
    
    if (res.ok) {
      const data = await res.json()
      
      if (data.action === 'liked') {
        props.comment.likes_count = (props.comment.likes_count || 0) + 1
        props.comment.user_has_liked = true
      } else if (data.action === 'unliked') {
        props.comment.likes_count = (props.comment.likes_count || 0) - 1
        props.comment.user_has_liked = false
      }
    }
  } catch (e) {
    console.error('Ошибка:', e)
  }
}
</script>