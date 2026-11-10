<!-- frontend/pages/profile/edit.vue -->
<template>
  <div class="max-w-4xl mx-auto mt-10 px-4">
    <!-- Заголовок -->
    <div class="flex items-center gap-3 mb-6">
      <div class="p-2 rounded-xl bg-amber-100 dark:bg-amber-900/30">
        <svg class="w-6 h-6 text-amber-600 dark:text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
        </svg>
      </div>
      <div>
        <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200">Редактировать профиль</h1>
        <p class="text-sm text-gray-500 dark:text-gray-400">Измените вашу личную информацию</p>
      </div>
    </div>
    
    <div class="flex items-center gap-2 mb-6">
      <NuxtLink to="/profile" class="text-sm text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition flex items-center gap-1.5">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
        </svg>
        Назад к профилю
      </NuxtLink>
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
    
    <form v-else @submit.prevent="updateProfile" enctype="multipart/form-data">
      <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 overflow-hidden">
        <!-- Аватар -->
        <div class="p-6 md:p-8 border-b border-gray-100 dark:border-gray-700">
          <div class="flex flex-col items-center">
            <div class="relative">
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
              <button 
                type="button"
                @click="triggerFileInput"
                class="absolute bottom-1 right-1 bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center hover:bg-blue-600 transition shadow-lg hover:scale-110"
                title="Загрузить аватар"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
              </button>
            </div>
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-2">Рекомендуемый размер: 512x512px. Максимум 2MB.</p>
            <input 
              ref="fileInput"
              type="file" 
              accept="image/*"
              class="hidden"
              @change="onAvatarSelected"
            />
          </div>
        </div>
        
        <!-- Форма -->
        <div class="p-6 md:p-8 space-y-4">
          <!-- Имя пользователя -->
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
              <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
              </svg>
              Имя пользователя
            </label>
            <input 
              v-model="form.username"
              type="text"
              disabled
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 bg-gray-100 dark:bg-gray-700/50 text-gray-500 dark:text-gray-400 cursor-not-allowed"
            />
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
                <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                </svg>
                Имя
              </label>
              <input 
                v-model="form.first_name"
                type="text"
                placeholder="Введите имя"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              />
            </div>
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
                <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                </svg>
                Фамилия
              </label>
              <input 
                v-model="form.last_name"
                type="text"
                placeholder="Введите фамилию"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              />
            </div>
          </div>
          
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
              <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
              </svg>
              Отчество
            </label>
            <input 
              v-model="form.patronymic"
              type="text"
              placeholder="Введите отчество"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            />
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
                <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                </svg>
                Email
              </label>
              <input
                v-model="form.email"
                type="email"
                placeholder="example@mail.com"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              />
              <label class="flex items-center gap-2 mt-2 text-xs text-gray-500 dark:text-gray-400 cursor-pointer">
                <input type="checkbox" v-model="form.show_email" class="w-4 h-4 rounded text-blue-600" />
                Показывать email на моей публичной странице
              </label>
            </div>
            <div>
              <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
                <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                </svg>
                Телефон
              </label>
              <input
                v-model="form.phone"
                type="tel"
                placeholder="+7 (999) 123-45-67"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              />
              <label class="flex items-center gap-2 mt-2 text-xs text-gray-500 dark:text-gray-400 cursor-pointer">
                <input type="checkbox" v-model="form.show_phone" class="w-4 h-4 rounded text-blue-600" />
                Показывать телефон на моей публичной странице
              </label>
            </div>
          </div>
          
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
              <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
              Дата рождения
            </label>
            <input 
              v-model="form.birth_date"
              type="date"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            />
          </div>
          
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
              <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
              </svg>
              О себе
            </label>
            <textarea 
              v-model="form.bio"
              placeholder="Расскажите о себе..."
              rows="4"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            ></textarea>
          </div>
          
          <div class="border-t border-gray-100 dark:border-gray-700 pt-4">
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
              <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/>
              </svg>
              Социальные сети
            </label>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <input
                v-model="form.vk"
                type="url"
                placeholder="ВКонтакте: https://vk.com/…"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              />
              <input
                v-model="form.max"
                type="url"
                placeholder="MAX: https://max.ru/…"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              />
              <input
                v-model="form.ok"
                type="url"
                placeholder="Одноклассники: https://ok.ru/…"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              />
              <input
                v-model="form.rutube"
                type="url"
                placeholder="RuTube: https://rutube.ru/…"
                class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              />
            </div>
            <label class="flex items-center gap-2 mt-2 text-xs text-gray-500 dark:text-gray-400 cursor-pointer">
              <input type="checkbox" v-model="form.show_socials" class="w-4 h-4 rounded text-blue-600" />
              Показывать соцсети на моей публичной странице
            </label>
          </div>

          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
              <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
              </svg>
              Роль
            </label>
            <input 
              v-model="form.role_display"
              type="text"
              disabled
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 bg-gray-100 dark:bg-gray-700/50 text-gray-500 dark:text-gray-400 cursor-not-allowed"
            />
          </div>
        </div>
        
        <!-- Кнопки -->
        <div class="border-t border-gray-100 dark:border-gray-700 p-6 md:p-8 flex flex-wrap gap-3">
          <button 
            type="submit" 
            :disabled="submitting"
            class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/>
            </svg>
            {{ submitting ? 'Сохранение...' : 'Сохранить изменения' }}
          </button>
          
          <NuxtLink to="/profile">
            <button type="button" class="inline-flex items-center gap-2 px-6 py-3 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 font-medium hover:-translate-y-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
              Отмена
            </button>
          </NuxtLink>
        </div>
        
        <p v-if="successMessage" class="px-6 pb-6 text-green-500 text-sm flex items-center gap-1.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          {{ successMessage }}
        </p>
        <p v-if="submitError" class="px-6 pb-6 text-red-500 text-sm flex items-center gap-1.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
          </svg>
          {{ submitError }}
        </p>
      </div>
    </form>
    
    <!-- ========================================== -->
    <!-- СМЕНА ПАРОЛЯ                             -->
    <!-- ========================================== -->
    <div class="mt-8 bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 overflow-hidden">
      <button 
        @click="showChangePassword = !showChangePassword"
        class="w-full p-6 flex items-center justify-between hover:bg-gray-50 dark:hover:bg-gray-700/50 transition"
      >
        <div class="flex items-center gap-3">
          <div class="p-2 rounded-xl bg-red-100 dark:bg-red-900/30">
            <svg class="w-5 h-5 text-red-600 dark:text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
            </svg>
          </div>
          <span class="text-lg font-semibold text-gray-800 dark:text-gray-200">Смена пароля</span>
        </div>
        <svg class="w-5 h-5 text-gray-400 transition-transform" :class="showChangePassword ? 'rotate-180' : ''" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
        </svg>
      </button>
      
      <div v-if="showChangePassword" class="border-t border-gray-100 dark:border-gray-700 p-6 md:p-8">
        <form @submit.prevent="changePassword" class="space-y-4">
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
              <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
              </svg>
              Текущий пароль
            </label>
            <input 
              v-model="passwordForm.old_password"
              type="password"
              placeholder="Введите текущий пароль"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              required
            />
          </div>
          
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
              <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
              </svg>
              Новый пароль
            </label>
            <input 
              v-model="passwordForm.new_password"
              type="password"
              placeholder="Введите новый пароль"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              required
            />
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Минимум 8 символов</p>
          </div>
          
          <div>
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium flex items-center gap-1.5">
              <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
              </svg>
              Подтвердите пароль
            </label>
            <input 
              v-model="passwordForm.new_password2"
              type="password"
              placeholder="Повторите новый пароль"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              required
            />
          </div>
          
          <div class="flex flex-wrap gap-3 pt-2">
            <button 
              type="submit"
              :disabled="passwordSubmitting"
              class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-red-500 to-red-600 text-white rounded-xl hover:from-red-600 hover:to-red-700 transition-all duration-300 font-medium shadow-lg shadow-red-500/25 hover:shadow-xl hover:shadow-red-500/40 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/>
              </svg>
              {{ passwordSubmitting ? 'Сохранение...' : 'Сменить пароль' }}
            </button>
            
            <button 
              type="button"
              @click="showChangePassword = false"
              class="inline-flex items-center gap-2 px-6 py-3 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-300 font-medium"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
              Отмена
            </button>
          </div>
          
          <p v-if="passwordSuccess" class="text-green-500 text-sm flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            {{ passwordSuccess }}
          </p>
          <p v-if="passwordError" class="text-red-500 text-sm flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
            </svg>
            {{ passwordError }}
          </p>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const { apiFetch } = useApi()
