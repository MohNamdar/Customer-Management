from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Order


@receiver(pre_save, sender=Order)
def customer_order_counter(sender, instance, **kwargs):
    # Check if buyer exists before modifying it
    if instance.buyer:
        # Update the visit count for the customer
        instance.buyer.visit_count = instance.buyer.visit_count + 1  # Increment visit count
        instance.buyer.save()  # Save the customer instance


@receiver(post_save, sender=Order)
def customer_kind_granter(sender, instance, **kwargs):
    if 3 < instance.buyer.visit_count < 6:
        instance.buyer.kind = instance.buyer.CustomerKind.KNOWN
    elif instance.buyer.visit_count > 6:
        instance.buyer.kind = instance.buyer.CustomerKind.LOYAL
    instance.buyer.save()
