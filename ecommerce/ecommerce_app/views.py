from django.shortcuts import render, redirect
from .models import *
import stripe, os

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['STRIPE_SECRET_KEY']

def home(request):
    return render(request, "index.html")


def checkout(request):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price': 'price_1LXGBFIuO4V9XiaItcrmeK8S',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='/',
        cancel_url='/',
    )
    return redirect(checkout_session.url, code=303)




# def try_cart(request, product_id):
#     if request.method=='POST':
#         product = Product.objects.get(id=product_id)
#         new_order = Order.objects.create(quantity=int(request.POST['quantity']), total=int(request.POST['quantity'])*product.price)
#         new_order.items_ordered.add(product)
#         print(product_id)
#     return redirect('/checkout') # renders wherever function checkout does


# def checkout(request):
#     all_orders = Order.objects.all()
#     total_spent = 0
#     for order in all_orders:
#         total_spent += order.total
#     context = {
#         'last_order': Order.objects.last(),
#         'all_orders': all_orders,
#         'grand_total': total_spent,
#     }
#     return render(request, "cart.html", context)