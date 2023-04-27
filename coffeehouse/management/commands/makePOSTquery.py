import requests
from django.core.management import BaseCommand

#  Make TOKEN authentication
"""class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        print(requests.post('http://localhost:8000/api/token/', json={"username":"", "password":""}))"""


#  Make POST api/login/ 
"""class Command(BaseCommand):
    def handle(self, *args, **options):
        print(requests.post('http://127.0.0.1:8000/api/login/', json={"username":"root", "password":"Volia2003"}))"""


#  Make POST api/register/ 
"""class Command(BaseCommand):
    def handle(self, *args, **options):
        print(requests.post('http://localhost:8000/api/register/', json={"username":"testuser", "password":"Volia2003"}))"""


#  Make POST api/logout/ 
"""class Command(BaseCommand):
    def handle(self, *args, **options):
        print(requests.post('http://localhost:8000/api/logout/'))"""


#  Make POST Order Creation
class Command(BaseCommand):
    def handle(self, *args, **options):
        print(requests.post('http://127.0.0.1:8000/api/order/', json={
        "id": 6,
        "date_time": "2023-04-26T21:42:00Z",
        "coffee_shop": 1,
        "status": "Active"
    }))