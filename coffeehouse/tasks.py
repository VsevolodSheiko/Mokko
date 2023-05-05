from celery import shared_task
from django.contrib.admin.models import LogEntry
from coffeehouse import google_sheets_api


@shared_task()
def add_new_visitors_to_google_sheets():
    print("Started google_sheets_api")
    google_sheets_api.write()


@shared_task()
def clear_unactive_orders():
    print("Started logins to site")
    logs = LogEntry.objects.all()
    for log in logs:
        print(log.user)

