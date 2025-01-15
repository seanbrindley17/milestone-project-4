from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<int:product_id>", views.product_detail, name="product_detail"),
]
