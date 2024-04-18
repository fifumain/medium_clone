from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import ArticleDocument


# just default serialization, like in other apps
class ArticleElasticSearchSerializer(DocumentSerializer):
    class Meta:
        document = ArticleDocument
        fields = ["title", "author", "slug", "description", "body", "created_at"]
