<template>
  <div class="container mx-auto p-8 max-w-2xl">
    <h1 class="text-3xl font-bold mb-8">UI Компоненты</h1>
    
    <!-- Кнопки -->
    <section class="mb-8">
      <h2 class="text-xl font-semibold mb-4">Кнопки</h2>
      <div class="flex flex-wrap gap-3">
        <UiButton variant="primary">Primary</UiButton>
        <UiButton variant="secondary">Secondary</UiButton>
        <UiButton variant="success">Success</UiButton>
        <UiButton variant="danger">Danger</UiButton>
        <UiButton variant="warning">Warning</UiButton>
        <UiButton variant="outline">Outline</UiButton>
        <UiButton variant="primary" disabled>Disabled</UiButton>
      </div>
      <div class="flex flex-wrap gap-3 mt-3">
        <UiButton variant="primary" size="sm">Small</UiButton>
        <UiButton variant="primary" size="md">Medium</UiButton>
        <UiButton variant="primary" size="lg">Large</UiButton>
      </div>
      <div class="mt-3">
        <UiButton variant="primary" fullWidth>Full Width</UiButton>
      </div>
    </section>
    
    <!-- Инпуты -->
    <section class="mb-8">
      <h2 class="text-xl font-semibold mb-4">Поля ввода</h2>
      <UiInput 
        v-model="inputValue"
        label="Имя пользователя"
        placeholder="Введите имя..."
        hint="Минимум 3 символа"
      />
      <UiInput 
        v-model="inputValue2"
        label="Email"
        type="email"
        placeholder="example@mail.com"
        required
      />
      <UiInput 
        v-model="inputValue3"
        label="Ошибка"
        placeholder="Пример ошибки"
        error="Это поле обязательно"
        variant="error"
      />
    </section>
    
    <!-- Текстареа -->
    <section class="mb-8">
      <h2 class="text-xl font-semibold mb-4">Текстовые области</h2>
      <UiTextarea 
        v-model="textareaValue"
        label="Описание"
        placeholder="Введите описание..."
        rows="4"
        hint="Максимум 500 символов"
      />
    </section>
    
    <!-- Чекбоксы -->
    <section class="mb-8">
      <h2 class="text-xl font-semibold mb-4">Чекбоксы</h2>
      <div class="space-y-2">
        <UiCheckbox v-model="checkbox1">
          Принять условия
        </UiCheckbox>
        <UiCheckbox v-model="checkbox2" disabled>
          Отключённый чекбокс
        </UiCheckbox>
      </div>
    </section>
    
    <!-- Карточка -->
    <section class="mb-8">
      <h2 class="text-xl font-semibold mb-4">Карточка</h2>
      <UiCard>
        <h3 class="text-lg font-semibold mb-2">Заголовок карточки</h3>
        <p class="text-gray-600 dark:text-gray-400">
          Это содержимое карточки. Она автоматически адаптируется под тёмную тему.
        </p>
      </UiCard>
    </section>
  </div>
</template>

<script setup>
const inputValue = ref('')
const inputValue2 = ref('')
const inputValue3 = ref('')
const textareaValue = ref('')
const checkbox1 = ref(false)
const checkbox2 = ref(true)
</script>