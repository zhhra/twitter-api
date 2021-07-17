from ..permissions.is_owner import IsOwner
from ..models.tweet import Tweet
from rest_framework.generics import (
    RetrieveDestroyAPIView,
)
from ..serializers.tweet_model_serializer import TweetModelSerializer
from rest_framework.permissions import IsAuthenticated


class TweetDelete(RetrieveDestroyAPIView):
    serializer_class = TweetModelSerializer
    queryset = Tweet.objects.all()
    permission_classes = (IsAuthenticated & IsOwner,)
