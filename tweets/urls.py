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
from .views.tweet_document_view import TweetDocumentView

app_name = "tweet"
urlpatterns = [
    path("api/tweet/info/<int:pk>", TweetInfo.as_view(), name="info"),
    path("api/tweet/create", TweetCreate.as_view(), name="create"),
    path("api/quote/<int:pk>", Quote.as_view(), name="quote"),
    path("api/retweet/<int:pk>", Retweet.as_view(), name="retweet"),
    path("api/tweet/delete/<int:pk>", TweetDelete.as_view(), name="delete"),
    path("api/tweet/likedby/<int:pk>", LikeInfo.as_view(), name="liked_by"),
    path("api/tweet/like/<int:pk>", like, name="like"),
    path("api/timeline", Timeline.as_view(), name="timeline"),
    path("api/tweet/search", TweetListView.as_view(), name="search"),
    path(
        "api/tweets/search", TweetDocumentView.as_view({"get": "list"}), name="search"
    ),
]
