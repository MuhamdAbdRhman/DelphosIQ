"""Loan serializer"""

from rest_framework import serializers

from loans.models import Loan
from loans.serializers import CountrySerializer, SectorSerializer


class LoanSerializer(serializers.ModelSerializer):
    """Loan Serializer"""
    country = CountrySerializer()
    sector = SectorSerializer()

    class Meta:
        model = Loan
        fields = '__all__'
