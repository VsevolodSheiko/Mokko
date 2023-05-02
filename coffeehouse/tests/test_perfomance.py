import time
from django.test import TestCase
from coffeehouse.models.coffeeshop import CoffeeShop

class CoffeeShopPerformanceTest(TestCase):
    def setUp(self):
        # Create 1000 coffee shop objects for testing
        start_time = time.time()
        for i in range(1000):
            CoffeeShop.objects.create(
                id=i,
                address=f"Address {i}",
                phone=f"123-456-{i:03}",
                city="Test City",
                description="Test description"
            )
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds for creating database")

    def test_list_coffee_shops_performance(self):
        start_time = time.time()
        response = self.client.get('/api/coffeeshop/')
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
        self.assertLessEqual(elapsed_time, 1.0)
