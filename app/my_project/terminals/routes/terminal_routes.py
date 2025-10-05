from flask import Blueprint
from my_project.terminals.controller.orders.terminal_controller import TerminalController

terminal_bp = Blueprint('terminal', __name__)
terminal_controller = TerminalController()

@terminal_bp.route('/terminals', methods=['GET'])
def get_terminals():
    """
    Get all terminals
    ---
    tags:
      - Terminals
    responses:
      200:
        description: List of all terminals
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              address:
                type: string
              gps_latitude:
                type: number
              gps_longitude:
                type: number
              manufacturer:
                type: string
              comissioning_date:
                type: string
              customer_company_id:
                type: integer
    """
    return terminal_controller.get_all()


@terminal_bp.route('/terminals/<int:terminal_id>', methods=['GET'])
def get_terminal_by_id(terminal_id):
    """
    Get a terminal by ID
    ---
    tags:
      - Terminals
    parameters:
      - name: terminal_id
        in: path
        type: integer
        required: true
        description: ID of the terminal to retrieve
    responses:
      200:
        description: Terminal details
        schema:
          type: object
          properties:
            id:
              type: integer
            address:
              type: string
            gps_latitude:
              type: number
            gps_longitude:
              type: number
            manufacturer:
              type: string
            comissioning_date:
              type: string
            customer_company_id:
              type: integer
      404:
        description: Terminal not found
    """
    return terminal_controller.get_by_id(terminal_id)


@terminal_bp.route('/terminals', methods=['POST'])
def add_terminal():
    """
    Create a new terminal
    ---
    tags:
      - Terminals
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - address
            - gps_latitude
            - gps_longitude
            - manufacturer
            - comissioning_date
            - customer_company_id
          properties:
            address:
              type: string
            gps_latitude:
              type: number
            gps_longitude:
              type: number
            manufacturer:
              type: string
            comissioning_date:
              type: string
              format: date
            customer_company_id:
              type: integer
    responses:
      200:
        description: Terminal created successfully
      400:
        description: Invalid input
    """
    return terminal_controller.create()


@terminal_bp.route('/terminals/<int:terminal_id>', methods=['PATCH'])
def update_terminal(terminal_id):
    """
    Update an existing terminal
    ---
    tags:
      - Terminals
    parameters:
      - name: terminal_id
        in: path
        type: integer
        required: true
        description: ID of the terminal to update
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            address:
              type: string
            gps_latitude:
              type: number
            gps_longitude:
              type: number
            manufacturer:
              type: string
            comissioning_date:
              type: string
              format: date
            customer_company_id:
              type: integer
    responses:
      200:
        description: Terminal updated successfully
      404:
        description: Terminal not found
      400:
        description: Invalid input
    """
    return terminal_controller.update(terminal_id)


@terminal_bp.route('/terminals/<int:terminal_id>', methods=['DELETE'])
def delete_terminal(terminal_id):
    """
    Delete a terminal
    ---
    tags:
      - Terminals
    parameters:
      - name: terminal_id
        in: path
        type: integer
        required: true
        description: ID of the terminal to delete
    responses:
      200:
        description: Terminal deleted successfully
      404:
        description: Terminal not found
    """
    return terminal_controller.delete(terminal_id)

