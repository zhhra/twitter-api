from ..models.tweet import Tweet
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


@login_required
def like(request, pk):
    user = request.user
    tweet = get_object_or_404(Tweet, pk=pk)
    if user in tweet.likes.all():
        tweet.likes.remove(user)
    else:
        tweet.likes.add(user)
    return redirect("tweet:info", pk=pk)
