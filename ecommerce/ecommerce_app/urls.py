from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home),
    path('checkout', views.checkout),
    path('<int:product_id>/product', views.one_item),
    path('add-to-cart', views.try_cart)
]