from django.db import models
from .coffeeshop import CoffeeShop
from .freetable import FreeTable


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15)
    table = models.ForeignKey(FreeTable, on_delete=models.DO_NOTHING)


    class Meta:
        db_table = "order"
        verbose_name = "order"
        verbose_name_plural = "orders"
    
