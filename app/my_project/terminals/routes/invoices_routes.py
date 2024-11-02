from flask import Blueprint
from my_project.terminals.controller.orders.invoices_controller import InvoiceController

invoice_bp = Blueprint('invoices', __name__)
invoice_controller = InvoiceController()

@invoice_bp.route('/invoices', methods=['GET'])
def get_invoices():
    return invoice_controller.get_all()

@invoice_bp.route('/invoices/<int:invoice_id>', methods=['GET'])
def get_invoice_by_id(invoice_id):
    return invoice_controller.get_by_id(invoice_id)

@invoice_bp.route('/invoices', methods=['POST'])
def add_invoices():
    return invoice_controller.create()

@invoice_bp.route('/invoices/<int:invoice_id>', methods=['PATCH'])
def update_invoice(invoice_id):
    return invoice_controller.update(invoice_id)

@invoice_bp.route('/invoices/<int:invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    return invoice_controller.delete(invoice_id)

@invoice_bp.route('/invoices/payments/<int:invoice_id>', methods=['GET'])
def get_invoice_payments(invoice_id):
    return invoice_controller.get_invoice_payments(invoice_id)