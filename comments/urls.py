from django.urls import path
from .views.comment_info import CommentInfo
from .views.comment_create import CommentCreate
from .views.comment_delete import CommentDelete
from .views.comment_list import CommentList

app_name = "comments"
urlpatterns = [
    path("api/info/<int:pk>", CommentInfo.as_view(), name="info"),
    path("api/create/<int:pk>", CommentCreate.as_view(), name="create"),
    path("api/create/<int:pk>/<int:comment>", CommentCreate.as_view(), name="reply"),
    path("api/delete/<int:pk>", CommentDelete.as_view(), name="delete"),
    path("api/list", CommentList.as_view(), name="comments_list"),
]
