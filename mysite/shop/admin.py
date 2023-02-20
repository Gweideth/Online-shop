from django.contrib import admin
from .models import Post


@admin.register(Post)  # means the same as "admin.site.register()
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "status")
    list_filter = ("status", "author", "published_date")
    search_fields = ("title", "body")
    date_hierarchy = "published_date"
    ordering = ("status", "published_date")



