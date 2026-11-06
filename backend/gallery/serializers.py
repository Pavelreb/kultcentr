# backend/gallery/serializers.py

from rest_framework import serializers
from .models import Album, Photo, PhotoLike, PhotoComment


class PhotoCommentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source="user.username")
    user_first_name = serializers.CharField(source="user.first_name", read_only=True)
    user_last_name = serializers.CharField(source="user.last_name", read_only=True)
    user_full_name = serializers.SerializerMethodField()
    user_avatar = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()

    class Meta:
        model = PhotoComment
        fields = [
            "id",
            "photo",
            "user",
            "user_name",
            "user_first_name",
            "user_last_name",
            "user_full_name",
            "user_avatar",
            "content",
            "created_at",
            "updated_at",
            "can_edit",
            "can_delete",
        ]
        read_only_fields = ["id", "user", "created_at", "updated_at"]

    def get_user_full_name(self, obj):
        parts = []
        if obj.user.last_name:
            parts.append(obj.user.last_name)
        if obj.user.first_name:
            parts.append(obj.user.first_name)
        return " ".join(parts) if parts else obj.user.username

    def get_user_avatar(self, obj):
        if obj.user.avatar:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.user.avatar.url)
            return obj.user.avatar.url
        return None

    def get_can_edit(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return obj.user == request.user

    def get_can_delete(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False

        user = request.user
        if obj.user == user:
            return True
        if user.role == "editor":
            return True
        return False


class PhotoLikeSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = PhotoLike
        fields = ["id", "photo", "user", "user_name", "created_at"]
        read_only_fields = ["id", "user", "created_at"]


class PhotoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = [
            "id",
            "album",
            "image",
            "image_url",
            "thumbnail_url",
            "caption",
            "order",
            "uploaded_at",
            "views",
            "likes_count",
            "user_has_liked",
            "comments_count",
            "comments",
        ]
        read_only_fields = ["id", "uploaded_at", "views", "likes_count"]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    def get_thumbnail_url(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    def get_user_has_liked(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return obj.likes.filter(user=request.user).exists()

    def get_comments(self, obj):
        comments = obj.comments.all()
        context = {"request": self.context.get("request")}
        return PhotoCommentSerializer(comments, many=True, context=context).data


class AlbumListSerializer(serializers.ModelSerializer):
    cover_image_url = serializers.SerializerMethodField()
    photos_count = serializers.IntegerField(source="photos.count", read_only=True)

    class Meta:
        model = Album
        fields = [
            "id",
            "title",
            "description",
            "date",
            "cover_image",
            "cover_image_url",
            "photos_count",
            "created_at",
            "updated_at",
            "is_published",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_cover_image_url(self, obj):
        if obj.cover_image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.cover_image.url)
            return obj.cover_image.url
        return obj.cover_image_url


class AlbumDetailSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    cover_image_url = serializers.SerializerMethodField()
    photos_count = serializers.IntegerField(source="photos.count", read_only=True)

    class Meta:
        model = Album
        fields = [
            "id",
            "title",
            "description",
            "date",
            "cover_image",
            "cover_image_url",
            "photos",
            "photos_count",
            "created_at",
            "updated_at",
            "is_published",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_cover_image_url(self, obj):
        if obj.cover_image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.cover_image.url)
            return obj.cover_image.url
        return obj.cover_image_url


class AlbumCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            "id",
            "title",
            "description",
            "date",
            "cover_image",
            "cover_image_url",
            "is_published",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def update(self, instance, validated_data):
        # Обновляем простые поля
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.date = validated_data.get("date", instance.date)
        instance.is_published = validated_data.get(
            "is_published", instance.is_published
        )

        # Обработка обложки
        if "cover_image" in validated_data:
            instance.cover_image = validated_data.get("cover_image")
            if instance.cover_image:
                instance.cover_image_url = None

        if "cover_image_url" in validated_data:
            cover_url = validated_data.get("cover_image_url")
            if cover_url:
                instance.cover_image_url = cover_url
                if instance.cover_image:
                    old_path = instance.cover_image.path
                    if os.path.isfile(old_path):
                        os.remove(old_path)
                    instance.cover_image = None
            else:
                instance.cover_image_url = None

        instance.save()
        return instance
