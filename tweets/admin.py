from django.contrib import admin
from .models.tweet import Tweet


admin.site.site_header = "TWITTER API"


class TweetAdmin(admin.ModelAdmin):
    list_display = ["body_truncation", "author", "created", "likes_count"]
    list_filter = ["created"]
    search_fields = ["author", "tweet_body", "quote_body", "created"]
    ordering = ["-created", "author"]


admin.site.register(Tweet, TweetAdmin)
