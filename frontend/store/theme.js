import { defineStore } from 'pinia'

// Режимы оформления:
// light — светлая, dark — тёмная,
// protanopia/deuteranopia/tritanopia — для людей с нарушением цветового зрения
// (дальтонизация: цвета по линии конфликта разводятся через третий канал),
// contrast — чёрно-белая максимально контрастная,
// largefont — светлая с увеличенными шрифтами
export const THEMES = [
    { id: 'light', label: 'Светлая', group: 'base' },
    { id: 'dark', label: 'Тёмная', group: 'base' },
    { id: 'protanopia', label: 'Протанопия (красный)', group: 'colorblind' },
    { id: 'deuteranopia', label: 'Дейтеранопия (зелёный)', group: 'colorblind' },
    { id: 'tritanopia', label: 'Тританопия (синий)', group: 'colorblind' },
    { id: 'contrast', label: 'Чёрно-белая контрастная', group: 'access' },
    { id: 'largefont', label: 'Крупный шрифт', group: 'access' },
]

const THEME_IDS = THEMES.map(t => t.id)

export const useThemeStore = defineStore('theme', {
    state: () => ({
        mode: 'light',
    }),

    getters: {
        // Совместимость со старым кодом
        darkMode: (state) => state.mode === 'dark',
        currentTheme: (state) => THEMES.find(t => t.id === state.mode) || THEMES[0],
    },

    actions: {
        setTheme(mode) {
            if (!THEME_IDS.includes(mode)) mode = 'light'
            this.mode = mode
            this.applyTheme()
        },

        // Старый переключатель светлая/тёмная (совместимость)
        toggleTheme() {
            this.setTheme(this.mode === 'dark' ? 'light' : 'dark')
        },

        applyTheme() {
            if (process.client) {
                const el = document.documentElement
                el.classList.remove('dark')
                for (const id of THEME_IDS) {
                    el.classList.remove(`theme-${id}`)
                }
                if (this.mode === 'dark') {
                    el.classList.add('dark')
                } else if (this.mode !== 'light') {
                    el.classList.add(`theme-${this.mode}`)
                }
                localStorage.setItem('theme', this.mode)
            }
        },

        loadTheme() {
            if (process.client) {
                const savedTheme = localStorage.getItem('theme')
                this.mode = THEME_IDS.includes(savedTheme) ? savedTheme : 'light'
                this.applyTheme()
            }
        },
    },
})
