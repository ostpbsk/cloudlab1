from flask import Blueprint
from my_project.terminals.controller.orders.terminal_controller import TerminalController

terminal_bp = Blueprint('terminal', __name__)
terminal_controller = TerminalController()

@terminal_bp.route('/terminals', methods=['GET'])
def get_terminals():
    return terminal_controller.get_all()

@terminal_bp.route('/terminals/<int:terminal_id>', methods=['GET'])
def get_terminal_by_id(terminal_id):
    return terminal_controller.get_by_id(terminal_id)

@terminal_bp.route('/terminals', methods=['POST'])
def add_terminal():
    return terminal_controller.create()

@terminal_bp.route('/terminals/<int:terminal_id>', methods=['PATCH'])
def update_terminal(terminal_id):
    return terminal_controller.update(terminal_id)

@terminal_bp.route('/terminals/<int:terminal_id>', methods=['DELETE'])
def delete_terminal(terminal_id):
    return terminal_controller.delete(terminal_id)
