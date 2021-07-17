from django.db import models
from accounts.models.user import User
from tweets.models.tweet import Tweet


class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, related_name="comments", on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField(max_length=148)
    created = models.DateTimeField(auto_now_add=True)
    in_reply_to = models.ForeignKey(
        "self",
        default=None,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reply_comments",
    )

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.body
