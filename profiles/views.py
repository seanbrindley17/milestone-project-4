from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

# Create your views here.


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    # if statement for handling form post requests
    if request.method == "POST":
        # Create new instance of form using the posted data, updating profile got above
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {"form": form, "orders": orders, "on_profile_page": True}

    return render(request, template, context)


# View to retrieve past orders and display to user
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (f"This is a previous order, Order number: {order_number}"))

    template = "checkout/checkout_success.html"
    context = {"order": order, "from_profile": True}

    return render(request, template, context)
