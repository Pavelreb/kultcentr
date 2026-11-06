from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Like
        fields = ["id", "post", "username", "created_at"]
        read_only_fields = ["user", "created_at"]
