from django.shortcuts import render
from django.views.generic import ListView
from news.models import Post


class AnnouncementListView(ListView):
    queryset = Post.published.filter(announcement=True)
    context_object_name = "announcement"
    template_name = "main/about_us/about_us.html"
