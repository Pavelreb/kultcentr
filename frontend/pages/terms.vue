<!-- frontend/pages/terms.vue -->
<template>
  <div class="max-w-3xl mx-auto mt-10 px-4 pb-16">
    <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-3 mb-2">
      <svg class="w-8 h-8 text-green-500 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
      </svg>
      Пользовательское соглашение
    </h1>
    <p class="text-sm text-gray-400 dark:text-gray-500 mb-8">Редакция от 11.11.2026</p>

    <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 p-6 md:p-8 space-y-6 text-sm text-gray-600 dark:text-gray-300 leading-relaxed">

      <section>
        <h2 class="text-lg font-bold text-gray-800 dark:text-gray-200 mb-2">1. Термины и общие положения</h2>
        <p>
          Настоящее Соглашение регулирует отношения между администрацией сайта «Центр Культуры»
          (далее — Сайт) и пользователем (далее — Пользователь). Регистрируясь на Сайте, Пользователь
          подтверждает, что ознакомился с условиями Соглашения и принимает их в полном объёме.
        </p>
      </section>

      <section>
        <h2 class="text-lg font-bold text-gray-800 dark:text-gray-200 mb-2">2. Учётная запись</h2>
        <ul class="list-disc pl-5 space-y-1">
          <li>Пользователь обязуется указывать достоверные данные при регистрации.</li>
          <li>Пользователь несёт ответственность за сохранность своего пароля и за все действия, совершённые под его учётной записью.</li>
          <li>Администрация вправе заблокировать учётную запись при нарушении условий Соглашения.</li>
        </ul>
      </section>

      <section>
        <h2 class="text-lg font-bold text-gray-800 dark:text-gray-200 mb-2">3. Правила размещения контента</h2>
        <p class="mb-2">На Сайте запрещено размещать материалы, которые:</p>
        <ul class="list-disc pl-5 space-y-1">
          <li>нарушают законодательство Российской Федерации;</li>
          <li>содержат оскорбления, угрозы, дискриминацию, призывы к насилию;</li>
          <li>содержат материалы порнографического характера;</li>
          <li>нарушают авторские и смежные права третьих лиц;</li>
          <li>содержат спам, рекламу без согласования с администрацией;</li>
          <li>содержат персональные данные других лиц без их согласия.</li>
        </ul>
        <p class="mt-2">
          Администрация вправе удалять контент, нарушающий эти правила, без предварительного уведомления.
        </p>
      </section>

      <section>
        <h2 class="text-lg font-bold text-gray-800 dark:text-gray-200 mb-2">4. Авторские права</h2>
        <p>
          Размещая публикации, фотографии и комментарии, Пользователь подтверждает, что обладает
          необходимыми правами на этот контент, и предоставляет Сайту неисключительное право на его
          отображение в рамках функционала Сайта. Авторские права на контент остаются за Пользователем.
        </p>
      </section>

      <section>
        <h2 class="text-lg font-bold text-gray-800 dark:text-gray-200 mb-2">5. Ответственность</h2>
        <ul class="list-disc pl-5 space-y-1">
          <li>Сайт предоставляется «как есть»; администрация не гарантирует бесперебойную работу сервиса.</li>
          <li>Ответственность за содержание публикаций и комментариев несёт их автор.</li>
          <li>Администрация не отвечает за содержание внешних сайтов, на которые ведут ссылки с Сайта.</li>
        </ul>
      </section>

      <section>
        <h2 class="text-lg font-bold text-gray-800 dark:text-gray-200 mb-2">6. Изменение соглашения</h2>
        <p>
          Администрация вправе изменять условия Соглашения. Актуальная редакция всегда доступна на этой
          странице. Продолжение использования Сайта после изменений означает согласие с новой редакцией.
        </p>
      </section>

      <div class="pt-4 border-t border-gray-100 dark:border-gray-700 text-xs text-gray-400 dark:text-gray-500">
        См. также: <NuxtLink to="/privacy" class="text-blue-500 dark:text-blue-400 hover:underline">Политика конфиденциальности</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
useSeoMeta({
  title: 'Пользовательское соглашение',
  description: 'Условия использования сайта Центр Культуры.'
})
</script>
