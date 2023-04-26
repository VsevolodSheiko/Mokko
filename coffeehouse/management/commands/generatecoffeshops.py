from faker import Faker
from django.core.management import BaseCommand
from coffeehouse.models.coffeeshop import CoffeeShop

fake = Faker('uk')

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1, 51):
            address = fake.street_address()

            # Generate a fake city
            city = fake.city()

            # Generate a fake phone number
            phone = fake.phone_number()

            # Generate a fake description
            description = fake.text()
            CoffeeShop.objects.create(id=i, address=address, city=city, phone=phone, description=description)
