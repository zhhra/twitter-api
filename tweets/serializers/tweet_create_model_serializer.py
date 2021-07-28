from rest_framework import serializers
from ..models.tweet import Tweet


class TweetCreateModelSerializer(serializers.ModelSerializer):
    tweet_body = serializers.CharField(max_length=148, required=True)

    class Meta:
        model = Tweet
        fields = [
            "tweet_body",
        ]
