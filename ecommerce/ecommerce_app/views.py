from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import *
import stripe, os

from dotenv import load_dotenv

load_dotenv()

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


stripe.api_key = os.environ['STRIPE_SECRET_KEY']

def home(request):
    context = {
        'all_products': Product.objects.all(),
        'quantity':[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, "index.html", context)


def try_cart(request, product_id):
    if request.method=='POST':
        product = Product.objects.get(id=product_id)
        new_order = Order.objects.create(quantity=int(request.POST['quantity']), total=int(request.POST['quantity'])*product.price)
        new_order.items_ordered.add(product)
    return redirect('/checkout') # renders wherever function checkout does


def checkout(request):
    all_orders = Order.objects.all()
    total_spent = 0
    for order in all_orders:
        total_spent += order.total
    context = {
        'last_order': Order.objects.last(),
        'all_orders': all_orders,
        'grand_total': total_spent,
    }
    return render(request, "cart.html", context)


def create_checkout_session():
  session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'title': 'shirt',
          'title': 'sweater'
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://127.0.0.1:8000/success',
    cancel_url='/',
  )
  return redirect(session.url, code=303)

def render_stripe(request):
    return render(request, "payment.html")

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


def one_item(request, product_id):
    one_item = Product.objects.get(id=product_id)
    context = {
        'item': one_item
    }
    return render(request, 'product.html', context)


