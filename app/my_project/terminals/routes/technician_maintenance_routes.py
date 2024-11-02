from flask import Blueprint
from my_project.terminals.controller.orders.technician_maintenance_controller import TechnicianMaintenanceController

technician_maintenance_bp = Blueprint('technician_maintenance', __name__)
technician_maintenance_controller = TechnicianMaintenanceController()

@technician_maintenance_bp.route('/technician_maintenances', methods=['GET'])
def get_technicians_maintenances():
    return technician_maintenance_controller.get_all()

@technician_maintenance_bp.route('/technician_maintenances/<int:technician_maintenance_id>', methods=['GET'])
def get_technician_maintenance_by_id(technician_maintenance_id):
    return technician_maintenance_controller.get_by_id(technician_maintenance_id)

@technician_maintenance_bp.route('/technician_maintenances', methods=['POST'])
def add_technician_maintenance():
    return technician_maintenance_controller.create()

@technician_maintenance_bp.route('/technician_maintenances/<int:technician_maintenance_id>', methods=['PATCH'])
def update_technician_maintenance(technician_maintenance_id):
    return technician_maintenance_controller.update(technician_maintenance_id)

@technician_maintenance_bp.route('/technicnian_maintenances/<int:technician_maintenance_id>', methods=['DELETE'])
def delete_technician_maintenance(technician_maintenance_id):
    return technician_maintenance_controller.delete(technician_maintenance_id)