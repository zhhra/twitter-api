from ..models.tweet import Tweet
from rest_framework.generics import (
    CreateAPIView,
)
from ..serializers.retweet_create_model_serializer import RetweetCreateModelSerializer
from rest_framework.permissions import IsAuthenticated


class Retweet(CreateAPIView):
    queryset = Tweet.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RetweetCreateModelSerializer

    def perform_create(self, serializer):
        tweet = Tweet.objects.get(pk=self.kwargs.get("pk"))
        serializer.save(
            author=self.request.user, retweet=tweet, tweet_body=tweet.tweet_body
        )
        return super().perform_create(serializer)
