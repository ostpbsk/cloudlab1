from flask import Blueprint
from my_project.terminals.controller.orders.maintenance_types_controller import MaintenanceTypeController

maintenance_type_bp = Blueprint('maintenance_type', __name__)
maintenance_type_controller = MaintenanceTypeController()

@maintenance_type_bp.route('/maintenance_types', methods=['GET'])
def get_maintenance_types():
    return maintenance_type_controller.get_all()

@maintenance_type_bp.route('/maintenance_types/<int:maintenance_type_id>', methods=['GET'])
def get_maintenance_type_by_id(maintenance_type_id):
    return maintenance_type_controller.get_by_id(maintenance_type_id)

@maintenance_type_bp.route('/maintenance_types', methods=['POST'])
def add_maintenance_type():
    return maintenance_type_controller.create()

@maintenance_type_bp.route('/maintenance_types/<int:maintenance_type_id>', methods=['PATCH'])
def update_maintenance_type(maintenance_type_id):
    return maintenance_type_controller.update(maintenance_type_id)

@maintenance_type_bp.route('/maintenance_types/<int:maintenance_type_id>', methods=['DELETE'])
def delete_maintenance_type(maintenance_type_id):
    return maintenance_type_controller.delete(maintenance_type_id)

@maintenance_type_bp.route('/maintenance_types/service_orders/<int:maintenance_type_id>', methods=['GET'])
def get_service_orders(maintenance_type_id):
    return maintenance_type_controller.get_maintenance_type_service_orders(maintenance_type_id)