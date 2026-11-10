// frontend/composables/useApi.js
import { useAuthStore } from '~/store/auth'

export const useApi = () => {
    const config = useRuntimeConfig()
    const apiBase = config.public.apiBase || 'http://127.0.0.1:8000/api'
    const authStore = useAuthStore()

    let refreshPromise = null

    const refreshAccessToken = () => {
        // Не даём нескольким запросам одновременно дёргать refresh
        if (!refreshPromise) {
            refreshPromise = (async () => {
                if (!authStore.refreshToken) return false
                try {
                    const res = await fetch(`${apiBase}/auth/token/refresh/`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ refresh: authStore.refreshToken })
                    })
                    if (!res.ok) return false
                    const data = await res.json()
                    authStore.accessToken = data.access
                    localStorage.setItem('access_token', data.access)
                    console.log('🔄 Access-токен обновлён')
                    return true
                } catch (e) {
                    console.error('Не удалось обновить токен:', e)
                    return false
                }
            })().finally(() => { refreshPromise = null })
        }
        return refreshPromise
    }

    const buildOptions = (options, withAuth) => {
        const headers = { ...(options.headers || {}) }
        if (withAuth && authStore.accessToken) {
            headers['Authorization'] = `Bearer ${authStore.accessToken}`
        }
        return { ...options, headers }
    }

    /**
     * fetch с авторизацией и авто-обновлением токена.
     * 401 → пробуем refresh → повторяем.
     * refresh не удался → разлогин и повтор БЕЗ токена
     * (публичный контент продолжит грузиться).
     */
    const apiFetch = async (path, options = {}) => {
        const url = path.startsWith('http') ? path : `${apiBase}${path}`

        let res = await fetch(url, buildOptions(options, authStore.isAuthenticated))

        if (res.status === 401 && authStore.accessToken) {
            const refreshed = await refreshAccessToken()
            if (refreshed) {
                res = await fetch(url, buildOptions(options, true))
            } else {
                authStore.logout()
                res = await fetch(url, buildOptions(options, false))
            }
        }

        return res
    }

    return { apiFetch, apiBase }
}