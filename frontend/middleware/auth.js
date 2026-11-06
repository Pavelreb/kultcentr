import { useAuthStore } from '~/store/auth'

export default defineNuxtRouteMiddleware((to, from) => {
    const authStore = useAuthStore()

    console.log('=== MIDDLEWARE AUTH ===')
    console.log('Путь:', to.path)

    authStore.restoreAuth()

    console.log('Авторизован:', authStore.isAuthenticated)
    console.log('Пользователь:', authStore.user?.username)
    console.log('Роль:', authStore.user?.role)

    if (!authStore.isAuthenticated) {
        console.log('❌ Перенаправляем на /auth/login')
        return navigateTo('/auth/login')
    }

    // Проверяем, если путь начинается с /contacts/edit
    if (to.path === '/contacts/edit' && authStore.user?.role !== 'editor') {
        console.log('❌ Недостаточно прав для редактирования контактов')
        return navigateTo('/contacts')
    }

    console.log('✅ Доступ разрешён')
})