const router = useRouter()

const loading = ref(true)
const submitting = ref(false)
const error = ref('')
const submitError = ref('')
const successMessage = ref('')

const avatarPreview = ref(null)
const avatarFile = ref(null)
const fileInput = ref(null)

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
  phone: '',
  vk: '',
  max: '',
  ok: '',
  rutube: '',
  show_phone: false,
  show_email: false,
  show_socials: true
})

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
// СМЕНА ПАРОЛЯ
// ============================================
const showChangePassword = ref(false)
const passwordSubmitting = ref(false)
const passwordSuccess = ref('')
const passwordError = ref('')

const passwordForm = ref({
  old_password: '',
  new_password: '',
  new_password2: ''
})

// ============================================
// ФУНКЦИИ
// ============================================
const triggerFileInput = () => {
  if (fileInput.value) {
    fileInput.value.click()
  }
}

const onAvatarSelected = (event) => {
  const file = event.target.files[0]
  if (file) {
    if (file.size > 2 * 1024 * 1024) {
      alert('Файл слишком большой. Максимум 2MB.')
      return
    }
    const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
    if (!allowedTypes.includes(file.type)) {
      alert('Неподдерживаемый формат. Используйте JPEG, PNG, GIF или WEBP.')
      return
    }
    avatarFile.value = file
    avatarPreview.value = URL.createObjectURL(file)
  }
}

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
        phone: user.phone || '',
        vk: user.vk || '',
        max: user.max || '',
        ok: user.ok || '',
        rutube: user.rutube || '',
        show_phone: !!user.show_phone,
        show_email: !!user.show_email,
        show_socials: user.show_socials !== false
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

