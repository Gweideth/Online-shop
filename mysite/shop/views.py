from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  "shop/post/list.html",
                  {"page": page,
                  "posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status="published",
                             published_date__year=year,
                             published_date__month=month,
                             published_date__day=day)
    return render(request,
                  "shop/post/detail.html",
                  {"post": post})
