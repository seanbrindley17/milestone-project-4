from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("add_product/", views.add_product, name="add_product"),
    path("edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("delete/<int:product_id>/",
         views.delete_product,
         name="delete_product"),
    path("newsletter/", views.newsletter, name="newsletter"),
]
