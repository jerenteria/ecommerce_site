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


class Order(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items_ordered = models.ManyToManyField(Product, related_name="orders")
    quantity = models.IntegerField()
    total = models.FloatField()
    ordered_date = models.DateTimeField(null=True)


