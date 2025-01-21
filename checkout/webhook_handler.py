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
        print(intent)
        return HttpResponse(content=f"Webhook received: {event['type']}", status=200)

    # handles payment_intent.payment_failed webhook
    def handle_payment_intent_payment_failed(self, event):

        return HttpResponse(content=f"Webhook received: {event['type']}", status=200)
