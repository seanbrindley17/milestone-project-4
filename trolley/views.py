from django.shortcuts import render, redirect

# Create your views here.


def show_trolley(request):

    return render(request, "trolley/trolley.html")


# View for a user to add a product to their trolley, tracked using the item_id
def add_to_trolley(request, item_id):

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

    # If there's already an item_id key matching a key in the trolley dictionary
    if item_id in list(trolley.keys()):
        # Then the quantity is incremented accordingly
        trolley[item_id] += quantity
    else:
        # Otherwise set the item_id key to match the quantity of the product added
        trolley[item_id] = quantity

    # Overwrite the previous Trolley with updated trolley session
    request.session["trolley"] = trolley
    print(request.session["trolley"])
    return redirect(return_url)
