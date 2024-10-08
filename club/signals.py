from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Customer


@receiver(pre_save, sender=Customer)
def edite_name(sender, instance, **kwargs):
    if Customer.objects.all().last():
        last_id = Customer.objects.last().id
    else:
        last_id = 0
    if not instance.first_name:
        instance.first_name = f'مشتری {last_id + 1}'
