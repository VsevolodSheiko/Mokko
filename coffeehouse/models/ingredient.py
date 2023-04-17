from django.db import models


class Ingredient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    price_per_unit = models.FloatField(default=0.00)

    class Meta:
        db_table = "ingredient"
        verbose_name = "ingredient"
        verbose_name_plural = "ingredients"
