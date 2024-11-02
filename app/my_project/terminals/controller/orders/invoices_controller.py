from my_project.terminals.controller.general_controller import GeneralController
from my_project.terminals.controller.__init__ import InvoiceService
from my_project.terminals.controller.utils import handle_error, handle_response

class InvoiceController(GeneralController):
    def __init__(self):
        super().__init__(InvoiceService())

    def get_invoice_payments(self, invoice_id):
        payments_data = self.service.get_payments(invoice_id)
        if payments_data is None:
            return handle_error(f"No payments found for invoice with ID {invoice_id}", 404)
        return handle_response(payments_data, 200)
