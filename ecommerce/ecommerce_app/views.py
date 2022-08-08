from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import *

# renders all items
# class based view is easier to create reusable components
class HomeView(ListView):
    model = Item
    template_name = "index.html"

# function based view; how i used to render items
    # def index(request):
    #     context = {
    #         'items': Item.objects.all(),
    #     }
    #     return render(request, "index.html", context)

class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug) # check to see if user has item or not
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in the order
        if order.items.filter(items__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("core:product", kwargs= {
        'slug': slug
    })

def checkout(request):
    return render(request, "cart.html")

