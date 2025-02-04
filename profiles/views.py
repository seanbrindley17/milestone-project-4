from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    # if statement for handling form post requests
    if request.method == "POST":
        # Create new instance of form using the posted data, updating profile got above
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Something went wrong. Try again")

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {"form": form, "orders": orders, "on_profile_page": True}

    return render(request, template, context)


# View to retrieve past orders and display to user
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    if not order:
        messages.error(request, "Order cannot be found.")
        return redirect("profile")

    messages.info(request, (f"This is a previous order, Order number: {order_number}"))

    template = "checkout/checkout_success.html"
    context = {"order": order, "from_profile": True}

    return render(request, template, context)
