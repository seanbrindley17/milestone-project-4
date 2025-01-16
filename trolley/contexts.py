from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings

from home.models import Product


# Context to allow the Trolley to be accessed by any app in the project
def trolley_items(request):

    items_in_trolley = []
    product_count = 0
    order_cost = 0
    trolley = request.session.get("trolley", {})

    # Iterates through the products in the trolley dictionary using the .items() method. This was confusing me intially
    for item_id, quantity in trolley.items():
        product = get_object_or_404(Product, pk=item_id)
        # increments the product_count by the quantity added to the bag
        product_count += quantity
        # Calculates the total cost of the added item, multiply the quantity by the price. Simple stuff really
        order_cost += quantity * product.price
        delivery_charge = order_cost * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        total_cost = order_cost + delivery_charge

        items_in_trolley.append(
            {
                "product": product,
                "quantity": quantity,
            }
        )

    context = {
        "items_in_trolley": items_in_trolley,
        "product_count": product_count,
        "order_cost": order_cost,
        "delivery_charge": delivery_charge,
        "total_cost": total_cost,
    }

    return context
