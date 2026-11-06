import os
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import Event


@receiver(pre_delete, sender=Event)
def delete_event_image_on_delete(sender, instance, **kwargs):
    """Удаляет изображение при удалении события"""
    if instance.image:
        file_path = instance.image.path
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"🗑️ Изображение события удалено при удалении: {file_path}")
        else:
            print(f"⚠️ Файл не найден: {file_path}")


@receiver(pre_save, sender=Event)
def delete_old_event_image_on_update(sender, instance, **kwargs):
    """Удаляет старое изображение при обновлении события"""
    if not instance.pk:
        return

    try:
        old_instance = Event.objects.get(pk=instance.pk)
    except Event.DoesNotExist:
        return

    old_image = old_instance.image
    new_image = instance.image

    print(f"🔍 Старое изображение: {old_image}")
    print(f"🔍 Новое изображение: {new_image}")

    if old_image and not new_image:
        file_path = old_image.path
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"🗑️ Старое изображение удалено: {file_path}")

    if old_image and new_image and old_image.path != new_image.path:
        file_path = old_image.path
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"🗑️ Старое изображение удалено (заменено): {file_path}")
