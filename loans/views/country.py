"""Country View"""

from rest_framework import views
from rest_framework.response import Response

from ..models import Country
from ..serializers import CountrySerializer


class CountryView(views.APIView):
    """Country View"""

    serializer_class = CountrySerializer

    def get(self, request):
        """handle get request"""
        countries = Country.objects.all()
        serializer = self.serializer_class(countries, many=True)
        return Response(serializer.data)
