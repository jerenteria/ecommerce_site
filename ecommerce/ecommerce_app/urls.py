from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", views.home),
    path("success", views.success),
    path("cancel", views.cancel),
    path("api", views.serialize_data),
    path("api/add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("api/get_cart_items/", views.get_cart_items, name="get_cart_items"),
    path("api/checkout/", views.checkout, name="checkout"),
]
