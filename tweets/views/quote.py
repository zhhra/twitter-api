from ..models.tweet import Tweet
from rest_framework.generics import (
    CreateAPIView,
)
from ..serializers.quote_create_model_serializer import QuoteCreateModelSerializer
from rest_framework.permissions import IsAuthenticated


class Quote(CreateAPIView):
    serializer_class = QuoteCreateModelSerializer
    queryset = Tweet.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        tweet = Tweet.objects.get(pk=self.kwargs.get("pk"))
        serializer.save(
            author=self.request.user, quote=tweet, tweet_body=tweet.tweet_body
        )
        return super().perform_create(serializer)
