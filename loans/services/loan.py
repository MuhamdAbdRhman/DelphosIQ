"""Loan Service"""

import io

import xlsxwriter

from loans.models import Loan


class LoanService:
    """Loan Service"""

    def prepare_loan_data(self):
        loans = Loan.objects.all()
        data = []
        for loan in loans:
            data.append({
                'A': loan.title,
                'B': loan.signature_date,
                'C': loan.country.name,
                'D': loan.sector.name,
                'E': loan.signed_amount,
            })
        return data

    def export_sheet(self):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Data sheet')
        worksheet.set_column('A:A', 30)
        worksheet.set_column('B:B', 20)
        worksheet.set_column('C:C', 20)
        worksheet.set_column('D:D', 20)
        worksheet.set_column('E:E', 20)
        bold = workbook.add_format({'bold': True})
        worksheet.write('A1', 'Title', bold)
        worksheet.write('B1', 'Signature Date', bold)
        worksheet.write('C1', 'Country', bold)
        worksheet.write('D1', 'Sector', bold)
        worksheet.write('E1', 'Signed Amount', bold)
        rows = self.prepare_loan_data()
        for i, row in enumerate(rows):
            for key, value in row.items():
                worksheet.write(f'{key}{i + 2}', value)
        workbook.close()
        output.seek(0)
        return output
