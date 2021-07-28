from ..serializers.tweet_model_serializer import TweetModelSerializer
from rest_framework import generics
from ..models.tweet import Tweet
from rest_framework import filters


class TweetListView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    queryset = Tweet.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["tweet_body", "created"]
