from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    # upload_to='static/' will create a media file in root directory where the images will be stored
    image = models.ImageField(upload_to='static/', blank=True, null=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)
    products = models.ManyToManyField(Product, through="CartItem") # allow many users to add many products to cart

    def add_product(self, product, quantity=1):
        cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items_ordered = models.ManyToManyField(Product, related_name="orders")
    quantity = models.IntegerField()
    total = models.FloatField()
    ordered_date = models.DateTimeField(null=True)


