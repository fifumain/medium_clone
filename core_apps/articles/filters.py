import django_filters as filters

from core_apps.articles.models import Article


class ArticleFilter(filters.FilterSet):
    # icontains stands for containing the specified value (case insensitive).
    author = filters.CharFilter(
        field_name="author__First_name", lookup_expr="icontains"
    )
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    # iexact stands for 1:1 relation
    tags = filters.CharFilter(field_name="tags", lookup_expr="iexact")
    created_at = filters.DateFromToRangeFilter(field_name="created_at")
    updated_at = filters.DateFromToRangeFilter(field_name="updated_at")

    class Meta:
        model = Article
        fields = ["author", "title", "tags", "created_at", "updated_at"]
