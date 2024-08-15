
from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name