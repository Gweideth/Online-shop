from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "shop"

urlpatterns = [
    path("store/",
         views.product_list,
         name="product_list"),
    path("store/<slug:category_slug>/",
         views.product_list,
         name="product_list_by_category"),
    path("store/<int:id>/<slug:slug>/",
         views.product_detail,
         name="product_detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
