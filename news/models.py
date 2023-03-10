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
    announcement = models.BooleanField(default=False)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ("-published_date",)
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:post_detail",
                       args=[self.published_date.year,
                             self.published_date.strftime("%m"),
                             self.published_date.strftime("%d"),
                             self.slug])


class Comments(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments")
    author = models.CharField(max_length=30)
    body = models.CharField(max_length=200, help_text="Maksymalnie 200 znaków")
    published_date = models.DateTimeField(default=timezone.now())
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("published_date",)
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Komentarz dodany przez {self.author}"


