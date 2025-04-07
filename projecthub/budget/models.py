from django.db import models
from django.core.validators import MinValueValidator


class Budget(models.Model):
    CATEGORIES = [
        ('IN', 'Inkomen'),
        ('FLEX', 'Flexibele lasten'),
        ('VAST', 'Vaste lasten'),
    ]

    name = models.CharField(max_length=50, unique=True)
    budget = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.CharField(max_length=4, choices=CATEGORIES)
    active = models.BooleanField(default=True)
