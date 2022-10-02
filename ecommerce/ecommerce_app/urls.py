from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home),
    path('checkout', views.checkout),
    path('checkout2', views.checkout2),
    path('success', views.success),
    path('cancel', views.cancel),
    # path('<int:product_id>/product', views.one_item),
    # path('<int:product_id>/add-to-cart', views.try_cart),
    # path('render_total', views.checkout),
    # path('pay', views.checkout),
    # path('create-checkout-session', views.create_checkout_session),
    # path('render_stripe', views.render_stripe),
]