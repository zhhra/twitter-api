from rest_framework import serializers
from ..models.tweet import Tweet


class QuoteCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = [
            "quote_body",
        ]

    def validate_quote_body(self, value):
        if not value:
            raise serializers.ValidationError("Body is required")
        return value
