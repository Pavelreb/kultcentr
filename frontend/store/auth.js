// frontend/store/auth.js

import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null,
        accessToken: null,
        refreshToken: null
    }),

    getters: {
        isAuthenticated: (state) => !!state.accessToken && !!state.user,
        isAuthor: (state) => state.user?.role === 'author',
        isSubscriber: (state) => state.user?.role === 'subscriber',
        isEditor: (state) => state.user?.role === 'editor',
        username: (state) => state.user?.username || '',

        // Полное имя пользователя (Фамилия Имя Отчество)
        fullName: (state) => {
            if (!state.user) return ''
            const parts = []
            if (state.user.last_name) parts.push(state.user.last_name)
            if (state.user.first_name) parts.push(state.user.first_name)
            if (state.user.patronymic) parts.push(state.user.patronymic)
            return parts.length > 0 ? parts.join(' ') : state.user.username
        },

        // Инициалы пользователя
        initials: (state) => {
            if (!state.user) return '?'
            const name = state.user.full_name || state.user.username
            const parts = name.split(' ')
            if (parts.length >= 2) {
                return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
            }
            return name.substring(0, 2).toUpperCase()
        }
    },

    actions: {
        setAuth(user, access, refresh) {
            this.user = user
            this.accessToken = access
            this.refreshToken = refresh

            if (process.client) {
                localStorage.setItem('access_token', access)
                localStorage.setItem('refresh_token', refresh)
                localStorage.setItem('user', JSON.stringify(user))
                console.log('✅ Авторизация установлена')
            }
        },

        restoreAuth() {
            if (process.client) {
                const access = localStorage.getItem('access_token')
                const refresh = localStorage.getItem('refresh_token')
                const userStr = localStorage.getItem('user')

                if (access && refresh && userStr) {
                    this.accessToken = access
                    this.refreshToken = refresh
                    this.user = JSON.parse(userStr)
                    console.log('✅ Авторизация восстановлена из localStorage')
                    return true
                } else {
                    console.log('⚠️ Токены не найдены в localStorage')
                    return false
                }
            }
            return false
        },

        logout() {
            this.user = null
            this.accessToken = null
            this.refreshToken = null

            if (process.client) {
                localStorage.removeItem('access_token')
                localStorage.removeItem('refresh_token')
                localStorage.removeItem('user')
                console.log('👋 Выход выполнен')
            }
        }
    }
})