from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):  # possibility to change code to simpler
    # https://docs.djangoproject.com/pl/4.1/topics/class-based-views/generic-display/
    posts = Post.published.all()
    return render(request,
                  "shop/post/list.html",
                  {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status="published",
                             published_date__year=year,
                             published_date__month=month,
                             published_date__day=day)
    return render(request,
                  "shop/post/detail.html",
                  {"post": post})
