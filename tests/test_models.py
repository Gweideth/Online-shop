from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from shop.models import Category, Product
from news.models import Post, Comments


class TestModels(TestCase):
    def test_shop(self):
        self.category = Category.objects.create(name="GPS",
                                                slug="gps")
        self.product = Product.objects.create(category=self.category,
                                              slug="GPS001",
                                              image=None,
                                              description="testing_description",
                                              price=500.00,
                                              available=True,
                                              published_date=timezone.now())

    def test_news(self):
        self.post = Post.objects.create(title="testing title",
                                        slug="testing_title",
                                        image=None,
                                        author=User.objects.create(),
                                        body="testing body",
                                        status="published",
                                        published_date=timezone.now(),
                                        announcement=True)
        self.comment = Comments.objects.create(post=self.post,
                                               author="tester",
                                               body="testing body",
                                               published_date=timezone.now(),
                                               active=True)

