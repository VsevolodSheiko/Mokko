from celery import shared_task
from .models.order import Order
from coffeehouse import google_sheets_api


@shared_task()
def add_new_visitors_to_google_sheets():
    print("Started")
    google_sheets_api.write()


@shared_task()
def clear_unactive_orders():
    values = Order.objects.filter(status="Ready").delete()
