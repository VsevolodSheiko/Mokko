from django.db import models

from .coffeeshop import CoffeeShop


class FreeTable(models.Model):
    id = models.IntegerField(primary_key=True)
    seats = models.IntegerField()
    is_available = models.BooleanField()
    coffeeshop = models.ForeignKey(CoffeeShop, on_delete=models.DO_NOTHING, related_name='tables')

    class Meta:
        db_table = "freetable"
        verbose_name = "freetable"
        verbose_name_plural = "freetables"
    
    def __str__(self):
        return self.id