from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'published_date', "category"]
    list_filter = ['available', "published_date"]
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

