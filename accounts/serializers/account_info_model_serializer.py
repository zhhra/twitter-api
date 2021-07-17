from rest_framework import serializers
from ..models.user import User


class AccountInfoModelSerializer(serializers.ModelSerializer):
    followings = serializers.StringRelatedField(many=True)
    followers = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "followings_count",
            "followings",
            "followers_count",
            "followers",
        ]
