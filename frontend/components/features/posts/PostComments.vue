<!-- frontend/components/features/posts/PostComments.vue -->
<template>
  <div class="mt-8 bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700">
    <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-4 flex items-center gap-2">
      <svg class="w-6 h-6 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
      </svg>
      Комментарии ({{ totalCommentsCount }})
    </h2>

    <div v-if="comments?.length === 0" class="text-gray-500 dark:text-gray-400 text-center py-8">
      Пока нет комментариев. Будьте первым!
    </div>

    <div v-else>
      <CommentItem 
        v-for="comment in comments" 
        :key="comment.id"
        :comment="comment"
        :editing-id="editingCommentId"
        :saving-edit="savingEdit"
        @start-edit="startEditComment"
        @start-reply="(commentId, authorName) => startReplyComment(commentId, authorName)"
        @save-edit="saveEditComment"
        @cancel-edit="cancelEditComment"
        @delete-comment="deleteComment"
      />
    </div>
  </div>

  <!-- Форма добавления комментария -->
  <div class="mt-6 bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700">
    <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-3">
      {{ replyToCommentId ? 'Ответ на комментарий' : 'Добавить комментарий' }}
    </h3>
    
    <div v-if="replyToCommentId" class="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg mb-3 border border-gray-200 dark:border-gray-600">
      <p class="text-sm text-gray-600 dark:text-gray-300">
        Ответ для <span class="font-semibold">{{ replyToAuthorName }}</span>:
      </p>
      <button 
        @click="cancelReply"
        class="text-red-500 text-sm hover:text-red-700 transition"
      >
        Отменить ответ
      </button>
    </div>
    
    <form v-if="isAuthenticated" @submit.prevent="submitComment">
      <textarea 
        v-model="newComment" 
        class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" 
        rows="3" 
        placeholder="Напишите ваш комментарий..."
        required
      ></textarea>
      <UiButton 
        type="submit"
        variant="primary"
        :disabled="submitting"
        class="mt-2"
      >
        {{ submitting ? 'Отправка...' : replyToCommentId ? 'Ответить' : 'Отправить' }}
      </UiButton>
    </form>
    
    <div v-else class="text-center py-3 text-gray-500 dark:text-gray-400">
      <NuxtLink to="/auth/login" class="text-blue-500 dark:text-blue-400 hover:underline">
        Войдите
      </NuxtLink>, чтобы оставить комментарий
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'

const authStore = useAuthStore()

const props = defineProps({
  postId: {
    type: Number,
    required: true
  },
  comments: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits(['comment-added', 'comment-deleted', 'comment-updated'])

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const isAuthenticated = computed(() => authStore.isAuthenticated)

// ============================================
// СОСТОЯНИЕ
// ============================================
const newComment = ref('')
const submitting = ref(false)
const replyToCommentId = ref(null)
const replyToAuthorName = ref('')
const editingCommentId = ref(null)
const savingEdit = ref(false)

// ============================================
// ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
// ============================================
const totalCommentsCount = computed(() => {
  if (!props.comments || props.comments.length === 0) return 0
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

const findComment = (comments, id) => {
  if (!comments) return null
  for (const comment of comments) {
    if (comment.id === id) {
      return comment
    }
    if (comment.replies && comment.replies.length > 0) {
      const found = findComment(comment.replies, id)
      if (found) return found
    }
  }
  return null
}

// ============================================
// ОТПРАВКА КОММЕНТАРИЯ
// ============================================
const submitComment = async () => {
  if (!newComment.value.trim()) return
  
  submitting.value = true
  
  try {
    const body = {
      post: props.postId,
      content: newComment.value.trim()
    }
    
    if (replyToCommentId.value) {
      body.parent = replyToCommentId.value
    }
    
    const res = await fetch(`${API_URL}/comments/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify(body)
    })
    
    if (res.ok) {
      const comment = await res.json()
      
      // Обновляем локальные комментарии
      if (replyToCommentId.value) {
        const parentComment = findComment(props.comments, replyToCommentId.value)
        if (parentComment) {
          if (!parentComment.replies) {
            parentComment.replies = []
          }
          parentComment.replies.push(comment)
        }
      } else {
        if (props.comments) {
          props.comments.push(comment)
        }
      }
      
      emit('comment-added', comment)
      newComment.value = ''
      cancelReply()
    } else {
      const error = await res.json()
      console.error('Ошибка сервера:', error)
      alert('Ошибка при отправке комментария')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    submitting.value = false
  }
}

// ============================================
// ОТВЕТ НА КОММЕНТАРИЙ
// ============================================
const startReplyComment = (commentId, authorName) => {
  replyToCommentId.value = commentId
  replyToAuthorName.value = authorName
}

const cancelReply = () => {
  replyToCommentId.value = null
  replyToAuthorName.value = ''
}

// ============================================
// РЕДАКТИРОВАНИЕ КОММЕНТАРИЯ
// ============================================
const startEditComment = (comment) => {
  editingCommentId.value = comment.id
}

const cancelEditComment = () => {
  editingCommentId.value = null
}

const saveEditComment = async (commentId, content) => {
  if (!content.trim()) return
  
  savingEdit.value = true
  
  try {
    const res = await fetch(`${API_URL}/comments/${commentId}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify({
        content: content.trim()
      })
    })
    
    if (res.ok) {
      const updatedComment = await res.json()
      
      const updateCommentInTree = (comments) => {
        for (let i = 0; i < comments.length; i++) {
          if (comments[i].id === commentId) {
            comments[i] = updatedComment
            return true
          }
          if (comments[i].replies && comments[i].replies.length > 0) {
            if (updateCommentInTree(comments[i].replies)) {
              return true
            }
          }
        }
        return false
      }
      
      updateCommentInTree(props.comments)
      emit('comment-updated', updatedComment)
      cancelEditComment()
    } else {
      const error = await res.json()
      console.error('Ошибка:', error)
      alert('Ошибка при редактировании комментария')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    savingEdit.value = false
  }
}

// ============================================
// УДАЛЕНИЕ КОММЕНТАРИЯ
// ============================================
const deleteComment = async (commentId) => {
  if (!confirm('Вы уверены, что хотите удалить этот комментарий?')) return
  
  try {
    const res = await fetch(`${API_URL}/comments/${commentId}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      const removeCommentFromTree = (comments) => {
        for (let i = 0; i < comments.length; i++) {
          if (comments[i].id === commentId) {
            comments.splice(i, 1)
            return true
          }
          if (comments[i].replies && comments[i].replies.length > 0) {
            if (removeCommentFromTree(comments[i].replies)) {
              return true
            }
          }
        }
        return false
      }
      
      removeCommentFromTree(props.comments)
      emit('comment-deleted', commentId)
    } else {
      const error = await res.json()
      console.error('Ошибка:', error)
      alert('Ошибка при удалении комментария')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  }
}

// ============================================
// ЭКСПОЗИЦИЯ ДЛЯ РОДИТЕЛЬСКОГО КОМПОНЕНТА
// ============================================
defineExpose({
  totalCommentsCount,
  startReplyComment,
  cancelReply,
  startEditComment,
  cancelEditComment,
  saveEditComment,
  deleteComment
})
</script>