from ..models.comment import Comment
from rest_framework.generics import (
    ListAPIView,
)
from ..serializers.comment_model_serializer import CommentModelSerializer
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend


class CommentList(ListAPIView):
    serializer_class = CommentModelSerializer
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tweet"]

    def get_queryset(self):
        return Comment.objects.filter(in_reply_to=None)
