"""scrap website"""

from django.core.management.base import BaseCommand

from loans.models import Loan
from loans.utils import (
    get_table_rows_from_url,
    prepare_amount,
    prepare_country,
    prepare_date,
    prepare_sector,
)


class Command(BaseCommand):
    """Django Command that scrap website """
    help = "scrap website"

    def handle(self, *args, **options):
        """handle"""
        url = "https://www.eib.org/en/projects/loans/index.htm?q=&sortColumn=loanParts.loanPartStatus.statusDate&sortDir=desc&pageNumber=0&itemPerPage=25&pageable=true&language=EN&defaultLanguage=EN&loanPartYearFrom=1959&loanPartYearTo=2023&orCountries.region=true&orCountries=true&orSectors=true"
        rows = get_table_rows_from_url(url)
        for r, row in enumerate(rows):
            loan_data = {
                'title': '',
                'signature_date': '',
                'country': '',
                'sector': '',
                'signed_amount': '',
            }
            # Exclude header and total line from table rows
            if r == 0 or r >= len(rows) - 1:
                continue
            for c, content in enumerate(row.contents):
                if c == 0:
                    loan_data['signature_date'] = prepare_date(content.text)
                elif c == 1:
                    loan_data['title'] = content.text
                elif c == 2:
                    loan_data['country'] = prepare_country(content.text)
                elif c == 3:
                    loan_data['sector'] = prepare_sector(content.text)
                elif c == 4:
                    loan_data['signed_amount'] = prepare_amount(content.text)
            Loan.objects.create(**loan_data)
