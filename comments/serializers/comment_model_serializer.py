from rest_framework import serializers
from ..models.comment import Comment


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentModelSerializer(serializers.ModelSerializer):
    writer = serializers.StringRelatedField()
    reply_comments = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ["writer", "body", "created", "reply_comments"]
