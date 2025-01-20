from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Category, Product

# Create your views here.


def index(request):
    products = Product.objects.all()

    products = products.order_by("name")

    context = {"products": products}

    return render(request, "home/index.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {"product": product}

    return render(request, "home/product_detail.html", context)
