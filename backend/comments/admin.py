from django.contrib import admin
from django import forms
from .models import Comment


class CommentAdminForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"

    def clean(self):
        """
        Проверка в админке: parent должен быть из того же поста
        """
        cleaned_data = super().clean()
        parent = cleaned_data.get("parent")
        post = cleaned_data.get("post")

        if parent and post:
            if parent.post_id != post.id:
                raise forms.ValidationError(
                    "Родительский комментарий должен принадлежать тому же посту!"
                )

        return cleaned_data


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = ["id", "content", "author", "post", "created_at", "parent"]
    list_filter = ["created_at", "post"]
    search_fields = ["content", "author__username"]
    raw_id_fields = ["post", "author", "parent"]  # Удобный поиск
