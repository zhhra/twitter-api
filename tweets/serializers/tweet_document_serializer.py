from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from ..documents.tweet_document import TweetDocument


class TweetDocumentSerializer(DocumentSerializer):
    class Meta:
        document = TweetDocument
        fields = [
            "id",
            "author",
            "created",
            "tweet_body",
            "likes",
            "quote_body",
            "quote",
            "retweet",
        ]
