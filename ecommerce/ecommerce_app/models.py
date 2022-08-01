from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity = models.IntegerField() 
    total_charge = models.IntegerField()
    items_ordered = models.ManyToManyField(Product, related_name="orders")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)