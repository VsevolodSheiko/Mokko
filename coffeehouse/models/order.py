import os
from django.db import models
from .freetable import FreeTable
from django.db.models.signals import post_save
from django.dispatch import receiver
from celery import shared_task
import requests

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT")
TELEGRAM_MY_ID = os.environ.get("TELEGRAM_MY_ID")


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15)
    table = models.ForeignKey(FreeTable, on_delete=models.DO_NOTHING, related_name='orders')
    
    class Meta:
        db_table = "order"
        verbose_name = "order"
        verbose_name_plural = "orders"
    
    def __str__(self):
        return self.id


@receiver(post_save, sender=Order)
def celery_on_order_creation(sender, instance, created, **kwargs):
    if created:
        on_order_creation.delay(instance.id)


@shared_task()
def on_order_creation(order_id):
    order = Order.objects.get(id=order_id)
    coffeeshop = order.table.coffeeshop
    text = f"Order {order.id} {order.status} {order.date_time} in Coffeeshop with address: {coffeeshop.city}, {coffeeshop.address}."

    print("Sending telegram message...")
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage' 

    body = {
        "chat_id": TELEGRAM_MY_ID,
        "text": text,
    }
    requests.post(url, json=body)







