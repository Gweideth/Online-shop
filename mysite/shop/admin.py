from django.contrib import admin
from .models import Post, Comments


@admin.register(Post)  # means the same as "admin.site.register()
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "status")
    list_filter = ("status", "author", "published_date")
    search_fields = ("title", "body")
    date_hierarchy = "published_date"
    ordering = ("status", "published_date")


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "comment", "published_date")
    list_filter = ("author", "published_date")
    search_fields = ("author", "body")



