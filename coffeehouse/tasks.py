import os

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT")


def send_tetelgram_message():
    url = 'https://api.telegram.org/bot%s/getMe', TELEGRAM_BOT_TOKEN
    


def order_creation(instance):
