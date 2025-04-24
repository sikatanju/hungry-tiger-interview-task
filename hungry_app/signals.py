from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import Customer, Vendor


User = get_user_model()

@receiver(post_save, sender=User)
def create_customer_or_vendor_for_new_user(sender, instance, created, **kwargs):
    if created:
        if instance.is_vendor:
            Vendor.objects.create(user=instance)
        elif instance.is_customer:
                Customer.objects.create(user=instance)