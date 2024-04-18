from django.contrib import admin

from . import models


# default setup for articles in admin panel
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "author",
        "title",
        "slug",
        "view_count",
    ]
    list_display_links = [
        "pkid",
        "author",
    ]
    list_filter = [
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "title",
        "body",
        "tags",
    ]
    ordering = [
        "-created_at",
    ]


# default setup for the views of articles in admin panel
class ArticleViewAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "article",
        "user",
        "viewer_ip",
    ]
    list_display_links = [
        "pkid",
        "article",
    ]
    list_filter = [
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "article",
        "user",
        "viewer_ip",
    ]


# default setup for article claps in admin panel
class ClapAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "user", "article"]
    list_display_links = ["id", "user"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.ArticleView, ArticleViewAdmin)
admin.site.register(models.Clap, ClapAdmin)
