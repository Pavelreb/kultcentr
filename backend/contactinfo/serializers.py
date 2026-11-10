from rest_framework import serializers
from .models import ContactInfo


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = [
            "id",
            "address",
            "phone",
            "email",
            "work_hours",
            "description",
            "vk",
            "max",
            "ok",
            "rutube",
            "updated_at",
        ]
        read_only_fields = ["id", "updated_at"]
