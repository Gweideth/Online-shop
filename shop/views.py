from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Comments, Category, Product
from .forms import CommentForm
from cart.forms import CartAddForm


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 5
    template_name = "shop/post/list.html"


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
                  "shop/post/detail.html",
                  {"post": post,
                   "comments": comments,
                   "comment_form": comment_form})

# STORE


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddForm()

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   "cart_product_form": cart_product_form})

# MAIN_SITE

