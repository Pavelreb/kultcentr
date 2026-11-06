import { useAuthStore } from '~/store/auth'

export default defineNuxtRouteMiddleware((to, from) => {
    const authStore = useAuthStore()

    authStore.restoreAuth()

    if (!authStore.isAuthenticated) {
        return navigateTo('/auth/login')
    }

    if (!authStore.isEditor) {
        return navigateTo('/')
    }
})