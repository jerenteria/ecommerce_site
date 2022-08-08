from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', HomeView.as_view()),
    path('checkout', views.checkout),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>', views.add_to_cart)
]