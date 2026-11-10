<!-- frontend/pages/profile/index.vue -->
<template>
  <div class="max-w-4xl mx-auto mt-10 px-4">
    <!-- Заголовок -->
    <div class="flex items-center gap-3 mb-6">
      <div class="p-2 rounded-xl bg-blue-100 dark:bg-blue-900/30">
        <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
        </svg>
      </div>
      <div>
        <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200">Мой профиль</h1>
        <p class="text-sm text-gray-500 dark:text-gray-400">Управление личной информацией</p>
      </div>
    </div>
    
    <div v-if="loading" class="text-center py-10">
      <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="error" class="text-red-500 text-center py-10">
      <svg class="w-16 h-16 mx-auto text-red-400 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
      </svg>
      {{ error }}
    </div>
    
    <div v-else>
      <!-- Карточка профиля -->
      <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 overflow-hidden">
        <div class="p-6 md:p-8">
          <!-- Аватар и имя -->
          <div class="flex flex-col items-center md:flex-row md:items-start gap-6">
            <div class="relative flex-shrink-0">
              <div class="w-32 h-32 rounded-full bg-gradient-to-br from-blue-400 to-purple-600 p-1">
                <div class="w-full h-full rounded-full bg-white dark:bg-gray-800 overflow-hidden">
                  <img 
                    v-if="avatarPreview" 
                    :src="avatarPreview" 
                    alt="Аватар"
                    class="w-full h-full object-cover"
                  >
                  <div 
                    v-else 
                    class="w-full h-full flex items-center justify-center text-4xl font-bold text-white bg-gradient-to-br from-blue-400 to-blue-600"
                  >
                    {{ userInitials }}
                  </div>
                </div>
              </div>
              <!-- Статус "онлайн" (заглушка) -->
              <div class="absolute bottom-1 right-1 w-4 h-4 bg-green-500 border-2 border-white dark:border-gray-800 rounded-full"></div>
            </div>
            
            <div class="flex-1 text-center md:text-left">
              <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200">{{ fullName || username }}</h2>
              <div class="flex items-center justify-center md:justify-start gap-2 mt-1">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                  </svg>
                  {{ roleDisplay }}
                </span>
                <span class="text-sm text-gray-400 dark:text-gray-500">•</span>
                <span class="text-sm text-gray-400 dark:text-gray-500 flex items-center gap-1">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                  </svg>
                  {{ formatDate(dateJoined) }}
                </span>
              </div>
              <p v-if="bio" class="text-gray-600 dark:text-gray-300 mt-3 max-w-md mx-auto md:mx-0">
                {{ bio }}
              </p>
            </div>
          </div>
        </div>
        
        <!-- Информация -->
        <div class="border-t border-gray-100 dark:border-gray-700 p-6 md:p-8">
          <h3 class="text-sm font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider mb-4 flex items-center gap-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            Личная информация
          </h3>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl">
              <p class="text-xs text-gray-400 dark:text-gray-500">Имя</p>
              <p class="text-gray-800 dark:text-gray-200 font-medium">{{ form.first_name || '—' }}</p>
            </div>
            <div class="p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl">
              <p class="text-xs text-gray-400 dark:text-gray-500">Фамилия</p>
              <p class="text-gray-800 dark:text-gray-200 font-medium">{{ form.last_name || '—' }}</p>
            </div>
            <div class="p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl">
              <p class="text-xs text-gray-400 dark:text-gray-500">Отчество</p>
              <p class="text-gray-800 dark:text-gray-200 font-medium">{{ form.patronymic || '—' }}</p>
            </div>
            <div class="p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl">
              <p class="text-xs text-gray-400 dark:text-gray-500">Email</p>
              <p class="text-gray-800 dark:text-gray-200 font-medium">{{ form.email || '—' }}</p>
            </div>
            <div class="p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl">
              <p class="text-xs text-gray-400 dark:text-gray-500">Дата рождения</p>
              <p class="text-gray-800 dark:text-gray-200 font-medium">{{ form.birth_date ? formatDate(form.birth_date) : '—' }}</p>
            </div>
            <div class="p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl">
              <p class="text-xs text-gray-400 dark:text-gray-500">Имя пользователя</p>
              <p class="text-gray-800 dark:text-gray-200 font-medium">{{ form.username }}</p>
            </div>
          </div>
          
          <div v-if="bio" class="mt-4 p-3 bg-gray-50 dark:bg-gray-700/50 rounded-xl">
            <p class="text-xs text-gray-400 dark:text-gray-500">О себе</p>
            <p class="text-gray-800 dark:text-gray-200 font-medium whitespace-pre-wrap">{{ bio }}</p>
          </div>
        </div>
        
        <!-- Кнопка редактирования -->
        <div class="border-t border-gray-100 dark:border-gray-700 p-6 md:p-8">
          <NuxtLink to="/profile/edit" class="block">
            <button class="w-full inline-flex items-center justify-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
              </svg>
              Редактировать профиль
            </button>
          </NuxtLink>
        </div>
      </div>
      
      <!-- ========================================== -->
      <!-- СТАТИСТИКА АВТОРСТВА                      -->
      <!-- ========================================== -->
      <div v-if="authStore.isAuthor || authStore.isEditor" class="mt-8">
        <div class="flex items-center gap-3 mb-4">
          <div class="p-2 rounded-xl bg-purple-100 dark:bg-purple-900/30">
            <svg class="w-5 h-5 text-purple-600 dark:text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
            </svg>
          </div>
          <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">Статистика авторства</h2>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 p-5 text-center">
            <svg class="w-6 h-6 mx-auto text-green-500 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
            </svg>
            <div class="text-2xl font-bold text-gray-800 dark:text-gray-200">{{ form.posts_count }}</div>
            <div class="text-xs text-gray-400 dark:text-gray-500 mt-1">Публикаций</div>
          </div>
          <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 p-5 text-center">
            <svg class="w-6 h-6 mx-auto text-blue-500 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
            </svg>
            <div class="text-2xl font-bold text-gray-800 dark:text-gray-200">{{ form.total_views }}</div>
            <div class="text-xs text-gray-400 dark:text-gray-500 mt-1">Просмотров</div>
          </div>
          <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 p-5 text-center">
            <svg class="w-6 h-6 mx-auto text-red-500 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <div class="text-2xl font-bold text-gray-800 dark:text-gray-200">{{ form.total_likes }}</div>
            <div class="text-xs text-gray-400 dark:text-gray-500 mt-1">Лайков</div>
          </div>
          <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 p-5 text-center">
            <svg class="w-6 h-6 mx-auto text-amber-500 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
            </svg>
            <div class="text-2xl font-bold text-gray-800 dark:text-gray-200">{{ form.total_comments }}</div>
            <div class="text-xs text-gray-400 dark:text-gray-500 mt-1">Комментариев</div>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- МОИ ПУБЛИКАЦИИ                           -->
      <!-- ========================================== -->
      <div v-if="authStore.isAuthor || authStore.isEditor" class="mt-8">
        <div class="flex items-center gap-3 mb-4">
          <div class="p-2 rounded-xl bg-green-100 dark:bg-green-900/30">
            <svg class="w-5 h-5 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
            </svg>
          </div>
          <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">Мои публикации</h2>
        </div>
        
        <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 p-6">
          <div class="flex flex-wrap gap-2 mb-4">
            <button 
              @click="postFilter = 'all'"
              class="px-4 py-1.5 rounded-lg text-sm font-medium transition"
              :class="postFilter === 'all' 
                ? 'bg-blue-500 text-white shadow-md' 
                : 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'"
            >
              Все
            </button>
            <button 
              @click="postFilter = 'published'"
              class="px-4 py-1.5 rounded-lg text-sm font-medium transition"
              :class="postFilter === 'published' 
                ? 'bg-green-500 text-white shadow-md' 
                : 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'"
            >
              Опубликованные
            </button>
            <button 
              @click="postFilter = 'draft'"
              class="px-4 py-1.5 rounded-lg text-sm font-medium transition"
              :class="postFilter === 'draft' 
                ? 'bg-yellow-500 text-white shadow-md' 
                : 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'"
            >
              Черновики
            </button>
          </div>
          
          <div v-if="userPostsLoading" class="text-center py-6">
            <svg class="w-8 h-8 mx-auto text-gray-300 dark:text-gray-600 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
            </svg>
          </div>
          
          <div v-else-if="filteredPosts.length === 0" class="text-center py-6 text-gray-500 dark:text-gray-400">
            Нет постов
          </div>
          
          <div v-else class="space-y-3">
            <div 
              v-for="post in filteredPosts" 
              :key="post.id" 
              class="bg-gray-50 dark:bg-gray-700/50 p-4 rounded-xl hover:shadow transition flex gap-4"
            >
              <div v-if="post.display_image" class="h-20 w-20 rounded-lg overflow-hidden flex-shrink-0">
                <img :src="post.display_image" :alt="post.title" class="w-full h-full object-cover">
              </div>
              <div v-else class="h-20 w-20 bg-gradient-to-r from-gray-200 to-gray-300 dark:from-gray-600 dark:to-gray-500 rounded-lg flex items-center justify-center flex-shrink-0">
                <svg class="w-8 h-8 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9"/>
                </svg>
              </div>
              
              <NuxtLink :to="post.is_published ? `/posts/${post.id}` : `/posts/edit-${post.id}`" class="block flex-1 min-w-0" @click="saveProfileScroll">
                <h3 class="text-base font-semibold text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition">
                  {{ post.title }}
                </h3>
                <p class="text-gray-500 dark:text-gray-400 text-sm mt-0.5 line-clamp-1">{{ post.excerpt || post.content?.substring(0, 100) }}...</p>
                <div class="flex items-center gap-3 mt-1">
                  <span class="text-xs text-gray-400 dark:text-gray-500 flex items-center gap-1">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                    </svg>
                    {{ formatDate(post.created_at) }}
                  </span>
                  <span v-if="post.is_published" class="text-xs bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300 px-2 py-0.5 rounded-full">
                    Опубликовано
                  </span>
                  <span v-else class="text-xs bg-yellow-100 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-300 px-2 py-0.5 rounded-full">
                    Черновик
                  </span>
                </div>
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
      
      <!-- ========================================== -->
      <!-- МОИ СОБЫТИЯ (для редактора)              -->
      <!-- ========================================== -->
      <div v-if="authStore.isEditor" class="mt-8">
        <div class="flex items-center gap-3 mb-4">
          <div class="p-2 rounded-xl bg-blue-100 dark:bg-blue-900/30">
            <svg class="w-5 h-5 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
            </svg>
          </div>
          <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">Мои события</h2>
        </div>
        
        <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 p-6">
          <div class="flex flex-wrap gap-2 mb-4">
            <button 
              @click="eventFilter = 'all'"
              class="px-4 py-1.5 rounded-lg text-sm font-medium transition"
              :class="eventFilter === 'all' 
                ? 'bg-blue-500 text-white shadow-md' 
                : 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'"
            >
              Все
            </button>
            <button 
              @click="eventFilter = 'published'"
              class="px-4 py-1.5 rounded-lg text-sm font-medium transition"
              :class="eventFilter === 'published' 
                ? 'bg-green-500 text-white shadow-md' 
                : 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'"
            >
              Опубликованные
            </button>
            <button 
              @click="eventFilter = 'draft'"
              class="px-4 py-1.5 rounded-lg text-sm font-medium transition"
              :class="eventFilter === 'draft' 
                ? 'bg-yellow-500 text-white shadow-md' 
                : 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'"
            >
              Черновики
            </button>
          </div>
          
          <div v-if="userEventsLoading" class="text-center py-6">
            <svg class="w-8 h-8 mx-auto text-gray-300 dark:text-gray-600 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
            </svg>
          </div>
          
          <div v-else-if="filteredEvents.length === 0" class="text-center py-6 text-gray-500 dark:text-gray-400">
            Нет событий
          </div>
          
          <div v-else class="space-y-3">
            <div 
              v-for="event in filteredEvents" 
              :key="event.id" 
              class="bg-gray-50 dark:bg-gray-700/50 p-4 rounded-xl hover:shadow transition"
            >
              <NuxtLink :to="event.is_published ? `/events/${event.id}` : `/events/edit-${event.id}`" class="block" @click="saveProfileScroll">
                <h3 class="text-base font-semibold text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition">
                  {{ event.title }}
                </h3>
                <p class="text-gray-500 dark:text-gray-400 text-sm mt-0.5">{{ event.excerpt || event.content?.substring(0, 100) }}...</p>
                <div class="flex items-center gap-3 mt-1">
                  <span v-if="event.event_date" class="text-xs text-gray-400 dark:text-gray-500 flex items-center gap-1">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                    </svg>
                    {{ formatDateTime(event.event_date) }}
                  </span>
                  <span v-if="event.is_published" class="text-xs bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300 px-2 py-0.5 rounded-full">
                    Опубликовано
                  </span>
                  <span v-else class="text-xs bg-yellow-100 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-300 px-2 py-0.5 rounded-full">
                    Черновик
                  </span>
                </div>
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
      
      <!-- ========================================== -->
      <!-- МОИ КОММЕНТАРИИ                          -->
      <!-- ========================================== -->
      <div v-if="authStore.isAuthenticated" class="mt-8 mb-10">
        <div class="flex items-center gap-3 mb-4">
          <div class="p-2 rounded-xl bg-purple-100 dark:bg-purple-900/30">
            <svg class="w-5 h-5 text-purple-600 dark:text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
            </svg>
          </div>
          <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">Мои комментарии</h2>
        </div>
        
        <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 p-6">
          <div v-if="userCommentsLoading" class="text-center py-6">
            <svg class="w-8 h-8 mx-auto text-gray-300 dark:text-gray-600 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
            </svg>
          </div>
          
          <div v-else-if="allComments.length === 0" class="text-center py-6 text-gray-500 dark:text-gray-400">
            Нет комментариев
          </div>
          
          <div v-else class="space-y-3">
            <div 
              v-for="comment in allComments.slice(0, 10)" 
              :key="comment.id" 
              class="bg-gray-50 dark:bg-gray-700/50 p-4 rounded-xl hover:shadow transition"
            >
              <NuxtLink
                :to="comment.type === 'post' ? `/posts/${comment.post}#comment-${comment.id}` : `/gallery/${comment.album}?photo=${comment.photo}#photo-comment-${comment.id}`"
                class="block"
                @click="saveProfileScroll"
              >
                <p class="text-gray-700 dark:text-gray-300">{{ comment.content }}</p>
                <div class="flex items-center gap-3 mt-1">
                  <span class="text-xs text-gray-400 dark:text-gray-500 flex items-center gap-1">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                    </svg>
                    {{ formatDate(comment.created_at) }}
                  </span>
                  <span class="text-xs px-2 py-0.5 rounded-full" :class="comment.type === 'post' ? 'bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300' : 'bg-pink-100 dark:bg-pink-900 text-pink-700 dark:text-pink-300'">
                    {{ comment.type === 'post' ? 'К посту' : 'В галерее' }}
                  </span>
                </div>
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

