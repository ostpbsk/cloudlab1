from flask import Blueprint
from my_project.terminals.controller.orders.technician_controller import TechnicianController

technician_bp = Blueprint('technician', __name__)
technician_controller = TechnicianController()

@technician_bp.route('/technicians', methods=['GET'])
def get_technicians():
    return technician_controller.get_all()

@technician_bp.route('/technicians/<int:technician_id>', methods=['GET'])
def get_technician_by_id(technician_id):
    return technician_controller.get_by_id(technician_id)

@technician_bp.route('/technicians', methods=['POST'])
def add_technician():
    return technician_controller.create()

@technician_bp.route('/technicians/<int:technician_id>', methods=['PATCH'])
def update_technician(technician_id):
    return technician_controller.update(technician_id)

@technician_bp.route('/technicnians/<int:technician_id>', methods=['DELETE'])
def delete_technician(technician_id):
    return technician_controller.delete(technician_id)