from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings

from home.models import Product


# Context to allow the Trolley to be accessed by any app in the project
def trolley_items(request):

    items_in_trolley = []
    product_count = 0
    order_cost = 0
    delivery_charge = 0
    total_cost = 0
    trolley = request.session.get("trolley", {})

    # Iterates through the products in the trolley dictionary using .items()
    # This was confusing me intially
    for item_id, item_data in trolley.items():
        # If item_data is just an integer then there's no sizings involved
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            # increments the product_count by the quantity added to the bag
            product_count += item_data
            # Calculates the total cost of the added item,
            # multiply the quantity by the price
            order_cost += item_data * product.price
            if order_cost > 0:
                delivery_charge = order_cost * Decimal(
                    settings.DELIVERY_PERCENTAGE / 100
                )
                total_cost = order_cost + delivery_charge
                items_in_trolley.append(
                    {
                        "item_id": item_id,
                        "product": product,
                        "quantity": item_data,
                    }
                )
        else:
            # iterates through items that have a traditional size
            product = get_object_or_404(Product, pk=item_id)
            # Uses items_by_size to iterate the price and quantity accordingly
            for size, quantity in item_data["items_by_size"].items():
                order_cost += quantity * product.price
                if order_cost > 0:
                    delivery_charge = order_cost * Decimal(
                        settings.DELIVERY_PERCENTAGE / 100
                    )
                    total_cost = order_cost + delivery_charge
                    items_in_trolley.append(
                        {
                            "item_id": item_id,
                            "quantity": quantity,
                            "product": product,
                            "size": size,
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
