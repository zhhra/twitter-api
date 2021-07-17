from ..models.comment import Comment
from tweets.models.tweet import Tweet
from rest_framework.generics import (
    CreateAPIView,
)
from ..serializers.comment_create_model_serializer import CommentCreateModelSerializer
from rest_framework.permissions import IsAuthenticated


class CommentCreate(CreateAPIView):
    serializer_class = CommentCreateModelSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        tweet_pk = self.kwargs.get("pk")
        comment_pk = self.kwargs.get("comment")
        if self.kwargs.get("comment"):
            serializer.save(
                writer=self.request.user,
                tweet=Tweet.objects.get(pk=tweet_pk),
                reply=Comment.objects.get(pk=comment_pk),
            )
        else:
            serializer.save(
                writer=self.request.user, tweet=Tweet.objects.get(pk=tweet_pk)
            )
        return super().perform_create(serializer)
