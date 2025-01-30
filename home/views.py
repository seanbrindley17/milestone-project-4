from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Category, Product
from .forms import ProductForm, NewsletterSignupForm

# Create your views here.


def index(request):
    products = Product.objects.all()
    categories = None

    # For filtering by category
    if "category" in request.GET:
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
@login_required
def add_product(request):

    if not request.user.is_superuser:
        messages.error(request, "Only accessible to admins")
        return redirect(reverse("home"))

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


# View for an admin to edit a product
@login_required
def edit_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, "Only accessible to admins")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        # On a edit form post request, pre fill using instance of product got above using product id
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Edit successful")
            return redirect(reverse("product_detail", args=[product_id]))
        else:
            messages.error(request, "Error editing product, double check fields")

    form = ProductForm(instance=product)
    messages.info(request, f"Editing {product.name}")

    template = "home/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


# View to allow an admin to delete products from the database
@login_required
def delete_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, "Only accessible to admins")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted")
    return redirect(reverse("home"))


def newsletter(request):
    if request.method == "POST":
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing to the newsletter")
            return redirect("home")
        else:
            messages.error(request, "Something went wrong, please try again.")

    return redirect("home")
