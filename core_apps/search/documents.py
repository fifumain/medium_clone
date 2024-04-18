from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from core_apps.articles.models import Article


# creating new document for search
@registry.register_document
class ArticleDocument(Document):
    title = fields.TextField(attr="title")
    description = fields.TextField(attr="description")
    body = fields.TextField(attr="body")
    # no arrt, because we use methods for this fields below
    author_first_name = fields.TextField()
    author_last_name = fields.TextField()
    tags = fields.KeywordField()

    # same as class META in django models etc.
    class Index:
        name = "articles"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    # set up reference to django
    class Django:
        model = Article
        fields = ["created_at"]

    def prepare_author_first_name(self, instance):
        return instance.author.first_name

    def prepare_author_last_name(self, instance):
        return instance.author.last_name

    # returning all the tags, that article has
    def prepare_tags(self, instance):
        return [tag.name for tag in instance.tags.all()]
