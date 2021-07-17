from rest_framework import serializers
from accounts.models.user import User


class LikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
