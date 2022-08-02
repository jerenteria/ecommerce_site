from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    context = {
        'all_products': Product.objects.all(),
        'quantity': [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, "index.html", context)

def render_products(request):
    context = {
        'all_products': Product.objects.all(),
        'quantity': [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, "index.html", context)
