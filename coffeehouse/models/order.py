from django.db import models
from .coffeeshop import CoffeeShop


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField()
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=15)

    class Meta:
        db_table = "order"
        verbose_name = "order"
        verbose_name_plural = "orders"
    
