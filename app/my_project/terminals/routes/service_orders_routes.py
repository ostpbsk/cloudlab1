from flask import Blueprint
from my_project.terminals.controller.orders.service_orders_controller import ServiceOrderController

service_orders_bp = Blueprint('service_orders', __name__)
service_orders_controller = ServiceOrderController()

@service_orders_bp.route('/service_orders', methods=['GET'])
def get_service_orders():
    return service_orders_controller.get_all()

@service_orders_bp.route('/service_orders/<int:service_order_id>', methods=['GET'])
def get_service_order_by_id(service_order_id):
    return service_orders_controller.get_by_id(service_order_id)

@service_orders_bp.route('/service_orders', methods=['POST'])
def add_service_order():
    return service_orders_controller.create()

@service_orders_bp.route('/service_orders/<int:service_order_id>', methods=['PATCH'])
def update_service_order(service_order_id):
    return service_orders_controller.update(service_order_id)

@service_orders_bp.route('/service_orders/<int:service_order_id>', methods=['DELETE'])
def delete_service_order(service_order_id):
    return service_orders_controller.delete(service_order_id)

@service_orders_bp.route('service_orders/parts/<int:service_order_id>', methods=['GET'])
def get_service_order_parts(service_order_id):
    return service_orders_controller.get_service_order_parts(service_order_id)

@service_orders_bp.route('service_orders/technicians/<int:service_order_id>', methods=['GET'])
def get_technicians(service_order_id):
    return service_orders_controller.get_service_order_technicians(service_order_id)