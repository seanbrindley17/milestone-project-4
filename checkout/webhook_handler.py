import stripe
import json
import time
from django.http import HttpResponse
from profiles.models import UserProfile
from home.models import Product
from .models import Order, OrderItem


# from profiles.models import UserProfile


class stripe_webhook_handler:
    # init method called every time instance of class is created
    def __init__(self, request):
        self.request = request

    # handle event returns a http response when event of unhandled webhook is received
    def handle_event(self, event):

        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}", status=200
        )

    # handles payment_intent.succeeded webhook
    def handle_payment_intent_succeeded(self, event):

        intent = event.data.object
        pid = intent.id
        trolley = intent.metadata.trolley
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        total_cost = round(stripe_charge.amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Allows webhook to handle user profile info
        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
            # Only happens if user has checked save info box
            if save_info:
                profile.phone_number = shipping_details.phone
                profile.postcode = shipping_details.address.postal_code
                profile.town_or_city = shipping_details.address.city
                profile.street_address1 = shipping_details.address.line1
                profile.street_address2 = shipping_details.address.line2
                profile.county = shipping_details.address.state
                profile.save()
        # Assumes order doesn't exist
        order_exists = False
        attempt = 1
        # While loop attempts to find the order 5 times
        while attempt <= 5:
            # Retrieve order from payment intent
            # __iexact looks for an exact match but is case insensitive
            try:
                order = Order.objects.get(
                    user_profile=profile,
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    total_cost=total_cost,
                    original_trolley=trolley,
                    stripe_pid=pid,
                )
                # if order is found set order exists to true
                order_exists = True
                break

            # If order doesn't exist, create it
            except Order.DoesNotExist:
                attempt += 1
                # After each attempt, wait for one second before trying again
                time.sleep(1)
        # Will display webhook if order exists now
        if order_exists:
            return HttpResponse(
                content=f"Webhook received: {event["type"]} | Order already in database. ",
                status=200,
            )
        # Otherwise, this is where the order is created by the webhook
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    total_cost=total_cost,
                    original_trolley=trolley,
                    stripe_pid=pid,
                )
                # Same code as from the view except loading from json intent
                for item_id, item_data in json.loads(trolley).items():
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
                            order_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f"Webhook received {event["type"]} | Error: {e}",
                    status=500,
                )

            return HttpResponse(
                content=f"Webhook received: {event["type"]} | Created order in webhook",
                status=200,
            )

    # handles payment_intent.payment_failed webhook
    def handle_payment_intent_payment_failed(self, event):

        return HttpResponse(content=f"Webhook received: {event['type']}", status=200)
