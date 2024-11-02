from flask import Blueprint
from my_project.terminals.controller.orders.payments_controller import PaymentController

payments_bp = Blueprint('payments', __name__)
payment_controller = PaymentController()

@payments_bp.route('/payments', methods=['GET'])
def get_payments():
    return payment_controller.get_all()

@payments_bp.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment_by_id(payment_id):
    return payment_controller.get_by_id(payment_id)

@payments_bp.route('/payments', methods=['POST'])
def add_payment():
    return payment_controller.create()

@payments_bp.route('/payments/<int:payment_id>', methods=['PATCH'])
def update_payment(payment_id):
    return payment_controller.update(payment_id)

@payments_bp.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    return payment_controller.delete(payment_id)