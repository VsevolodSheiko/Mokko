from faker import Faker
from django.core.management import BaseCommand
from coffeehouse.models.freetable import FreeTable
from coffeehouse.models.order import Order
import random
from datetime import datetime
fake = Faker('uk')

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1, 13096):
            FreeTable.objects.create(id=i, date_time=datetime.now(), coffeeshop=(CoffeeShop.objects.get(id=random.randint(1, 50))))