from django.shortcuts import render, get_object_or_404
from .models import News


def news_list(request):
    news = News.published.all()
    return render(request,
                  "shop/news/list.html",
                  {"news": news})


def news_detail(request, year, month, day, news):
    news = get_object_or_404(News, slug=news,
                             status="published",
                             published_year=year,
                             published_month=month,
                             published_day=day)
    return render(request,
                  "blog/news/detail.html",
                  {"news": news})
