from faker import Faker
from django.core.management import BaseCommand
from coffeehouse.models.visitor import Visitor

fake = Faker('uk')

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1, 701):
            # Generate a fake first name and last name
            first_name = fake.first_name()
            last_name = fake.last_name()

            # Generate a fake email
            email = fake.email()

            # Generate a fake date joined
            date_joined = fake.date_between(start_date='-10y', end_date='today')
            Visitor.objects.create(id=i, first_name=first_name, last_name=last_name, email=email, date_joined=date_joined)
