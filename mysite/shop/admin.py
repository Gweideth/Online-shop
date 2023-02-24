from django.contrib import admin
from .models import Post, Comments


@admin.register(Post)  # means the same as "admin.site.register()
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "status")
    list_filter = ("status", "author", "published_date")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_date"
    ordering = ("status", "published_date")


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "published_date", "active")
    list_filter = ("author", "published_date", "active")
    search_fields = ("author", "body")



