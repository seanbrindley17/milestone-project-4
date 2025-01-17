import stripe
from decimal import Decimal
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from trolley.contexts import trolley_items
from .forms import OrderForm


# Create your views here.


# View for the checkout
def view_checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    stripe.api_key = stripe_secret_key

    trolley = request.session.get("trolley", {})
    # If nothing is in the trolley dictionary
    if not trolley:
        # Display error message
        messages.error(request, "No items in trolley")
        # Return user to home page to prevent access by inputting the checkout url
        return redirect(reverse("home"))

    trolley_items_context = trolley_items(request)
    order_cost = trolley_items_context["order_cost"]
    delivery_charge = trolley_items_context["delivery_charge"]
    total_cost = trolley_items_context["total_cost"]

    order_form = OrderForm()
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": "test client secret",
    }
    template = "checkout/checkout.html"

    return render(request, template, context)
