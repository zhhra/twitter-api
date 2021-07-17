from rest_framework import fields, serializers
from ..models.tweet import Tweet


class RetweetCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["created"]
