from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_trolley, name="show_trolley"),
    path("add_product/<item_id>", views.add_to_trolley, name="add_to_trolley"),
    path("remove/<item_id>", views.remove_item, name="remove_item")
]
