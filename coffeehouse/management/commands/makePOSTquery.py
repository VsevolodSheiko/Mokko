import requests
from django.core.management import BaseCommand

#  Make TOKEN authentication
"""class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        print(requests.post('http://localhost:8000/api/token/', data={"username":"", "password":""}))"""


#  Make POST api/login/ 
"""class Command(BaseCommand):
    def handle(self, *args, **options):
        print(requests.post('http://localhost:8000/api/login/', data={"username":"root", "password":"Volia2003"}))"""


#  Make POST api/register/ 
"""class Command(BaseCommand):
    def handle(self, *args, **options):
        print(requests.post('http://localhost:8000/api/register/', data={"username":"testuser", "password":"Volia2003"}))"""


#  Make POST api/logout/ 
"""class Command(BaseCommand):
    def handle(self, *args, **options):
        print(requests.post('http://localhost:8000/api/logout/'))"""