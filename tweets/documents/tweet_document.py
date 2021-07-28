from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer
from ..models.tweet import Tweet

TWEET_INDEX = Index("tweet")

TWEET_INDEX.settings(number_of_shards=1, number_of_replicas=0)

html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)


@TWEET_INDEX.doc_type
class TweetDocument(Document):

    author = fields.ObjectField(
        attr="author",
        properties={
            "username": fields.TextField(
                analyzer=html_strip,
            ),
        },
    )

    likes = fields.TextField(
        attr="likes_count",
    )

    quote = fields.ObjectField(
        attr="quote",
        properties={
            "tweet_body": fields.TextField(
                analyzer=html_strip,
            ),
            "quote_body": fields.TextField(
                analyzer=html_strip,
            ),
        },
    )

    retweet = fields.ObjectField(
        attr="retweet",
        properties={
            "tweet_body": fields.TextField(
                analyzer=html_strip,
            ),
            "quote_body": fields.TextField(
                analyzer=html_strip,
            ),
        },
    )

    class Django:
        model = Tweet
        fields = [
            "created",
            "tweet_body",
            "quote_body",
        ]
