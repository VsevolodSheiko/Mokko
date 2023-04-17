from django.db import models


class FreeTable(models.Model):
    id = models.IntegerField(primary_key=True)
    seats = models.IntegerField()
    is_available = models.BooleanField()

    class Meta:
        db_table = "freetable"
        verbose_name = "freetable"
        verbose_name_plural = "freetables"