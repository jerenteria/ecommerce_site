from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home),
    path('checkout', views.checkout),
    path('<int:product_id>/product', views.one_item),
    path('<int:product_id>/add-to-cart', views.try_cart),
    path('render_total', views.checkout),
    path('pay', views.checkout),
]