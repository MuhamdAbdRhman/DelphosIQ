"""Country serializer"""

from rest_framework import serializers

from ..models import Country


class CountrySerializer(serializers.ModelSerializer):
    """Country Serializer"""

    class Meta:
        model = Country
        fields = '__all__'
