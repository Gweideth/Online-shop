from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.urls import cart_detail, cart_add, cart_remove


class TestUrls(SimpleTestCase):

    def test_cart_add_resolved(self):
        url = reverse("cart:cart_add", kwargs={"product_id":1})
        self.assertEquals(resolve(url).func, cart_add)

    def test_cart_remove_resolved(self):
        url = reverse("cart:cart_remove", kwargs={"product_id":1})
        self.assertEquals(resolve(url).func, cart_remove)

    def test_cart_detail_resolved(self):
        url = reverse("cart:cart_detail")
        self.assertEquals(resolve(url).func, cart_detail)