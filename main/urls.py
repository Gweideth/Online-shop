from django.urls import path
from main.views import AnnouncementListView

app_name = "main"

urlpatterns = [
    path("",
         AnnouncementListView.as_view(),
         name="main"),
]