import stripe
from django.http import HttpResponse


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

        return HttpResponse(content=f"Webhook received: {event['type']}", status=200)

    # handles payment_intent.payment_failed webhook
    def handle_payment_intent_payment_failed(self, event):

        return HttpResponse(content=f"Webhook received: {event['type']}", status=200)
