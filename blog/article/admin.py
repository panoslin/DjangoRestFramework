from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "desc",
        "content",

        "status",

        "author",
    )

    list_display = ("id", "title", "status", "author")
    list_display_links = ("id", "title")

    list_filter = ("status",)

    search_fields = ("title", "desc", "content", "author")