const updateProfile = async () => {
  submitting.value = true
  submitError.value = ''
  successMessage.value = ''
  
  try {
    const formData = new FormData()
    formData.append('email', form.value.email)
    formData.append('first_name', form.value.first_name)
    formData.append('last_name', form.value.last_name)
    formData.append('patronymic', form.value.patronymic)
    formData.append('birth_date', form.value.birth_date || '')
    formData.append('bio', form.value.bio || '')
    formData.append('phone', form.value.phone || '')
    formData.append('vk', form.value.vk || '')
    formData.append('max', form.value.max || '')
    formData.append('ok', form.value.ok || '')
    formData.append('rutube', form.value.rutube || '')
    formData.append('show_phone', form.value.show_phone ? 'true' : 'false')
    formData.append('show_email', form.value.show_email ? 'true' : 'false')
    formData.append('show_socials', form.value.show_socials ? 'true' : 'false')
    
    if (avatarFile.value) {
      formData.append('avatar', avatarFile.value)
    }
    
    const res = await apiFetch(`${API_URL}/auth/users/me/update/`, {
      method: 'PUT',
      body: formData
    })
    
    if (res.ok) {
      const user = await res.json()
      authStore.user = user
      if (process.client) {
        localStorage.setItem('user', JSON.stringify(user))
      }
      
      successMessage.value = '✅ Профиль обновлён!'
      
      setTimeout(() => {
        router.push('/profile')
      }, 1500)
    } else {
      const data = await res.json()
      submitError.value = data.detail || 'Ошибка обновления'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    submitError.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}

const changePassword = async () => {
  if (!passwordForm.value.old_password || !passwordForm.value.new_password || !passwordForm.value.new_password2) {
    passwordError.value = 'Заполните все поля'
    return
  }
  
  if (passwordForm.value.new_password !== passwordForm.value.new_password2) {
    passwordError.value = 'Новые пароли не совпадают'
    return
  }
  
  if (passwordForm.value.new_password.length < 8) {
    passwordError.value = 'Пароль должен содержать минимум 8 символов'
    return
  }
  
  passwordSubmitting.value = true
  passwordError.value = ''
  passwordSuccess.value = ''
  
  try {
    const res = await apiFetch(`${API_URL}/auth/users/me/change-password/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        old_password: passwordForm.value.old_password,
        new_password: passwordForm.value.new_password,
        new_password2: passwordForm.value.new_password2
      })
    })
    
    const data = await res.json()
    
    if (res.ok) {
      passwordSuccess.value = '✅ Пароль успешно изменён!'
      passwordForm.value = {
        old_password: '',
        new_password: '',
        new_password2: ''
      }
      setTimeout(() => {
        passwordSuccess.value = ''
        showChangePassword.value = false
      }, 3000)
    } else {
      passwordError.value = data.old_password || data.detail || 'Ошибка смены пароля'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    passwordError.value = 'Ошибка подключения к серверу'
  } finally {
    passwordSubmitting.value = false
  }
}

// ============================================
// ЖИЗНЕННЫЙ ЦИКЛ
// ============================================
onMounted(async () => {
  authStore.restoreAuth()
  await loadProfile()
})
</script>