from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Category, Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    categories = None

    # For filtering by category
    if request.GET:
        categories = request.GET["category"].split(",")
        products = products.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    # Ensures products are always ordered alphabetically
    products = products.order_by("name")

    context = {
        "products": products,
        "currect_categories": categories,
    }

    return render(request, "home/index.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {"product": product}

    return render(request, "home/product_detail.html", context)
