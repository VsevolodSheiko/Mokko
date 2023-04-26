import os
from celery import shared_task

from coffeehouse.models.order import Order, CoffeeShop


TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT")


def send_telegram_message(text):
    url = 'https://api.telegram.org/bot%s/sendMessage', TELEGRAM_BOT_TOKEN

    body = {
        "chat_id": TELEGRAM_USER_ID,
        "text": text,
    }
    response = requests.post(url, json=body)

    response.raise_for_status()


@shared_task
def on_order_creation(order_id):
    order = Order.objects.get(id=order_id)
    coffeshop = CoffeeShop.objects.get(id=order.coffee_shop)
    text = f"Online Order {order.id} {order.status} {order.date_time} in Coffeshop with address: {coffeshop.city}, {coffeshop.address}."

    print("Sending telegram message...")
    send_telegram_message(text)
