from faker import Faker
from django.core.management import BaseCommand
from coffeehouse.models.freetable import FreeTable
from coffeehouse.models.order import Order
import random
from datetime import datetime
fake = Faker('uk')

class Command(BaseCommand):
    def handle(self, *args, **options):
        result = Order.objects.filter(status="Ready")[:10]
        for i in result:
            print(i.id, i.status)