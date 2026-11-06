from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post
from .permissions import IsOwnerOrReadOnly, CanCommentPermission


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        CanCommentPermission,
    ]

    def perform_create(self, serializer):
        post_id = self.request.data.get("post")
        if not post_id:
            from rest_framework.exceptions import ValidationError

            raise ValidationError({"post": "Это поле обязательно"})
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)
        print(f"💬 Создан комментарий к посту: {serializer.instance.content[:30]}...")

    def get_queryset(self):
        queryset = super().get_queryset()
        post_id = self.request.query_params.get("post_id")
        if post_id:
            queryset = queryset.filter(post_id=post_id)
        return queryset

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=["get"], url_path="my_comments")
    def my_comments(self, request):
        user = request.user

        if not user.is_authenticated:
            return Response({"detail": "Не авторизован"}, status=401)

        comments = Comment.objects.filter(author=user).order_by("-created_at")
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)
