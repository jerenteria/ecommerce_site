from django.shortcuts import render, redirect
from .models import *
import stripe, os

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['STRIPE_SECRET_KEY']

def home(request):
    return render(request, "index.html")



def checkout(request):
  session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'Sweater',
        },
        'unit_amount': 2999,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://127.0.0.1:8000/',
    cancel_url='http://127.0.0.1:8000/',
  )

  return redirect(session.url, code=303)


def success(request):
    return redirect("success.html")

def cancel(request):
    return render("cancel.html")


