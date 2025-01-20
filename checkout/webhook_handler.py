from django.http import HttpResponse


class stripe_webhook_handler:
    # init method called every time instance of class is created
    def __init__(self, request):
        self.request = request

    # handle event returns a http response when event of webhook is received
    def handle_event(self, event):

        return HttpResponse(content=f"Webhook received: {event['type']}", status=200)
