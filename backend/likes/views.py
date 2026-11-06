from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer
from posts.models import Post
from comments.models import Comment


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Переопределяем create для работы с постами и комментариями"""
        post_id = request.data.get("post")
        comment_id = request.data.get("comment")

        if not post_id and not comment_id:
            return Response(
                {"detail": "Не указан пост или комментарий"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Лайк на пост
        if post_id:
            try:
                post = Post.objects.get(id=post_id)
            except Post.DoesNotExist:
                return Response(
                    {"detail": "Пост не найден"}, status=status.HTTP_404_NOT_FOUND
                )

            existing_like = Like.objects.filter(user=request.user, post=post).first()

            if existing_like:
                existing_like.delete()
                return Response(
                    {"detail": "Лайк убран", "action": "unliked", "type": "post"},
                    status=status.HTTP_200_OK,
                )
            else:
                like = Like.objects.create(user=request.user, post=post)
                serializer = self.get_serializer(like)
                return Response(
                    {
                        "detail": "Лайк поставлен",
                        "action": "liked",
                        "type": "post",
                        "data": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )

        # Лайк на комментарий
        if comment_id:
            try:
                comment = Comment.objects.get(id=comment_id)
            except Comment.DoesNotExist:
                return Response(
                    {"detail": "Комментарий не найден"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            existing_like = Like.objects.filter(
                user=request.user, comment=comment
            ).first()

            if existing_like:
                existing_like.delete()
                return Response(
                    {"detail": "Лайк убран", "action": "unliked", "type": "comment"},
                    status=status.HTTP_200_OK,
                )
            else:
                like = Like.objects.create(user=request.user, comment=comment)
                serializer = self.get_serializer(like)
                return Response(
                    {
                        "detail": "Лайк поставлен",
                        "action": "liked",
                        "type": "comment",
                        "data": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )
