from faker import Faker
from django.core.management import BaseCommand
from coffeehouse.models.freetable import FreeTable
from coffeehouse.models.coffeeshop import CoffeeShop
import random
fake = Faker('uk')

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1, 100):
            FreeTable.objects.create(id=i, seats=random.randint(2, 15), is_available=random.randint(0, 1), coffeeshop=(CoffeeShop.objects.get(id=random.randint(1,10))))