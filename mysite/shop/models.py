from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="news")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title
