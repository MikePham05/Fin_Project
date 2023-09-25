from django.db import models

# Create your models here. models are databases schema

class StockInfo(models.Model):
    name = models.TextField(max_length=20)
    date = models.DateTimeField();
    open = models.FloatField();
    high = models.FloatField();
    low = models.FloatField();
    close = models.FloatField();

    def __str__(self):
        return self.name




