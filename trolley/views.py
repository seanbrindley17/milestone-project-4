from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from home.models import Product

# Create your views here.


def show_trolley(request):

    return render(request, "trolley/trolley.html")


# View for a user to add a product to their trolley, tracked using the item_id
def add_to_trolley(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    return_url = request.POST.get("return-url")
    quantity = int(request.POST.get("product-quantity"))

    size = None
    if "product_size" in request.POST:
        size = request.POST["product-size"]

    shoesize = None
    if "shoe_size" in request.POST:
        shoesize = request.POST["shoe-size"]

    personalisation = None
    if "product_personalisation_input" in request.POST:
        personalisation = request.POST["product-personalisation-input"]

    # Access session to check if trolley variable exists, if not initialise empty dictionary
    trolley = request.session.get("trolley", {})

    # If the item has a tradional sizing
    if size:
        # Check if the item is in the trolley by looking to see if the item id matches a key in a key value pair in the trolley
        if item_id in list(trolley.keys()):
            # If there's already an item with the size that is being added, then increment quantity of item and size
            if size in trolley[item_id]["items_by_size"].keys():
                trolley[item_id]["items_by_size"][size] += quantity
            else:
                # If this is a new size of an existing item being added, set the quantity to the value of the quantity added
                trolley[item_id]["items_by_size"][size] = quantity
        else:
            # It item wasn't in trolley, add to dictionary items_by_size to track by size items with same ID
            trolley[item_id] = {"items_by_size": {size: quantity}}

    # If there's already an item_id key matching a key in the trolley dictionary
    if item_id in list(trolley.keys()):
        # Then the quantity is incremented accordingly
        trolley[item_id] += quantity
    else:
        # Otherwise set the item_id key to match the quantity of the product added
        trolley[item_id] = quantity
        messages.success(request, f"Added { product.name } to trolley")

    # Overwrite the previous Trolley with updated trolley session
    request.session["trolley"] = trolley
    print(request.session["trolley"])
    return redirect(return_url)


# View for the user to be able to remove items from their trolley
def remove_item(request, item_id):

    # Get the current trolley items
    trolley = request.session.get("trolley", {})

    # Check the item id is in the trolley
    if item_id in trolley:
        # delete item_id from trolley
        del trolley[item_id]

    # As in the add_to_trolley above, overwrite with updated trolley
    request.session["trolley"] = trolley

    return redirect("show_trolley")
