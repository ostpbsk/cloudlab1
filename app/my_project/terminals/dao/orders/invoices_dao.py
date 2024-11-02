from my_project.terminals.dao.general_dao import GeneralDAO

class InvoiceDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import Invoice
    def __init__(self):
        super().__init__(self.Invoice)

    def get_payments_by_invoice_id(self, invoice_id):
        from my_project.terminals.dao.__init__ import Payment
        return Payment.query.filter_by(invoice_id=invoice_id).all()