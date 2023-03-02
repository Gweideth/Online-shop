from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "news"

urlpatterns = [
    path("news/", views.PostListView.as_view(),
         name="post_list"),
    path("news/<int:year>/<int:month>/<int:day>/<slug:post>",
         views.post_detail,
         name="post_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)