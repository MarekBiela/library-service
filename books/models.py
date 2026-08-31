from django.db import models
from enum import Enum


class Cover(Enum):
    HARD = "hard"
    SOFT = "soft"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover = models.CharField(
        max_length=20,
        choices=[(cover.value, cover.name) for cover in Cover],
    )
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} - {self.author}"
