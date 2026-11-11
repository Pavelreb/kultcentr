<!-- frontend/pages/guide.vue -->
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4 pb-16">
    <div v-if="!canAccess" class="bg-white dark:bg-gray-800 p-8 rounded-xl shadow text-center py-20 border border-gray-100 dark:border-gray-700">
      <svg class="w-24 h-24 mx-auto text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
      </svg>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2 mt-4">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Справочник доступен только авторам и редакторам.</p>
    </div>
    <template v-else>
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3">
        <svg class="w-8 h-8 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
        </svg>
        Справочник
      </h1>
      <p class="mt-2 text-gray-500 dark:text-gray-400">
        Как оформлять афиши, публикации, фотоальбомы и раздел «Об учреждении»: форматы изображений, безопасные зоны и советы.
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
      <a href="#guide-banner" class="px-4 py-2 text-sm font-medium rounded-full bg-cyan-100 dark:bg-cyan-900/30 text-cyan-700 dark:text-cyan-300 hover:bg-cyan-200 dark:hover:bg-cyan-900/50 transition">
        Баннер
      </a>
      <a href="#guide-staff" class="px-4 py-2 text-sm font-medium rounded-full bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-300 hover:bg-green-200 dark:hover:bg-green-900/50 transition">
        Сотрудники
      </a>
      <a href="#guide-clubs" class="px-4 py-2 text-sm font-medium rounded-full bg-teal-100 dark:bg-teal-900/30 text-teal-700 dark:text-teal-300 hover:bg-teal-200 dark:hover:bg-teal-900/50 transition">
        Клубные формирования
      </a>
      <a href="#guide-achievements" class="px-4 py-2 text-sm font-medium rounded-full bg-amber-100 dark:bg-amber-900/30 text-amber-700 dark:text-amber-300 hover:bg-amber-200 dark:hover:bg-amber-900/50 transition">
        Достижения
      </a>
      <a href="#guide-content" class="px-4 py-2 text-sm font-medium rounded-full bg-rose-100 dark:bg-rose-900/30 text-rose-700 dark:text-rose-300 hover:bg-rose-200 dark:hover:bg-rose-900/50 transition">
        Текст, голосования и тесты
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
        Рекомендуемый формат обложки альбома — <b>квадрат 1:1</b>: так она одинаково хорошо смотрится и в карточках на странице «Галерея», и на странице самого альбома.
      </p>

      <div class="overflow-x-auto mb-5">
        <table class="w-full text-sm">
          <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Соотношение сторон</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">1:1 (квадрат)</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Рекомендуемый размер</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">1200 × 1200 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Минимальный размер</td><td class="py-2 text-gray-800 dark:text-gray-200">800 × 800 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Формат файла</td><td class="py-2 text-gray-800 dark:text-gray-200">JPG, PNG, WebP</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Вес файла</td><td class="py-2 text-gray-800 dark:text-gray-200">до 500 КБ</td></tr>
          </tbody>
        </table>
      </div>

      <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-2 list-disc pl-5">
        <li><b class="text-gray-800 dark:text-gray-200">Карточки альбомов</b> на странице «Галерея» обрезают обложку под свой кадр — выбирайте обложку, где главное находится в центре.</li>
        <li>На странице альбома обложка показывается целиком, но квадратная обложка занимает место аккуратнее и не растягивает страницу по высоте.</li>
        <li>Если под рукой только горизонтальное или вертикальное фото — обрежьте его под квадрат заранее, чтобы обрезка не случилась автоматически в неудачном месте.</li>
      </ul>
    </section>

    <!-- ======== Баннер (главная и «Об учреждении») ======== -->
    <section id="guide-banner" class="scroll-mt-24 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-6 mt-8">
      <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 mb-4">
        <svg class="w-6 h-6 text-cyan-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        </svg>
        Баннер
      </h2>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
        Баннер используется на двух страницах: на <b>главной</b> (настраивается в «Настройки сайта → Баннер») и на странице <b>«Об учреждении»</b> («Настройки сайта → Об учреждении»).
        Устройство у них одинаковое: широкое фоновое изображение, поверх — затемнение и текст по центру. На странице «Об учреждении» дополнительно выводится <b>логотип</b> учреждения.
        Рекомендации по фону одинаковы для обоих баннеров.
      </p>

      <h3 class="font-semibold text-gray-800 dark:text-gray-200 mb-2">Фоновое изображение</h3>
      <div class="overflow-x-auto mb-4">
        <table class="w-full text-sm">
          <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Соотношение сторон</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">Широкое горизонтальное, примерно 16:5</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Рекомендуемый размер</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">1920 × 600 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Формат файла</td><td class="py-2 text-gray-800 dark:text-gray-200">JPG, WebP</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Вес файла</td><td class="py-2 text-gray-800 dark:text-gray-200">до 500 КБ</td></tr>
          </tbody>
        </table>
      </div>
      <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-2 list-disc pl-5 mb-5">
        <li>Фон <b>обрезается под широкую горизонтальную полосу</b> и затемняется — мелкий текст и лица на нём теряются, используйте атмосферное фото (здание, сцена, зал).</li>
        <li>Центр кадра перекрыт текстом (на «Об учреждении» — ещё и логотипом) — главное в фото держите ближе к краям или используйте нейтральный фон.</li>
        <li>Если фон не загружен, показывается цветной градиент по умолчанию.</li>
      </ul>

      <h3 class="font-semibold text-gray-800 dark:text-gray-200 mb-2">Логотип (только «Об учреждении»)</h3>
      <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-2 list-disc pl-5">
        <li><b class="text-gray-800 dark:text-gray-200">Квадратный</b>, минимум 400 × 400 px; отображается в круглой рамке — важное не должно касаться углов.</li>
        <li>Лучше всего <b>PNG с прозрачным фоном</b>; подойдут и JPG/WebP до 500 КБ.</li>
        <li>Если логотип не загружен, показывается иконка-заглушка.</li>
      </ul>
    </section>

    <!-- ======== Фото сотрудников ======== -->
    <section id="guide-staff" class="scroll-mt-24 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-6 mt-8">
      <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 mb-4">
        <svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/>
        </svg>
        Фото сотрудника
      </h2>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
        Фото сотрудника показывается <b>в круглой рамке</b> в карточках на страницах «Об учреждении» и «Наши сотрудники». Настраивается в «Настройки сайта → Сотрудники».
      </p>

      <div class="overflow-x-auto mb-5">
        <table class="w-full text-sm">
          <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Соотношение сторон</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">1:1 (квадрат)</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Рекомендуемый размер</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">600 × 600 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Минимальный размер</td><td class="py-2 text-gray-800 dark:text-gray-200">400 × 400 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Формат файла</td><td class="py-2 text-gray-800 dark:text-gray-200">JPG, PNG, WebP</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Вес файла</td><td class="py-2 text-gray-800 dark:text-gray-200">до 500 КБ</td></tr>
          </tbody>
        </table>
      </div>

      <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-2 list-disc pl-5">
        <li>Лицо — <b>по центру кадра</b>, углы изображения обрежутся круглой рамкой.</li>
        <li>Лучше всего работает портрет по пояс или по плечи на спокойном фоне.</li>
        <li>Если сотрудник привязан к пользователю сайта и фото не загружено, подставится его аватар; если нет и его — инициалы.</li>
      </ul>
    </section>

    <!-- ======== Изображения клубных формирований ======== -->
    <section id="guide-clubs" class="scroll-mt-24 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-6 mt-8">
      <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 mb-4">
        <svg class="w-6 h-6 text-teal-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
        </svg>
        Изображение клубного формирования
      </h2>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
        Изображение формирования везде отображается как <b>горизонтальный кадр 16:9</b>: в карточках на страницах «Об учреждении» и «Клубные формирования», а также крупно на странице самого формирования. Настраивается в «Настройки сайта → Клубные формирования».
      </p>

      <div class="overflow-x-auto mb-5">
        <table class="w-full text-sm">
          <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Соотношение сторон</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">16:9 (строго горизонтальное)</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Рекомендуемый размер</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">1600 × 900 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Минимальный размер</td><td class="py-2 text-gray-800 dark:text-gray-200">1280 × 720 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Формат файла</td><td class="py-2 text-gray-800 dark:text-gray-200">JPG (фото), PNG (графика), WebP</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Вес файла</td><td class="py-2 text-gray-800 dark:text-gray-200">до 500 КБ</td></tr>
          </tbody>
        </table>
      </div>

      <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-2 list-disc pl-5">
        <li>Если пропорции не 16:9, картинка <b>обрежется сверху и снизу</b> — ключевое держите по центру кадра.</li>
        <li>Идеально подходят фото занятий, репетиций, выступлений коллектива.</li>
        <li>Если изображение не загружено, вместо него показывается заглушка-иконка.</li>
      </ul>
    </section>

    <!-- ======== Изображения достижений ======== -->
    <section id="guide-achievements" class="scroll-mt-24 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-6 mt-8">
      <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 mb-4">
        <svg class="w-6 h-6 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/>
        </svg>
        Изображение достижения
      </h2>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
        Изображение достижения везде отображается как <b>горизонтальный кадр 16:9</b>: в карточках на страницах «Об учреждении» и «Достижения», а также крупно на странице самого достижения. Настраивается в «Настройки сайта → Достижения».
      </p>

      <div class="overflow-x-auto mb-5">
        <table class="w-full text-sm">
          <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Соотношение сторон</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">16:9 (строго горизонтальное)</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Рекомендуемый размер</td><td class="py-2 text-gray-800 dark:text-gray-200 font-medium">1600 × 900 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Минимальный размер</td><td class="py-2 text-gray-800 dark:text-gray-200">1280 × 720 px</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Формат файла</td><td class="py-2 text-gray-800 dark:text-gray-200">JPG (фото), PNG (скан диплома/грамоты), WebP</td></tr>
            <tr><td class="py-2 pr-4 text-gray-500 dark:text-gray-400 whitespace-nowrap">Вес файла</td><td class="py-2 text-gray-800 dark:text-gray-200">до 500 КБ</td></tr>
          </tbody>
        </table>
      </div>

      <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-2 list-disc pl-5">
        <li>Если пропорции не 16:9, картинка <b>обрежется сверху и снизу</b> — диплом или грамоту сфотографируйте/отсканируйте горизонтально, с запасом по краям.</li>
        <li>Подходят фото награждения, сканы дипломов и грамот, кубки и медали.</li>
        <li>Если изображение не загружено, вместо него показывается заглушка-иконка.</li>
      </ul>
    </section>

    <!-- ======== Текст, голосования и тесты ======== -->
    <section id="guide-content" class="scroll-mt-24 bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-6 mt-8">
      <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2 mb-4">
        <svg class="w-6 h-6 text-rose-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
        </svg>
        Текст, голосования и тесты
      </h2>

      <h3 class="font-semibold text-gray-800 dark:text-gray-200 mb-2">Форматирование текста</h3>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-3">
        Поле «Содержание» публикации и «Полное описание» афиши поддерживают форматирование. Над полем есть панель с кнопками: выделите текст и нажмите кнопку — разметка подставится сама. Можно писать разметку и вручную:
      </p>
      <div class="overflow-x-auto mb-5">
        <table class="w-full text-sm">
          <thead>
            <tr class="text-left text-xs text-gray-400 dark:text-gray-500 uppercase tracking-wide border-b border-gray-100 dark:border-gray-700">
              <th class="py-2 pr-4 font-medium">Как написать</th>
              <th class="py-2 font-medium">Что получится</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
            <tr><td class="py-2 pr-4 text-gray-800 dark:text-gray-200 font-mono text-xs">**важный текст**</td><td class="py-2 text-gray-800 dark:text-gray-200"><b>важный текст</b></td></tr>
            <tr><td class="py-2 pr-4 text-gray-800 dark:text-gray-200 font-mono text-xs">*наклонный текст*</td><td class="py-2 text-gray-800 dark:text-gray-200"><i>наклонный текст</i></td></tr>
            <tr><td class="py-2 pr-4 text-gray-800 dark:text-gray-200 font-mono text-xs">[название](https://site.ru)</td><td class="py-2 text-gray-800 dark:text-gray-200"><span class="text-blue-600 dark:text-blue-400 underline">название</span> — ссылка, откроется в новой вкладке</td></tr>
            <tr><td class="py-2 pr-4 text-gray-800 dark:text-gray-200 font-mono text-xs">- первый пункт<br>- второй пункт</td><td class="py-2 text-gray-800 dark:text-gray-200">маркированный список</td></tr>
            <tr><td class="py-2 pr-4 text-gray-800 dark:text-gray-200 font-mono text-xs">1. первый шаг<br>2. второй шаг</td><td class="py-2 text-gray-800 dark:text-gray-200">нумерованный список</td></tr>
          </tbody>
        </table>
      </div>
      <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-2 list-disc pl-5 mb-6">
        <li>Каждый список пишется с новой строки; пустая строка заканчивает список и начинает новый абзац.</li>
        <li>Ссылка должна начинаться с <span class="font-mono text-xs">http://</span> или <span class="font-mono text-xs">https://</span>.</li>
        <li>Форматирование работает и в карточках на главной и в списках — текст там показывается уже оформленным.</li>
      </ul>

      <h3 class="font-semibold text-gray-800 dark:text-gray-200 mb-2">Голосование в публикации (только редакторы)</h3>
      <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-2 list-disc pl-5 mb-4">
        <li>Создавать и изменять голосования могут <b>только редакторы</b> — в форме публикации включите галочку <b>«Добавить голосование»</b>.</li>
        <li>Заполните <b>вопрос</b> и минимум <b>2 варианта ответа</b>; кнопка «Добавить вариант» добавляет ещё.</li>
        <li>Каждый <b>зарегистрированный</b> пользователь может проголосовать <b>только один раз</b>; после голоса видны результаты с процентами. Незарегистрированным предлагается войти.</li>
        <li>Удалить голосование может только редактор (кнопка корзины на блоке) — все голоса при этом стираются.</li>
      </ul>

      <h3 class="font-semibold text-gray-800 dark:text-gray-200 mb-2">Тест в публикации (только редакторы)</h3>
      <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-2 list-disc pl-5 mb-4">
        <li>Создавать и изменять тесты могут <b>только редакторы</b> — включите галочку <b>«Добавить тест»</b>, укажите название (обязательно) и описание (по желанию).</li>
        <li>Добавьте вопросы. У каждого вопроса минимум 2 ответа, и ровно один из них отметьте переключателем как <b>правильный</b>.</li>
        <li>Любой <b>зарегистрированный</b> пользователь проходит тест <b>один раз</b>: кнопка «Завершить тест» активна, когда выбран ответ на каждый вопрос. Незарегистрированным предлагается войти.</li>
        <li>После прохождения показывается результат (например, 7 из 10) и разбор: правильные ответы подсвечены зелёным, ошибки пользователя — красным.</li>
        <li>Удалить тест может только редактор — результаты всех прохождений при этом стираются.</li>
      </ul>

      <!-- Большое предупреждение -->
      <div class="flex items-start gap-3 p-4 mb-6 rounded-xl border-2 border-red-300 dark:border-red-700 bg-red-50 dark:bg-red-900/20">
        <svg class="w-8 h-8 text-red-500 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
        </svg>
        <div>
          <p class="text-lg font-extrabold text-red-600 dark:text-red-400 uppercase tracking-wide mb-1">Внимание!</p>
          <p class="text-base font-bold text-red-600 dark:text-red-400">
            Если отредактировать и сохранить пост с голосованием или тестом — все результаты СБРОСЯТСЯ: голоса и прохождения пользователей будут удалены безвозвратно.
          </p>
          <p class="text-sm text-red-500 dark:text-red-400 mt-1">
            Перед правкой такого поста убедитесь, что голосование/тест завершены, либо сначала сохраните нужные данные со страницы «Статистика».
          </p>
        </div>
      </div>

      <h3 class="font-semibold text-gray-800 dark:text-gray-200 mb-2">Статистика (только для редакторов)</h3>
      <p class="text-sm text-gray-600 dark:text-gray-400">
        Раздел <b>«Управление → Статистика»</b> в главном меню показывает по каждому голосованию распределение голосов и список проголосовавших, а по каждому тесту — число прохождений, средний результат и таблицу: кто, когда и на сколько процентов прошёл тест.
      </p>
    </section>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: ['auth']
})

useSeoMeta({
  title: 'Справочник',
  description: 'Как оформлять афиши, публикации и фотоальбомы: форматы изображений, безопасные зоны и советы.'
})

const authStore = useAuthStore()

const canAccess = computed(() => authStore.isAuthor || authStore.isEditor)

onMounted(() => {
  authStore.restoreAuth()
})
</script>
