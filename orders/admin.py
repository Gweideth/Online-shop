from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email", "postal_code", "city", "address", "created", "paid"]
    list_filter = ["paid", "created"]
    inlines = [OrderItemInline]