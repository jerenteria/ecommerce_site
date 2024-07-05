from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import stripe, os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
import json
import logging

from django.conf import settings

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]


def serialize_data(request):
    data = Product.objects.all().values(
        "id", "title", "price", "image"
    )  # Query existing data
    serialized_data = list(data)
    return JsonResponse(serialized_data, safe=False)


def home(request):
    return render(request, "index.html")


@csrf_exempt
@never_cache
def add_to_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(f"Request data: {data}")
        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)
        product = get_object_or_404(Product, id=product_id)

        cart = request.session.get("cart", {})
        print(f"Cart before adding item: {cart}")
        if str(product_id) in cart:
            cart[str(product_id)]["quantity"] += quantity
        else:
            cart[str(product_id)] = {
                "title": product.title,
                "price": product.price,
                "image": product.image.url if product.image else "",
                "quantity": quantity,
            }
        request.session["cart"] = cart
        request.session.modified = True  # Ensure the session is saved
        print(f"Cart after adding item: {cart}")

        cart_items = [{"product_id": k, **v} for k, v in cart.items()]
        return JsonResponse(
            {"status": "success", "message": "Item added to cart", "cart": cart_items}
        )

    return JsonResponse(
        {"status": "error", "message": "Invalid request method"}, status=400
    )


@csrf_exempt
def get_cart_items(request):
    # get the "cart" stored in the session, if there is none then return an empty dictionary
    cart = request.session.get("cart", {})
    print(f"Fetching items in cart: {cart}")
    # converts the cart dictionary into a list of dictionaries
    # k is the "product_id", v is the dictionary of product details, it creates a new dictionary for each item
    # adds product id as the key "product_id" and unpacking the other key-value pairs from 'v' into the new dictionary
    # (iterates over each key-value pair in the cart dictionary )
    cart_items = [{"product_id": k, **v} for k, v in cart.items()]
    print(f"Cart items to be returned: {cart_items}")
    return JsonResponse(cart_items, safe=False)


@csrf_exempt
def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        return JsonResponse({"status": "error", "message": "Cart is empty"})

    line_items = []
    for item in cart.values():
        line_items.append(
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item["title"],
                    },
                    "unit_amount": int(
                        item["price"] * 100
                    ),  # Stripe expects amount in cents
                },
                "quantity": item["quantity"],
            }
        )

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url="http://127.0.0.1:8000/success/",
        cancel_url="http://127.0.0.1:8000/cancel/",
    )

    # Clear the cart
    request.session["cart"] = {}

    return JsonResponse({"url": session.url})


# def checkout(request):
#   session = stripe.checkout.Session.create(
#     line_items=[{
#       'price_data': {
#         'currency': 'usd',
#         'product_data': {
#           'name': 'Sweater',
#         },
#         'unit_amount': 2999,
#       },
#       'quantity': 1,
#     }],
#     mode='payment',
#     success_url='http://127.0.0.1:8000/f',
#     cancel_url='http://127.0.0.1:8000/',
#   )

#   return redirect(session.url, code=303)

# def checkout2(request):
#   session = stripe.checkout.Session.create(
#     line_items=[{
#       'price_data': {
#         'currency': 'usd',
#         'product_data': {
#           'name': 'Sweater',
#         },
#         'unit_amount': 2599,
#       },
#       'quantity': 1,
#     }],
#     mode='payment',
#     success_url='http://127.0.0.1:8000/',
#     cancel_url='http://127.0.0.1:8000/',
#   )

#   return redirect(session.url, code=303)


def success(request):
    return redirect("success.html")


def cancel(request):
    return render("cancel.html")
