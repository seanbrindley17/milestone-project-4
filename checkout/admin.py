from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ("item_total_cost",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "delivery_cost",
        "order_cost",
        "total_cost",
        "original_trolley",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "name",
        "surname",
        "email",
        "phone_number",
        "postcode",
        "town_or_city",
        "address_line_one",
        "address_line_two",
        "county",
        "date",
        "delivery_cost",
        "order_cost",
        "total_cost",
        "original_bag",
        "stripe_pid",
    )

    list_display = (
        "order_number",
        "date",
        "name",
        "surname",
        "delivery_cost",
        "order_cost",
        "total_cost",
    )

    # Ordered by "date", most recent first
    ordering = ("-date",)


# OrderItemAdminInline doesn't need to be registered as it is accessible via OrderAdmin
admin.site.register(Order, OrderAdmin)
