from rest_framework import serializers
from .models import Banner


class BannerSerializer(serializers.ModelSerializer):
    background_image_url_display = serializers.SerializerMethodField()
    has_background = serializers.SerializerMethodField()

    class Meta:
        model = Banner
        fields = [
            "id",
            "title",
            "subtitle",
            "background_image",
            "background_image_url",
            "background_image_url_display",
            "has_background",
            "button_text",
            "button_link",
            "button_enabled",
            "is_active",
            "updated_at",
        ]
        read_only_fields = ["id", "updated_at"]

    def get_background_image_url_display(self, obj):
        if obj.background_image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.background_image.url)
            return obj.background_image.url
        return obj.background_image_url

    def get_has_background(self, obj):
        return bool(obj.background_image or obj.background_image_url)
