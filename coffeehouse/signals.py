from django.db.models.signals import post_save
from django.dispatch import receiver
from coffeehouse.models.order import Order
from .tasks import on_order_creation

@receiver(post_save, sender=Order)
def celery_on_order_creation(sender, instance, created, **kwargs):
    if created:
        on_order_creation.delay()



