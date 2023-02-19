from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="news")
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.title


class Comments(models.Model):
    comment = models.ForeignKey(News,
                                on_delete=models.CASCADE,
                                related_name="comments")
    author = models.CharField(max_length=30)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return f"Komentarz dodany przez {self.author}"
