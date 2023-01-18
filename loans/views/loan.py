"""Loan View"""

from django.http import HttpResponse
from rest_framework import views
from rest_framework.response import Response

from loans.models import Loan
from loans.serializers import LoanSerializer
from loans.services import LoanService


class LoanView(views.APIView):
    """Loan View"""

    serializer_class = LoanSerializer

    def get(self, request):
        """handle get request"""
        loans = Loan.objects.all()
        serializer = self.serializer_class(loans, many=True)
        return Response(serializer.data)


class ExportLoanView(views.APIView):
    """Loan View"""

    def get(self, request):
        """handle post request"""
        file = LoanService().export_sheet()
        response = HttpResponse(
            file,
            content_type='application/vnd.openxmlformats-'
                         'officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=loans.xlsx'
        return response
