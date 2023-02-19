from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.news_list, name="news_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:news>",
         views.news_detail,
         name="news_detail")
]