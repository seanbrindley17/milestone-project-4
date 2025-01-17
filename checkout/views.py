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

    # trolley items and costs
    trolley_items_context = trolley_items(request)
    order_cost = trolley_items_context["order_cost"]
    delivery_charge = trolley_items_context["delivery_charge"]
    total_cost = trolley_items_context["total_cost"]

    # Payment intent
    total_cost_money = int(total_cost * 100)
    intent = stripe.PaymentIntent.create(
        amount=total_cost_money,
        currency="gbp",
    )

    # Order form available in view
    order_form = OrderForm()

    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": "intent.client_secret",
        "order_cost": order_cost,
        "delivery_charge": delivery_charge,
        "total_cost": total_cost,
    }
    template = "checkout/checkout.html"

    return render(request, template, context)
