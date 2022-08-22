from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import *
import stripe, os
from flask import Flask, redirect, request, jsonify

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


app = Flask(__name__,
            static_url_path='',
            static_folder='public')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session(str):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1LXGBFIuO4V9XiaItcrmeK8S',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/success.html',
            cancel_url='/'
        )
    except Exception as e:
        return str(e)

    return render(checkout_session.url, code=303)



def render_stripe(request):
    return render(request, "payment.html")



def one_item(request, product_id):
    one_item = Product.objects.get(id=product_id)
    context = {
        'item': one_item
    }
    return render(request, 'product.html', context)


