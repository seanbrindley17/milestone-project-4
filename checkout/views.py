import stripe
import json
from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from home.models import Product
from trolley.contexts import trolley_items
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from .models import Order, OrderItem
from .forms import OrderForm


# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:
        # Gets payment intent id by splitting client secret and taking the first element in that new array
        pid = request.POST.get("client_secret").split("_secret")[0]
        # set up stripe with secret key to be able to modify payment intent
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Modify by calling the "pid" variable and tell it which data to modify
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "trolley": json.dumps(request.session.get("trolley", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Payment cannot be proccessed. Try again later")
        # return 400 for a bad request
        return HttpResponse(content=e, status=400)


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
            order = order_form.save(commit=False)
            # Get payment intent by splitting at the secret
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_trolley = json.dumps(trolley)
            order.save()
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
                    # # Non working code for shoe sizes
                    # # Keeping because I will fix after this has been marked
                    # elif isinstance(item_data["items_by_shoesize"]):
                    #     for shoesize, quantity in item_data[
                    #         "items_by_shoesize"
                    #     ].items():
                    #         order_item = OrderItem(
                    #             order=order,
                    #             product=product,
                    #             quantity=quantity,
                    #             product_size=shoesize,
                    #         )
                    #         order_item.save()
                    else:
                        for size, quantity in item_data["items_by_size"].items():
                            order_item = OrderItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                regular_size=size,
                            )
                            order_item.save()
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

    # Prefills fields for authenticated users
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(
                initial={
                    "name": profile.name,
                    "surname": profile.surname,
                    "email": profile.email,
                    "phone_number": profile.phone_number,
                    "town_or_city": profile.town_or_city,
                    "street_address_one": profile.address_line_one,
                    "street_address_two": profile.address_line_two,
                    "postcode": profile.postcode,
                    "county": profile.county,
                }
            )
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
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

    if request.user.is_authenticated:
        # Gets user's profile and sets the order to it and saves. Allows retrieval
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                "name": order.name,
                "surname": order.surname,
                "phone_number": order.phone_number,
                "postcode": order.postcode,
                "town_or_city": order.town_or_city,
                "address_line_one": order.address_line_one,
                "address_line_two": order.address_line_two,
                "county": order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

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
