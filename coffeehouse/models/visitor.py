from django.db import models


class Visitor(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    class Meta:
        db_table = "visitor"
        verbose_name = "visitor"
        verbose_name_plural = "visitors"