from django.db import models
from .product import Product
from .order import Order


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