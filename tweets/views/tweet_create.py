from ..models.tweet import Tweet
from rest_framework.generics import (
    CreateAPIView,
)
from ..serializers.tweet_create_model_serializer import TweetCreateModelSerializer
from rest_framework.permissions import IsAuthenticated


class TweetCreate(CreateAPIView):
    serializer_class = TweetCreateModelSerializer
    queryset = Tweet.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
