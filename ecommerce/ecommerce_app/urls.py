from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", views.home),
    path("checkout", views.checkout),
    path("checkout2", views.checkout2),
    path("success", views.success),
    path("cancel", views.cancel),
    path("api/data", views.serialize_data),
]