useSeoMeta({
  title: 'Мой профиль'
})

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()
const router = useRouter()

// ============================================
// ПРОФИЛЬ
// ============================================
const loading = ref(true)
const error = ref('')
const avatarPreview = ref(null)

const form = ref({
  username: '',
  first_name: '',
  last_name: '',
  patronymic: '',
  email: '',
  birth_date: '',
  bio: '',
  role_display: '',
  date_joined: '',
  posts_count: 0,
  total_views: 0,
  total_likes: 0,
  total_comments: 0
})

const fullName = computed(() => {
  const parts = []
  if (form.value.last_name) parts.push(form.value.last_name)
  if (form.value.first_name) parts.push(form.value.first_name)
  if (form.value.patronymic) parts.push(form.value.patronymic)
  return parts.length ? parts.join(' ') : form.value.username
})

const username = computed(() => form.value.username)
const roleDisplay = computed(() => form.value.role_display)
const bio = computed(() => form.value.bio)
const dateJoined = computed(() => form.value.date_joined)

const userInitials = computed(() => {
  if (avatarPreview.value) return ''
  if (form.value.first_name && form.value.last_name) {
    return `${form.value.first_name[0]}${form.value.last_name[0]}`.toUpperCase()
  }
  if (form.value.first_name) {
    return form.value.first_name[0].toUpperCase()
  }
  return form.value.username?.[0]?.toUpperCase() || '?'
})

