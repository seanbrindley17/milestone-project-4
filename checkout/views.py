import stripe
from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from home.models import Product
from trolley.contexts import trolley_items
from .models import Order, OrderItem
from .forms import OrderForm


# Create your views here.


# View for the checkout
def view_checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # If form is being posted
    if request.method == "POST":
        trolley = request.session.get("trolley", {})

        # Save form data in variable form_data
        form_data = {
            "name": request.POST["name"],
            "surname": request.POST["surname"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "town_or_city": request.POST["town_or_city"],
            "address_line_one": request.POST["address_line_one"],
            "address_line_two": request.POST["address_line_two"],
            "county": request.POST["county"],
            "postcode": request.POST["postcode"],
        }
        # Passes form_data above to the OrderForm in forms.py and save as order_form
        order_form = OrderForm(form_data)
        # Will save the order form if it's valid
        if order_form.is_valid():
            order = order_form.save()
            # Loop through items in trolley
            for item_id, item_data in trolley.items():
                try:
                    # Get the item id to determine whether it has sizes, shoesizes or not
                    product = Product.objects.get(id=item_id)
                    # if item_data is an integer, it doesn't have a size
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_item.save()
                    elif isinstance(item_data["items_by_size"]):
                        for size, quantity in item_data["items_by_size"].items():
                            order_item = OrderItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_item.save()
                    else:
                        for shoesize, quantity in item_data[
                            "items_by_shoesize"
                        ].items():
                            order_item = OrderItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=shoesize,
                            )
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        ("A product in the trolley was not found in the the database"),
                    )
                    order.delete()
                    return redirect(reverse("show_trolley"))

            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse("checkout_success", args=[order.order_number]))
        else:
            messages.error(
                request,
                "There was an error with your form. \
                Please double check your information.",
            )

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

    # sets api key to secret key
    stripe.api_key = stripe_secret_key

    # Payment intent
    total_cost_money = int(total_cost * 100)
    try:
        intent = stripe.PaymentIntent.create(
            amount=total_cost_money,
            currency="gbp",
        )
        print(intent)
    except stripe.error.StripeError as e:
        messages.error(request, f"Stripe Error: {e}")
        return redirect(reverse("show_trolley"))

    if not stripe_public_key:
        messages.warning(request, "Stripe Public Key is missing!")

    # Order form available in view
    order_form = OrderForm()

    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
        "order_cost": order_cost,
        "delivery_charge": delivery_charge,
        "total_cost": total_cost,
    }
    template = "checkout/checkout.html"

    return render(request, template, context)


# View for a successful checkout proceedure
def checkout_success(request, order_number):

    # Check if user wants to save info
    save_info = request.session.get("save_info")
    # Gets the order using the order number in the Order model
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(
        request,
        f"Order placed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.",
    )

    # Deletes user's trolley from session as if successful order they won't need it
    if "trolley" in request.session:
        del request.session["trolley"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
