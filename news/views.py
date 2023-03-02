from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Comments
from .forms import CommentForm


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "news/post/list.html"


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status="published",
                             published_date__year=year,
                             published_date__month=month,
                             published_date__day=day)

    comments = post.comments.filter(active=True)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                  "news/post/detail.html",
                  {"post": post,
                   "comments": comments,
                   "comment_form": comment_form})


