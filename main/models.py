from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class AboutUs(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
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