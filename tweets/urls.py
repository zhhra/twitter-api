from django.urls import path
from .views.like import like
from .views.timeline import Timeline
from .views.tweet_info import TweetInfo
from .views.tweet_create import TweetCreate
from .views.tweet_delete import TweetDelete
from .views.like_info import LikeInfo
from .views.quote import Quote
from .views.retweet import Retweet
from .views.search import TweetListView
from .views.tweet_document_view import TweetDcoumentView

app_name = "tweet"
urlpatterns = [
    path("tweet/info/api/<int:pk>", TweetInfo.as_view(), name="info"),
    path("tweet/create/api", TweetCreate.as_view(), name="create"),
    path("tweet/delete/api/<int:pk>", TweetDelete.as_view(), name="delete"),
    path("tweet/likedby/api/<int:pk>", LikeInfo.as_view(), name="liked_by"),
    path("tweet/like/api/<int:pk>", like, name="like"),
    path("timeline/api", Timeline.as_view(), name="timeline"),
    path("tweet/search/api", TweetListView.as_view(), name="search"),
    path(
        "tweets/search/api", TweetDcoumentView.as_view({"get": "list"}), name="search"
    ),
    path("quote/api/<int:pk>", Quote.as_view(), name="quote"),
    path("retweet/api/<int:pk>", Retweet.as_view(), name="retweet"),
]
