"""User Management URL Configuration"""

from django.urls import path

from .views import *

app_name = "Loans"

urlpatterns = [
    path(
        "loan/",
        LoanView.as_view(),
        name="loan"
    ),
    path(
        "export-loan/",
        ExportLoanView.as_view(),
        name="export_loan"
    ),
    path(
        "country/",
        CountryView.as_view(),
        name="country"
    ),
    path(
        "sector/",
        SectorView.as_view(),
        name="sector"
    ),
]
