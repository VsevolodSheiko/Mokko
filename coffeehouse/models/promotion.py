from django.db import models
from .product import Product


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
    
    def __str__(self):
        return self.id