from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('purchase/<int:product_id>', views.process_purchase),
]