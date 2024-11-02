from flask import Blueprint
from my_project.terminals.controller.orders.service_order_parts_controller import ServiceOrderPartController

service_order_parts_bp = Blueprint('service_order_parts', __name__)
service_order_parts_controller = ServiceOrderPartController()

@service_order_parts_bp.route('/service_order_parts', methods=['GET'])
def get_service_order_parts():
    return service_order_parts_controller.get_all()

@service_order_parts_bp.route('/service_order_parts/<int:service_order_part_id>', methods=['GET'])
def get_service_order_part_by_id(service_order_part_id):
    return service_order_parts_controller.get_by_id(service_order_part_id)

@service_order_parts_bp.route('/service_order_parts', methods=['POST'])
def add_service_order_part():
    return service_order_parts_controller.create()

@service_order_parts_bp.route('/service_order_parts/<int:service_order_part_id>', methods=['PATCH'])
def update_service_order_part(service_order_part_id):
    return service_order_parts_controller.update(service_order_part_id)

@service_order_parts_bp.route('/service_order_parts/<int:service_order_part_id>', methods=['DELETE'])
def delete_service_order_part(service_order_part_id):
    return service_order_parts_controller.delete(service_order_part_id)