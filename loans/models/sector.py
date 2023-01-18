"""Sector Model"""

from django.db import models


class Sector(models.Model):
    """Sector Model"""
    name = models.CharField(
        max_length=300,
        unique=True,
    )

    def __str__(self):
        return self.name
