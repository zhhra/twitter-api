from rest_framework import serializers
from ..models.tweet import Tweet


class QuoteCreateModelSerializer(serializers.ModelSerializer):
    quote_body = serializers.CharField(max_length=148, required=True)

    class Meta:
        model = Tweet
        fields = [
            "quote_body",
        ]
