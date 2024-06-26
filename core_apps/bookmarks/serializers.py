from rest_framework import serializers

from .models import Bookmark


# Nothing special, simple serializer class of bookmarks model
class BookmarkSerializer(serializers.ModelSerializer):
    article_title = serializers.CharField(source="article.title", read_only=True)
    user_fisrt_name = serializers.CharField(source="user.fisrt_name", read_only=True)

    class Meta:
        model = Bookmark
        fields = [
            "id",
            "user_fisrt_name",
            "article_title",
            "created_at",
        ]
        read_only_fields = ["user"]
