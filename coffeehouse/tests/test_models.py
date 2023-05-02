from django.test import TestCase
from coffeehouse.models.category import Category
from coffeehouse.models.coffeeshop import CoffeeShop
from coffeehouse.models.order import Order
from coffeehouse.models.freetable import FreeTable

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            id=1,
            name='Test Category',
            description='This is a test category.'
        )

    def test_category_fields(self):
        """Test that the Category model fields are properly defined"""
        self.assertEqual(self.category.id, 1)
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.description, 'This is a test category.')

    def test_category_str(self):
        """Test that the __str__ method of the Category model returns the correct value"""
        self.assertEqual(str(self.category), 'Test Category')


class CoffeeShopModelTest(TestCase):
    def setUp(self):
        self.coffee_shop = CoffeeShop.objects.create(
            id=1,
            address='123 Main St',
            phone='555-555-5555',
            city='New York',
            description='This is a test coffee shop.'
        )

    def test_coffee_shop_fields(self):
        """Test that the CoffeeShop model fields are properly defined"""
        self.assertEqual(self.coffee_shop.id, 1)
        self.assertEqual(self.coffee_shop.address, '123 Main St')
        self.assertEqual(self.coffee_shop.phone, '555-555-5555')
        self.assertEqual(self.coffee_shop.city, 'New York')
        self.assertEqual(self.coffee_shop.description, 'This is a test coffee shop.')

    def test_coffee_shop_str(self):
        """Test that the __str__ method of the CoffeeShop model returns the correct value"""
        self.assertEqual(str(self.coffee_shop), '123 Main St')


class OrderModelTest(TestCase):
    def setUp(self):
        self.coffeeshop = CoffeeShop.objects.create(id=1, address='test add', phone='23432', city='Kyiv', description='test description')
        self.table = FreeTable.objects.create(coffeeshop=self.coffeeshop, id=1, is_available=1, seats=10)
        self.order = Order.objects.create(id=1, status='Pending', table=self.table)

    def test_order_fields(self):
        """Test that the Order model fields are properly defined"""
        self.assertEqual(self.order.id, 1)
        self.assertEqual(self.order.status, 'Pending')
        self.assertEqual(self.order.table, self.table)

    def test_order_str(self):
        """Test that the __str__ method of the Order model returns the correct value"""
        self.assertEqual(self.order.id, 1)