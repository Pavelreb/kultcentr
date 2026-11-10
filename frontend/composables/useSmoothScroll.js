// frontend/composables/useSmoothScroll.js
// Мягкий скролл с easeInOut-анимацией (нативный behavior:'smooth' слишком резкий)

/**
 * Плавно скроллит страницу до абсолютной Y-координаты.
 * @param {number} targetY - целевая координата прокрутки
 * @param {number} duration - длительность анимации в мс
 */
export const smoothScrollTo = (targetY, duration = 700) => {
  const startY = window.scrollY
  const diff = targetY - startY
  if (Math.abs(diff) < 2) return

  // easeInOutCubic: медленный старт, мягкое замедление в конце
  const easeInOutCubic = (t) =>
    t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2

  let startTime = null
  const step = (timestamp) => {
    if (!startTime) startTime = timestamp
    const progress = Math.min((timestamp - startTime) / duration, 1)
    window.scrollTo(0, startY + diff * easeInOutCubic(progress))
    if (progress < 1) requestAnimationFrame(step)
  }
  requestAnimationFrame(step)
}

/**
 * Плавно скроллит к верху элемента с отступом под липкую шапку.
 * @param {HTMLElement|null} el - целевой элемент
 * @param {number} offset - отступ сверху в px (80 = scroll-mt-20 под шапку)
 * @param {number} duration - длительность анимации в мс
 */
export const smoothScrollToElement = (el, offset = 80, duration = 700) => {
  if (!el) return
  const y = el.getBoundingClientRect().top + window.scrollY - offset
  smoothScrollTo(Math.max(0, y), duration)
}
