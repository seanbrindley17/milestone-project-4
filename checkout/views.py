from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.


# View for the checkout
def view_checkout(request):

    trolley = request.session.get("trolley", {})
    # If nothing is in the trolley dictionary
    if not trolley:
        # Display error message
        messages.error(request, "No items in trolley")
        # Return user to home page to prevent access by inputting the checkout url
        return redirect(reverse("home"))

    order_form = OrderForm()
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51QhxeeJIWLpCU8q8Mf6QMfrNuhh8EE0b0PVHDxLE4FRhFpECs9p8DiI2Lkjftaty1jWXHcYx0ZMJRfPA6aucMgJs00fjUMHKTH",
        "client_secret": "test client secret",
    }
    template = "checkout/checkout.html"

    return render(request, template, context)
