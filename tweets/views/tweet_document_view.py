from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from ..documents.tweet_document import TweetDocument
from ..serializers.tweet_document_serializer import TweetDocumentSerializer


class TweetDcoumentView(DocumentViewSet):
    document = TweetDocument
    serializer_class = TweetDocumentSerializer
    filter_backends = [SearchFilterBackend]
    search_fields = ["tweet_body", "quote_body"]
