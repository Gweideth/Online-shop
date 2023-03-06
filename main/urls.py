from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.LatestNewsListView.as_view(), name="main"),
]