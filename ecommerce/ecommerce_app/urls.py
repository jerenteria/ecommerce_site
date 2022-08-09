from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', HomeView.as_view()),
    path('checkout', views.checkout),
    path('<int:item_id>/product', views.one_item),
    path('add-to-cart/add_to_cart_url', views.add_to_cart)
]