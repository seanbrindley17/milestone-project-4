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
    context = {"order_form": order_form}
    template = "checkout/checkout.html"

    return render(request, template, context)
