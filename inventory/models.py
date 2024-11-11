# inventory/models.py
from django.db import models

class InventoryItem(models.Model):
    CATEGORY_CHOICES = [
        ('Dairy', 'Dairy Items'),
        ('Meat', 'Meat'),
        ('Fruits', 'Fruits'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    barcode = models.CharField(max_length=50, unique=True, blank=True, null=True)  # Barcode field

    def __str__(self):
        return self.name
