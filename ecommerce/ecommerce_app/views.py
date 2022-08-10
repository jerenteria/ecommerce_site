from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import *

# renders all items
# class based view is easier to create reusable components
# class HomeView(ListView):
#     model = Item
#     template_name = "index.html"

# function based view; how i used to render items
    # def index(request):
    #     context = {
    #         'items': Item.objects.all(),
    #     }
    #     return render(request, "index.html", context)

# class ItemDetailView(DetailView):
#     model = Item
#     template_name = "product.html"


def home(request):
    context = {
        'all_products': Product.objects.all(),
    }
    return render(request, "index.html", context)


def try_cart(request):
    if request.method=='POST':
        item = Item.objects.get(id=item_id)
        new_order = Order.objects.create(quantity=int(request.POST['quantity']), total_charge=int(request.POST['quantity'])*product.price)
        new_order.items.add(items)
        return redirect('/')
    return redirect('/')


# def add_to_cart(request):
#     # item = get_object_or_404(Item) #slug=slug) # check to see if user has item or not
#     order_item = OrderItem.objects.create(item=item)
#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if order item is in the order
#         if order.items.filter(item__id=item.id).exists():
#             order_item.quantity += 1
#             order_item.save()
#     else:
#         order_date = timezone.now()
#         order = Order.objects.create(user=request.user, ordered_date=ordered_date)
#         order.item.add(order_item)
#     return redirect('/index')

def checkout(request):
    return render(request, "cart.html")

def one_item(request, item_id):
    one_item = Item.objects.get(id=item_id)
    context = {
        'item': one_item
    }
    return render(request, 'product.html', context)