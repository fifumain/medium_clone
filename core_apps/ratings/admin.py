from .models import Rating
from django.contrib import admin


class RatingAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "article",
        "rating",
        "created_at",
        "updated_at",
    ]


admin.site.register(Rating, RatingAdmin)
