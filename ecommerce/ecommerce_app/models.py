from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# CATEGORY_CHOICES = (
#     ('S', 'Shirt'),
#     ('SW', 'Sweater')
# )

# LABEL_CHOICES = (
#     ('S', 'primary'),
#     ('SW', 'secondary')
# )

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    # category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    # label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    # slug = models.SlugField()

    
    # slugs are used to store urls 
    # since spaced dont work in urls they are stored in slugs to prevent all the spaces
    # if i wanted to refer to my post with an id=2 then i can refer to it with www.ecommerce.com/2
    # we would not be able to refer to it like www.ecommerce.com/juans second blog post
        # all the spaced would be replaced with "%" and it would look ugly
    # instead it is storing www.ecommerce.com/juans-second-blog-post
    # def get_absolute_url(self):
    #     # going to go back to product url
    #     return reverse("core:product", kwargs={
    #         'slug': self.slug
    #     })

    # def get_add_to_cart_url(self):
    #             # going to go back to product url
    #     return reverse("core:add-to-cart", kwargs={
    #         'slug': self.slug
    #     })


# class OrderItem(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items_ordered = models.ManyToManyField(Product, related_name="orders")
    quantity = models.IntegerField()
    total = models.FloatField()
    ordered_date = models.DateTimeField(null=True)


