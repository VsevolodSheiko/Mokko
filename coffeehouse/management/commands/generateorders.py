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
            freetable = FreeTable.objects.get(id=random.randint(1, 100))
            Order.objects.create(id=i, date_time=datetime.now(), status=random.choice(["In progress", "Ready"]), table_id=(freetable.id))