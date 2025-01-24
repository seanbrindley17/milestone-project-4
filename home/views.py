from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import Category, Product
from .forms import ProductForm

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


# View for an admin to add product to store
def add_product(request):

    if request.method == "POST":
        # Needs request.FILES to get the image posted too
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Added Product Successfully")
            return redirect(reverse("add_product"))
        else:
            messages.error(
                request, "Failed to add product. Check form is filled out correctly."
            )
    form = ProductForm

    template = "home/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm
    messages.info(request, f"Editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)
