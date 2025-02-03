import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from home.models import Product
from profiles.models import UserProfile


# Create your models here.
# Model for collating a user's order
class Order(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    order_number = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    surname = models.CharField(max_length=35, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    town_or_city = models.CharField(max_length=30, null=True, blank=True)
    address_line_one = models.CharField(max_length=50, null=True, blank=True)
    address_line_two = models.CharField(max_length=50, null=True, blank=True)
    county = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    total_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    original_trolley = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default="")

    # Will generate a random 32 character string to be used as an order number
    def _generate_order_number(self):

        return uuid.uuid4().hex.upper()

    # Sets the order number, if not already set, by overriding the save method
    def save(self, *args, **kwargs):

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    # Updates the total cost by aggregating the sum of the items
    def update_total_cost(self):

        self.order_cost = (
            self.items.aggregate(Sum("item_total_cost"))["item_total_cost__sum"] or 0
        )
        self.delivery_cost = self.order_cost * settings.DELIVERY_PERCENTAGE / 100
        self.total_cost = self.order_cost + self.delivery_cost
        self.save()

    def __str__(self):
        return self.order_number


# Model for the individual items being ordered
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    regular_size = models.CharField(max_length=20, null=True, blank=True)
    fin_size = models.CharField(max_length=4, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    item_total_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    # Overwrites save method to update the item_total_cost field
    def save(self, *args, **kwargs):

        self.item_total_cost = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SKU {self.product.sku} on order {self.order.order_number}"
