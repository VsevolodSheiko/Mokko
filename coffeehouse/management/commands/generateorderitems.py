from faker import Faker
from django.core.management import BaseCommand
from coffeehouse.models.order import Order
from coffeehouse.models.orderitem import OrderItem
from coffeehouse.models.product import Product
import random
fake = Faker('uk')

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1, 40):
            product = Product.objects.get(id=random.randint(1, 28)) 
            order = Order.objects.get(id=random.randint(1, 150)) 
            OrderItem.objects.create(id=i, quantity=random.randint(1, 4), item=product, order=order)