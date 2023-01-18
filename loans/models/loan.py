"""Loan Model"""

from django.db import models


class Loan(models.Model):
    """Loan Model"""
    title = models.CharField(
        max_length=300,
    )
    signature_date = models.DateField()
    country = models.ForeignKey(
        to="loans.Country",
        on_delete=models.CASCADE,
    )
    sector = models.ForeignKey(
        to="loans.Sector",
        on_delete=models.CASCADE,
    )
    signed_amount = models.FloatField()

    def __str__(self):
        return self.title
