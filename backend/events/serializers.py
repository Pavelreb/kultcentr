from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)
    author_role = serializers.CharField(source="author.role", read_only=True)
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "content",
            "author_name",
            "author_role",
            "event_date",
            "location",
            "price",
            "image",
            "image_url",
            "display_image",
            "created_at",
            "updated_at",
            "is_published",
            "excerpt",
            "is_featured",
        ]
        read_only_fields = [
            "author",
            "author_name",
            "author_role",
            "created_at",
            "updated_at",
            "is_featured",
        ]
        extra_kwargs = {
            "image": {"required": False, "allow_null": True},
            "image_url": {"required": False, "allow_null": True, "allow_blank": True},
        }

    def get_display_image(self, obj):
        """Возвращает URL изображения для отображения"""
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return obj.image_url

    def to_representation(self, instance):
        """Добавляем image_url в ответ для удобства фронтенда"""
        data = super().to_representation(instance)
        if instance.image:
            request = self.context.get("request")
            if request:
                data["image_url"] = request.build_absolute_uri(instance.image.url)
            else:
                data["image_url"] = instance.image.url
        return data

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.excerpt = validated_data.get("excerpt", instance.excerpt)
        instance.event_date = validated_data.get("event_date", instance.event_date)
        instance.location = validated_data.get("location", instance.location)
        instance.price = validated_data.get("price", instance.price)

        if "image" in validated_data:
            instance.image = validated_data.get("image")

        if "image_url" in validated_data:
            instance.image_url = validated_data.get("image_url")

        instance.is_published = validated_data.get(
            "is_published", instance.is_published
        )
        instance.save()
        return instance
