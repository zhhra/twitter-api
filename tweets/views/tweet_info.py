from ..models.tweet import Tweet
from rest_framework.generics import (
    RetrieveAPIView,
)
from ..serializers.tweet_model_serializer import TweetModelSerializer
from rest_framework.permissions import AllowAny


class TweetInfo(RetrieveAPIView):
    serializer_class = TweetModelSerializer
    queryset = Tweet.objects.all()
    permission_classes = (AllowAny,)
