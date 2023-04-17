from django.db import models
from .product import Product
from .visitor import Visitor


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