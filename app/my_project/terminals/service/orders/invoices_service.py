# my_project/customer_companies/service/customer_company_service.py
from my_project.terminals.service.general_service import GeneralService
from my_project.terminals.service.__init__ import Invoice
from my_project.terminals.service.__init__ import InvoiceDAO


class InvoiceService(GeneralService):

    def __init__(self):
        super().__init__(InvoiceDAO(), Invoice)

    def get_payments(self, invoice_id):
        payments = self.dao.get_payments_by_invoice_id(invoice_id)
        if not payments:
            return None
        return [payment.to_dict() for payment in payments]
