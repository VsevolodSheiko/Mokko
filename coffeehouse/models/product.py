from django.db import models
from .category import Category


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
    
    def __str__(self):
        return self.name