from ..models.comment import Comment
from rest_framework.generics import (
    RetrieveAPIView,
)
from ..serializers.comment_model_serializer import CommentModelSerializer
from rest_framework.permissions import AllowAny


class CommentInfo(RetrieveAPIView):
    serializer_class = CommentModelSerializer
    queryset = Comment.objects.all()
    permission_classes = (AllowAny,)