// ============================================
// ПОСТЫ
// ============================================
const userPosts = ref([])
const userPostsLoading = ref(true)
const postFilter = ref('all')

const filteredPosts = computed(() => {
  if (postFilter.value === 'published') {
    return userPosts.value.filter(p => p.is_published)
  }
  if (postFilter.value === 'draft') {
    return userPosts.value.filter(p => !p.is_published)
  }
  return userPosts.value
})

// ============================================
// СОБЫТИЯ
// ============================================
const userEvents = ref([])
const userEventsLoading = ref(true)
const eventFilter = ref('all')

const filteredEvents = computed(() => {
  if (eventFilter.value === 'published') {
    return userEvents.value.filter(e => e.is_published)
  }
  if (eventFilter.value === 'draft') {
    return userEvents.value.filter(e => !e.is_published)
  }
  return userEvents.value
})

// ============================================
// КОММЕНТАРИИ
// ============================================
const allComments = ref([])
const userCommentsLoading = ref(true)

// ============================================
// ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
// ============================================
const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

const formatDateTime = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

// ============================================
// ЗАГРУЗКА ДАННЫХ
// ============================================
const loadProfile = async () => {
  try {
    const res = await apiFetch(`${API_URL}/auth/users/me/`, {
    })
    
    if (res.ok) {
      const user = await res.json()
      form.value = {
        username: user.username,
        first_name: user.first_name || '',
        last_name: user.last_name || '',
        patronymic: user.patronymic || '',
        email: user.email || '',
        birth_date: user.birth_date || '',
        bio: user.bio || '',
        role_display: user.role_display || '',
        date_joined: user.date_joined || '',
        posts_count: user.posts_count || 0,
        total_views: user.total_views || 0,
        total_likes: user.total_likes || 0,
        total_comments: user.total_comments || 0
      }
      
      if (user.avatar_url) {
        avatarPreview.value = user.avatar_url
      }
    } else {
      error.value = 'Не удалось загрузить профиль'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    loading.value = false
  }
}

const loadUserPosts = async () => {
  try {
    const res = await apiFetch(`${API_URL}/posts/my_posts/`, {
    })
    
    if (res.ok) {
      userPosts.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка загрузки постов:', e)
  } finally {
    userPostsLoading.value = false
  }
}

const loadUserEvents = async () => {
  try {
    const res = await apiFetch(`${API_URL}/events/my_events/`, {
    })
    
    if (res.ok) {
      userEvents.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка загрузки событий:', e)
  } finally {
    userEventsLoading.value = false
  }
}

// ============================================
// Возврат «назад» к тому же месту профиля:
// при клике на пост/событие/комментарий запоминаем
// скролл, при возврате — восстанавливаем (одноразово)
// ============================================
const PROFILE_SCROLL_KEY = 'profile_scroll'

const saveProfileScroll = () => {
  sessionStorage.setItem(PROFILE_SCROLL_KEY, String(window.scrollY))
}

const restoreProfileScroll = async () => {
  const saved = sessionStorage.getItem(PROFILE_SCROLL_KEY)
  if (!saved) return
  sessionStorage.removeItem(PROFILE_SCROLL_KEY)
  await nextTick()
  smoothScrollTo(Number(saved))
}

const loadUserComments = async () => {
  try {
    let comments = []

    try {
      const postCommentsRes = await apiFetch(`${API_URL}/comments/my_comments/`, {
      })

      if (postCommentsRes.ok) {
        const data = await postCommentsRes.json()
        comments = [...comments, ...data.map(c => ({ ...c, type: 'post' }))]
      }
    } catch (e) {
      console.error('Ошибка загрузки комментариев к постам:', e)
    }

    try {
      const photoCommentsRes = await apiFetch(`${API_URL}/photo-comments/my_comments/`, {
      })

      if (photoCommentsRes.ok) {
        const data = await photoCommentsRes.json()
        comments = [...comments, ...data.map(c => ({ ...c, type: 'photo' }))]
      }
    } catch (e) {
      console.error('Ошибка загрузки комментариев к фото:', e)
    }

    comments.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
    allComments.value = comments
  } catch (e) {
    console.error('Ошибка загрузки комментариев:', e)
  } finally {
    userCommentsLoading.value = false
  }
}

// ============================================
// ЖИЗНЕННЫЙ ЦИКЛ
// ============================================
onMounted(async () => {
  authStore.restoreAuth()
  await loadProfile()
  
  if (authStore.isAuthor || authStore.isEditor) {
    await loadUserPosts()
  }
  
  if (authStore.isEditor) {
    await loadUserEvents()
  }
  
  if (authStore.isAuthenticated) {
    await loadUserComments()
  }

  // Все секции отрисованы — восстанавливаем позицию скролла (возврат «назад»)
  restoreProfileScroll()
})
</script>

<style scoped>
.line-clamp-1 {
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>