from rest_framework import serializers
from ..models.tweet import Tweet


class TweetCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = [
            "tweet_body",
        ]

    def validate_tweet_body(self, value):
        if not value:
            raise serializers.ValidationError("Body is required")
        return value
