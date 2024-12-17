from django.urls import path
from . import views

urlpatterns = [path("", views.show_trolley, name="show_trolley")]
