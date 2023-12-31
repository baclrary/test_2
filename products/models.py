from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    count = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
