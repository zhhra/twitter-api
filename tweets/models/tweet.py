from django.db import models
from accounts.models.user import User
from django.template.defaultfilters import truncatewords


class Tweet(models.Model):
    author = models.ForeignKey(User, related_name="tweets", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    tweet_body = models.TextField(max_length=148, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="liked_tweets", blank=True)
    quote = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        default=None,
        related_name="the_main_tweet",
        blank=True,
        null=True,
    )
    quote_body = models.TextField(max_length=148, blank=True, null=True)
    retweet = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        default=None,
        related_name="main_tweet",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        if not self.quote:
            return f"{self.tweet_body}"
        return f"{self.quote_body}"

    def likes_count(self):
        return self.likes.count()

    def body_truncation(self):
        if not self.quote:
            return truncatewords(self.tweet_body, 10)
        return truncatewords(self.quote_body, 10)

    body_truncation.short_description = "body"
