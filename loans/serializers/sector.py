"""Sector serializer"""

from rest_framework import serializers

from ..models import Sector


class SectorSerializer(serializers.ModelSerializer):
    """Sector Serializer"""

    class Meta:
        model = Sector
        fields = '__all__'
