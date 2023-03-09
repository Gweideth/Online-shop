from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news.views import PostListView, post_detail

app_name = "news"

urlpatterns = [
    path("news/",
         PostListView.as_view(),
         name="post_list"),
    path("news/<int:year>/<int:month>/<int:day>/<slug:post>",
         post_detail,
         name="post_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)