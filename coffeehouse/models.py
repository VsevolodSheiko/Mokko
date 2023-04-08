# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.db import models


# Create your models here.
class CoffeeShop(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    city = models.CharField(max_length=50)
    description = models.TextField()
    
    class Meta:
        db_table = "coffeeshop"
        verbose_name = "coffeeshop"
        verbose_name_plural = "coffeeshops"


class Visitor(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    date_joined = models.DateField()

    class Meta:
        db_table = "visitor"
        verbose_name = "visitor"
        verbose_name_plural = "visitors"


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "categories"


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, null=False)
    price = models.FloatField(default=0.00, null=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()

    class Meta:
        db_table = "product"
        verbose_name = "product"
        verbose_name_plural = "products"


class Ingredient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    price_per_unit = models.FloatField(default=0.00)

    class Meta:
        db_table = "ingredient"
        verbose_name = "ingredient"
        verbose_name_plural = "ingredients"


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField()
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=15)

    class Meta:
        db_table = "order"
        verbose_name = "order"
        verbose_name_plural = "orders"


class OrderItem(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    unit_price = models.ManyToManyField(to=Product, related_name="products")

    class Meta:
        db_table = "orderitem"
        verbose_name = "orderitem"
        verbose_name_plural = "orderitems"


class FreeTable(models.Model):
    id = models.IntegerField(primary_key=True)
    seats = models.IntegerField()
    is_available = models.BooleanField()

    class Meta:
        db_table = "freetable"
        verbose_name = "freetable"
        verbose_name_plural = "freetables"


class Promotion(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    discount = models.IntegerField()
    product_type = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "promotion"
        verbose_name = "promotion"
        verbose_name_plural = "promotions"


class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    visitor = models.ForeignKey(Visitor, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    context = models.TextField()

    class Meta:
        db_table = "review"
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
        