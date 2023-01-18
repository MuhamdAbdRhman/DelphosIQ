"""Sector View"""

from rest_framework import views
from rest_framework.response import Response

from ..models import Sector
from ..serializers import SectorSerializer


class SectorView(views.APIView):
    """Sector View"""

    serializer_class = SectorSerializer

    def get(self, request):
        """handle get request"""
        sectors = Sector.objects.all()
        serializer = self.serializer_class(sectors, many=True)
        return Response(serializer.data)
