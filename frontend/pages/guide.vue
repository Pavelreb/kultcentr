<!-- frontend/pages/guide.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4 pb-16">
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
        </svg>
        Справочник
      </h1>
      <p class="mt-2 text-gray-500 dark:text-gray-400">
        Как оформлять афиши, публикации и фотоальбомы: форматы изображений, безопасные зоны и советы.
      </p>
    </div>

    <!-- Навигация по разделам -->
    <div class="flex flex-wrap gap-2 mb-8">
      <a href="#guide-events" class="px-4 py-2 text-sm font-medium rounded-full bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 hover:bg-purple-200 dark:hover:bg-purple-900/50 transition">
        Афиши
      </a>
      <a href="#guide-posts" class="px-4 py-2 text-sm font-medium rounded-full bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-300 hover:bg-green-200 dark:hover:bg-green-900/50 transition">
        Публикации
      </a>
      <a href="#guide-albums" class="px-4 py-2 text-sm font-medium rounded-full bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 hover:bg-blue-200 dark:hover:bg-blue-900/50 transition">
        Фотоальбомы
      </a>
    </div>

    <!-- ======== Афиши ======== -->
    <section id="guide-events" class="scroll-mt-24 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-6 mb-8">
      <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 mb-4">
        <svg class="w-6 h-6 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        </svg>
        Изображение афиши
      </h2>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
        Афиша на сайте везде отображается как <b>вертикальный постер 9:16</b>.
      </p>

      <div class="overflow-x-auto mb-5">
        <table class="w-full text-sm">
          <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Соотношение сторон</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">9:16 (строго вертикальное)</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Рекомендуемый размер</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">900 × 1600 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Минимальный размер</td><td class="py-2 text-gray-800 dark:text-gray-200">720 × 1280 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Формат файла</td><td class="py-2 text-gray-800 dark:text-gray-200">JPG (фото), PNG (графика с текстом), WebP</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Вес файла</td><td class="py-2 text-gray-800 dark:text-gray-200">до 500 КБ (сжимать перед загрузкой)</td></tr>
          </tbody>
        </table>
      </div>

      <h3 class="font-semibold text-gray-800 dark:text-gray-200 mb-2">Как обрезается</h3>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
        Изображение выводится в режиме «заполнить кадр»: если пропорции загруженной картинки не 9:16, края <b>обрежутся</b>.
        Горизонтальные фото не подходят — они будут обрезаны по бокам до вертикали. Важные элементы (лица, текст, логотипы) размещайте по центру кадра, не у краёв.
      </p>

      <h3 class="font-semibold text-gray-800 dark:text-gray-200 mb-2">Безопасные зоны постера</h3>
      <div class="flex flex-col sm:flex-row gap-4 mb-5">
        <!-- Схема постера -->
        <div class="flex-shrink-0 mx-auto sm:mx-0">
          <div class="w-[108px] h-[192px] rounded-lg overflow-hidden border border-gray-200 dark:border-gray-600 flex flex-col text-center text-[10px] leading-tight">
            <div class="h-[15%] bg-red-100 dark:bg-red-900/40 text-red-600 dark:text-red-300 flex items-center justify-center px-1">Бейджи «Сегодня» / «Скоро»</div>
            <div class="flex-1 bg-green-100 dark:bg-green-900/40 text-green-700 dark:text-green-300 flex items-center justify-center px-1">Главная зона: ключевой образ</div>
            <div class="h-[35%] bg-amber-100 dark:bg-amber-900/40 text-amber-700 dark:text-amber-300 flex items-center justify-center px-1">Градиент: заголовок, дата, место</div>
          </div>
        </div>
        <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-2 list-disc pl-5">
          <li><b class="text-gray-800 dark:text-gray-200">Верх (~15% высоты)</b> — бейджи «Сегодня» / «Скоро» / «Черновик». Не размещайте там важный текст.</li>
          <li><b class="text-gray-800 dark:text-gray-200">Низ (~35% высоты)</b> — затемняющий градиент с заголовком, датой и местом. Нижнюю треть картинки лучше делать спокойной, без мелких деталей.</li>
          <li><b class="text-gray-800 dark:text-gray-200">Середина</b> — главная зона: здесь должен быть ключевой образ афиши.</li>
        </ul>
      </div>

      <h3 class="font-semibold text-gray-800 dark:text-gray-200 mb-2">Как оформлять афишу</h3>
      <ol class="text-sm text-gray-600 dark:text-gray-400 space-y-1.5 list-decimal pl-5 mb-4">
        <li><b class="text-gray-800 dark:text-gray-200">Изображение</b> — вертикальный постер 9:16. Лучше всего работает настоящая «театральная» афиша: название, ключевой визуал, минимум мелкого текста.</li>
        <li><b class="text-gray-800 dark:text-gray-200">Заголовок</b> — короткий, 2–6 слов: на карточке показывается максимум 2 строки.</li>
        <li><b class="text-gray-800 dark:text-gray-200">Описание</b> — первые 1–2 предложения работают как анонс: на карточке видно ~80–120 символов.</li>
        <li><b class="text-gray-800 dark:text-gray-200">Дата и время</b> — указывать обязательно: по дате работают бейджи «Сегодня» и «Скоро».</li>
        <li><b class="text-gray-800 dark:text-gray-200">Место проведения</b> — короткое («Большой зал», «ДК, 2 этаж»): на карточке обрезается до 15 символов.</li>
        <li><b class="text-gray-800 dark:text-gray-200">Стоимость</b> — как принято писать: «Вход свободный», «300 ₽», «300–500 ₽».</li>
        <li><b class="text-gray-800 dark:text-gray-200">Кнопка «Купить билет»</b> — ссылка на внешний сервис; заполнять, только если билеты действительно продаются онлайн.</li>
      </ol>
      <p class="text-xs text-gray-400 dark:text-gray-500">
        Постер 9:16 используется: в секции «Афиша» на главной, на странице «Афиша», в главной афише и на странице отдельного события.
      </p>
    </section>

    <!-- ======== Публикации ======== -->
    <section id="guide-posts" class="scroll-mt-24 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-6 mb-8">
      <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 mb-4">
        <svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
        </svg>
        Изображение публикации
      </h2>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
        Изображение поста везде отображается как <b>горизонтальный кадр 16:9</b> — как обложка статьи.
      </p>

      <div class="overflow-x-auto mb-5">
        <table class="w-full text-sm">
          <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Соотношение сторон</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">16:9 (строго горизонтальное)</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Рекомендуемый размер</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">1600 × 900 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Минимальный размер</td><td class="py-2 text-gray-800 dark:text-gray-200">1280 × 720 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Формат файла</td><td class="py-2 text-gray-800 dark:text-gray-200">JPG (фото), PNG (графика), WebP</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Вес файла</td><td class="py-2 text-gray-800 dark:text-gray-200">до 500 КБ (сжимать перед загрузкой)</td></tr>
          </tbody>
        </table>
      </div>

      <h3 class="font-semibold text-gray-800 dark:text-gray-200 mb-2">Как обрезается</h3>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
        Если пропорции не 16:9, картинка <b>обрежется сверху и снизу</b>. Вертикальные фото не подходят — от них останется узкая полоса по центру.
        Ключевой объект держите по центру кадра, важное не размещайте у самого верха и низа.
      </p>

      <h3 class="font-semibold text-gray-800 dark:text-gray-200 mb-2">Безопасные зоны кадра</h3>
      <div class="flex flex-col sm:flex-row gap-4 mb-5">
        <!-- Схема кадра -->
        <div class="flex-shrink-0 mx-auto sm:mx-0">
          <div class="relative w-[256px] h-[144px] rounded-lg overflow-hidden border border-gray-200 dark:border-gray-600 bg-green-100 dark:bg-green-900/40">
            <div class="absolute top-1 left-1 px-1.5 py-0.5 rounded bg-red-200 dark:bg-red-900/60 text-red-700 dark:text-red-300 text-[9px] leading-tight">«Новое»</div>
            <div class="absolute top-1 right-1 px-1.5 py-0.5 rounded bg-red-200 dark:bg-red-900/60 text-red-700 dark:text-red-300 text-[9px] leading-tight">«Черновик»</div>
            <div class="absolute bottom-1 right-1 px-1.5 py-0.5 rounded bg-amber-200 dark:bg-amber-900/60 text-amber-700 dark:text-amber-300 text-[9px] leading-tight">Лайки</div>
            <div class="absolute inset-0 flex items-center justify-center text-green-700 dark:text-green-300 text-[10px] leading-tight text-center px-8">Свободная зона</div>
          </div>
        </div>
        <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-2 list-disc pl-5">
          <li><b class="text-gray-800 dark:text-gray-200">Верхний левый угол</b> — бейдж «Новое». Не размещайте там текст и лица.</li>
          <li><b class="text-gray-800 dark:text-gray-200">Верхний правый угол</b> — бейдж «Черновик» (виден только редакции).</li>
          <li><b class="text-gray-800 dark:text-gray-200">Нижний правый угол</b> — на странице поста там счётчик лайков.</li>
          <li>Текст на изображении допустим, но помните про возможную обрезку по краям.</li>
        </ul>
      </div>

      <h3 class="font-semibold text-gray-800 dark:text-gray-200 mb-2">Как оформлять публикацию</h3>
      <ol class="text-sm text-gray-600 dark:text-gray-400 space-y-1.5 list-decimal pl-5 mb-4">
        <li><b class="text-gray-800 dark:text-gray-200">Изображение</b> — горизонтальный кадр 16:9: фото события, коллективное, с мероприятия — то, что даёт представление о теме поста.</li>
        <li><b class="text-gray-800 dark:text-gray-200">Заголовок</b> — 2–8 слов: на карточках показывается максимум 2 строки.</li>
        <li><b class="text-gray-800 dark:text-gray-200">Первый абзац</b> — работает как анонс: на карточках видно ~100–200 символов. Пишите в нём суть, без «воды».</li>
        <li><b class="text-gray-800 dark:text-gray-200">Текст</b> — абзацы разделяйте пустой строкой; длинные «простыни» без абзацев читаются плохо.</li>
        <li><b class="text-gray-800 dark:text-gray-200">Главная публикация</b> — отмечается редактором; её изображение показывается крупно на странице «Публикации», поэтому для неё особенно важно качественное фото 16:9.</li>
      </ol>
      <p class="text-xs text-gray-400 dark:text-gray-500">
        Кадр 16:9 используется: в секции «Публикации» на главной, на странице «Публикации», в главной публикации и на странице отдельного поста.
      </p>
    </section>

    <!-- ======== Фотоальбомы ======== -->
    <section id="guide-albums" class="scroll-mt-24 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-6">
      <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 mb-4">
        <svg class="w-6 h-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        </svg>
        Обложка фотоальбома
      </h2>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
        У обложки альбома <b>нет строгого формата</b>: на странице альбома она показывается целиком, без обрезки — рамка подстраивается под пропорции изображения.
      </p>

      <div class="overflow-x-auto mb-5">
        <table class="w-full text-sm">
          <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Соотношение сторон</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">Любое; лучше всего 3:2 или 4:3 (горизонтальное)</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Рекомендуемый размер</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">1200 × 900 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Максимальная высота показа</td><td class="py-2 text-gray-800 dark:text-gray-200">520 px — очень высокие вертикальные обложки ужмутся</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Формат файла</td><td class="py-2 text-gray-800 dark:text-gray-200">JPG, PNG, WebP</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Вес файла</td><td class="py-2 text-gray-800 dark:text-gray-200">до 500 КБ</td></tr>
          </tbody>
        </table>
      </div>

      <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-2 list-disc pl-5">
        <li><b class="text-gray-800 dark:text-gray-200">Карточки альбомов</b> на странице «Галерея» обрезают обложку под свой кадр — выбирайте обложку, где главное находится в центре.</li>
        <li>На странице альбома обложка видна целиком, поэтому подойдёт и вертикальный кадр, и панорама.</li>
      </ul>
    </section>
  </div>
</template>

<script setup>
useSeoMeta({
  title: 'Справочник',
  description: 'Как оформлять афиши, публикации и фотоальбомы: форматы изображений, безопасные зоны и советы.'
})
</script>
