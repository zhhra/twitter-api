from ..permissions.is_owner import IsOwner
from ..models.comment import Comment
from rest_framework.generics import (
    RetrieveDestroyAPIView,
)
from ..serializers.comment_model_serializer import CommentModelSerializer
from rest_framework.permissions import IsAuthenticated


class CommentDelete(RetrieveDestroyAPIView):
    serializer_class = CommentModelSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated & IsOwner,)
