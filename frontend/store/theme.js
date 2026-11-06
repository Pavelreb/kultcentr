import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', {
    state: () => ({
        darkMode: false,
    }),

    actions: {
        toggleTheme() {
            this.darkMode = !this.darkMode
            this.applyTheme()
        },

        applyTheme() {
            if (process.client) {
                if (this.darkMode) {
                    document.documentElement.classList.add('dark')
                    localStorage.setItem('theme', 'dark')
                } else {
                    document.documentElement.classList.remove('dark')
                    localStorage.setItem('theme', 'light')
                }
            }
        },

        loadTheme() {
            if (process.client) {
                const savedTheme = localStorage.getItem('theme')
                if (savedTheme === 'dark') {
                    this.darkMode = true
                    document.documentElement.classList.add('dark')
                } else {
                    this.darkMode = false
                    document.documentElement.classList.remove('dark')
                }
            }
        },
    },
})