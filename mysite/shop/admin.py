from django.contrib import admin
from .models import News


@admin.register(News)  # means the same as "admin.site.register()
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "status")
    list_filter = ("status", "author", "published_date")
    search_fields = ("title", "body")
    date_hierarchy = "published_date"
    ordering = ("status", "published_date")



