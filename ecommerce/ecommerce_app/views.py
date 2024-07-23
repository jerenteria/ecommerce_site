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


# serializes the data(turns django models into JSON so that the react front end can read it)
def serialize_data(request):
    data = Product.objects.all().values(
        "id", "title", "price", "image"
    )  # Query existing data
    serialized_data = list(data)
    return JsonResponse(serialized_data, safe=False)


def home(request):
    return render(request, "index.html")


@csrf_exempt # Exempts this view from CSRF protection. Used when you want to allow POST request without CSRF token
@never_cache # prevents the view from being cached by the browser
def add_to_cart(request):
    if request.method == "POST":
        # Parces(breaks down) JSON data sent in the request body
        data = json.loads(request.body)
        print(f"Request data: {data}")
        # Gets(extracts) the product_id
        product_id = data.get("product_id")
        # Gets(extracts) quanitity from request data, if quantity is not provided it defaults to 1
        quantity = data.get("quantity", 1)
        # Retreives(gets) object with the given product_id or returns error 404 not found
        product = get_object_or_404(Product, id=product_id)

        # Gets the cart from the session, or initializes an empty dictionary if it doesn't exist
        cart = request.session.get("cart", {})
        print(f"Cart before adding item: {cart}")
        # Check if the product is already in the cart using the product_id
        if str(product_id) in cart:
            # Increase the quantity
            cart[str(product_id)]["quantity"] += quantity
            print(f"increased quantity for product {product_id}")
        # If its not already in the cart then add it to the cart
        else:
            cart[str(product_id)] = {
                "title": product.title,
                "price": product.price,
                "image": product.image.url if product.image else "",
                "quantity": quantity,
            }
            print(f"added new product {product_id} to cart")
        # Update the cart in the session with all the items added    
        request.session["cart"] = cart
        # Mark the session as modified
        request.session.modified = True
        print(f"Cart after adding item: {cart}")

        # Creates a list of cart items, each including its product_id

        {"product_id": k, **v}: This creates a new dictionary for each item in the cart:


        # {"product_id": k, **v}: This creates a new dictionary for each item in the cart
        # "product_id": k adds a new key-value pair where the key is "product_id" and the value is the product ID (the key from the original cart dictionary).
        # **v is the dictionary unpacking operator. It takes all the key-value pairs from the original product details dictionary (v) and includes them in this new dictionary.

        # for k, v in cart.items(): This iterates over each key-value pair in the cart.
        # Here, k represents the key (which is the product_id as a string), and v represents the value (which is a dictionary containing the product details).

        # cart.items(): This method returns a view of the cart dictionary's key-value pairs as tuples.
        cart_items = [{"product_id": k, **v} for k, v in cart.items()]
        # Returns a JSON response indicating successfully adding item to cart
        return JsonResponse(
            {"status": "success", "message": "Item added to cart", "cart": cart_items}
        )

    # If the request method is not post then render an error message
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
@never_cache
def remove_from_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(f"Remove from cart request data: {data}")
        product_id = str(data.get("product_id"))
        quantity = data.get("quantity", 1)

        cart = request.session.get("cart", {})
        print(f"Cart before removing item: {cart}")

        if product_id in cart:
            if cart[product_id]["quantity"] <= quantity:
                del cart[product_id]
                print(f"Removed product {product_id} from cart")
            else:
                cart[product_id]["quantity"] -= quantity
                print(f"Decreased quantity for product {product_id}")

            request.session["cart"] = cart
            request.session.modified = True  # Ensure the session is saved
            print(f"Cart after removing item: {cart}")

            cart_items = [{"product_id": k, **v} for k, v in cart.items()]
            return JsonResponse(
                {"status": "success", "message": "Item removed from cart", "cart": cart_items}
            )
        else:
            return JsonResponse(
                {"status": "error", "message": "Item not in cart"}, status=400
            )

    return JsonResponse(
        {"status": "error", "message": "Invalid request method"}, status=400
    )

@csrf_exempt
def checkout(request):
    try:
        data = json.loads(request.body)
        cart = data.get("cart", [])
        if not cart:
            return JsonResponse({"error": "Cart is empty"}, status=400)

        line_items = []
        for item in cart:
            line_items.append(
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": item["title"],
                        },
                        "unit_amount": int(item["price"] * 100),
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

        return JsonResponse({"url": session.url})

    except json.JSONDecodeError:
        logger.error("Invalid JSON in request body")
        return JsonResponse({"error": "Invalid JSON in request body"}, status=400)
    except stripe.error.StripeError as e:
        logger.error(f"Stripe error: {str(e)}")
        return JsonResponse({"error": str(e)}, status=400)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return JsonResponse({"error": "An unexpected error occurred"}, status=500)


def success(request):
    return redirect("success.html")


def cancel(request):
    return render("cancel.html")
