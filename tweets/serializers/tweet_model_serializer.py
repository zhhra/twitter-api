from rest_framework import serializers
from ..models.tweet import Tweet
from collections import OrderedDict


class TweetModelSerializer(serializers.ModelSerializer):
    quote = serializers.PrimaryKeyRelatedField(read_only=True)
    retweet = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Tweet
        fields = [
            "author",
            "created",
            "tweet_body",
            "likes_count",
            "quote",
            "quote_body",
            "retweet",
        ]

    def to_representation(self, instance):
        result = super(TweetModelSerializer, self).to_representation(instance)
        return OrderedDict(
            [
                (key, result[key])
                for key in result
                if result[key] is not None and result[key] != ""
            ]
        )
