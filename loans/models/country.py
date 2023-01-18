"""Country Model"""

from django.db import models


class Country(models.Model):
    """Country Model"""
    name = models.CharField(
        max_length=300,
        unique=True,
    )

    def __str__(self):
        return self.name
