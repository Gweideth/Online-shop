from django.shortcuts import render
from django.views.generic import ListView
from news.models import Post


class LatestNewsListView(ListView):
    queryset = Post.published.filter(announcement=True)
    context_object_name = "latest_news"
    template_name = "main/about_us/about_us.html"
