from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem


# Receiving signals from OrderItem model to update post_save
@receiver(post_save, sender=OrderItem)
# Will update order cost when item is updated or created
def update_on_save(sender, instance, created, **kwargs):
    # Update total of instance of order referred to
    instance.order.update_total_cost()


# Updates order cost upon item delete
@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):

    instance.order.update_total_cost()
