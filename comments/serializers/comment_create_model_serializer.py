from rest_framework import serializers
from ..models.comment import Comment


class CommentCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "body",
        ]
