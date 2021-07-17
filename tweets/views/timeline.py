from django.db.models import Q
from ..models.tweet import Tweet
from rest_framework.generics import (
    ListAPIView,
)
from ..serializers.tweet_model_serializer import TweetModelSerializer
from rest_framework.permissions import IsAuthenticated


class Timeline(ListAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        followings = user.followings.all()
        timeline = Tweet.objects.filter(
            Q(author__in=followings) | Q(author=user) | Q(likes__in=followings)
        ).distinct()
        return timeline
