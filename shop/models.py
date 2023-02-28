from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200,
                            unique_for_date="published_date",
                            default="")
    image = models.ImageField(upload_to='posts/%Y/%m/%d',
                              blank=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="shop_posts")
    body = models.TextField(default="")
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default="draft")
    published_date = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ("-published_date",)
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:post_detail",
                       args=[self.published_date.year,
                             self.published_date.strftime("%m"),
                             self.published_date.strftime("%d"),
                             self.slug])


class Comments(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments")
    author = models.CharField(max_length=30)
    body = models.CharField(max_length=200)
    published_date = models.DateTimeField(default=timezone.now())
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("published_date",)
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Komentarz dodany przez {self.author}"

# STORE


class Category(models.Model):
    name = models.CharField(max_length=100,
                            db_index=True)
    slug = models.SlugField(max_length=100,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100,
                            db_index=True)
    slug = models.SlugField(max_length=100,
                            db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])