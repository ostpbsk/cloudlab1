from flask import Blueprint
from my_project.terminals.controller.orders.customer_comp_controller import CustomerCompanyController

customer_comp_bp = Blueprint('customer_company', __name__)
customer_company_controller = CustomerCompanyController()

@customer_comp_bp.route('/customer_companies', methods=['GET'])
def get_companies():
    return customer_company_controller.get_all()

@customer_comp_bp.route('/customer_companies/<int:company_id>', methods=['GET'])
def get_company_by_id(company_id):
    return customer_company_controller.get_by_id(company_id)

@customer_comp_bp.route('/customer_companies', methods=['POST'])
def add_company():
    return customer_company_controller.create()

@customer_comp_bp.route('/customer_companies/<int:company_id>', methods=['PATCH'])
def update_company(company_id):
    return customer_company_controller.update(company_id)

@customer_comp_bp.route('/customer_companies/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    return customer_company_controller.delete(company_id)

@customer_comp_bp.route('/customer_companies/terminals/<int:company_id>', methods=['GET'])
def get_company_terminals(company_id):
    return customer_company_controller.get_company_terminals(company_id)
