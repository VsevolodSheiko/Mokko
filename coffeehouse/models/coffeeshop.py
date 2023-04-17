from django.db import models

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


