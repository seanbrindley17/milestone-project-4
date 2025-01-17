from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_checkout, name="view_checkout"),
    path("checkout/<order_number>", views.checkout_success, name="checkout_success"),
]
