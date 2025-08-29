from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,\
                                null=True, blank=True)
    quality = models.CharField(null=True, blank=True)
    instock = models.BooleanField(default=True)

    def __str__(self):
        return self.title