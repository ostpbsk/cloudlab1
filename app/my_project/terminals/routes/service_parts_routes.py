from flask import Blueprint
from my_project.terminals.controller.orders.service_parts_controller import ServicePartController

service_parts_bp = Blueprint('service_parts', __name__)
service_parts_controller = ServicePartController()

@service_parts_bp.route('/service_parts', methods=['GET'])
def get_service_parts():
    return service_parts_controller.get_all()

@service_parts_bp.route('/service_parts/<int:service_part_id>', methods=['GET'])
def get_service_part_by_id(service_part_id):
    return service_parts_controller.get_by_id(service_part_id)

@service_parts_bp.route('/service_parts', methods=['POST'])
def add_service_part():
    return service_parts_controller.create()

@service_parts_bp.route('/service_parts/<int:service_part_id>', methods=['PATCH'])
def update_service_part(service_part_id):
    return service_parts_controller.update(service_part_id)

@service_parts_bp.route('/service_order_parts/<int:service_part_id>', methods=['DELETE'])
def delete_service_part(service_part_id):
    return service_parts_controller.delete(service_part_id)