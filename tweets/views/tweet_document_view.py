from ..documents.tweet_document import TweetDocument
from ..serializers.tweet_model_serializer import TweetModelSerializer
from rest_framework import viewsets
from ..models.tweet import Tweet
from elasticsearch_dsl.query import MultiMatch
from itertools import chain


class TweetDocumentView(viewsets.ModelViewSet):
    serializer_class = TweetModelSerializer

    def get_queryset(self):
        param = self.request.query_params.get("search")
        if param:
            s = TweetDocument.search()
            x = True
            try:
                qs1 = s.filter("match", created=param).to_queryset()
            except:
                x = False
            finally:
                qs2 = s.query(
                    MultiMatch(
                        query=param,
                        fields=["tweet_body", "quote_body", "author.username"],
                    )
                ).to_queryset()
            if x:
                return list(set(chain(qs1, qs2)))
                # does chain do set or not
            return qs2

        return Tweet.objects.all()
