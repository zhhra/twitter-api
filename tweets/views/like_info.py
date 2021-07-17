from ..models.tweet import Tweet
from rest_framework.generics import (
    ListAPIView,
)
from ..serializers.like_model_serializer import LikeModelSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404


class LikeInfo(ListAPIView):
    serializer_class = LikeModelSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        pk = self.kwargs["pk"]
        tweet = get_object_or_404(Tweet, pk=pk)
        likes = tweet.likes.all()
        return likes
