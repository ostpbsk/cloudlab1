# my_project/customer_companies/controller/customer_company_controller.py
from flask import jsonify
from my_project.terminals.controller.general_controller import GeneralController
from my_project.terminals.controller.__init__ import CustomerCompanyService
from my_project.terminals.controller.utils import handle_error, handle_response

class CustomerCompanyController(GeneralController):
    def __init__(self):
        super().__init__(CustomerCompanyService())

    def get_company_terminals(self, company_id):
        terminals_data = self.service.get_company_terminals(company_id)

        if terminals_data is None:
            return handle_error(f"Company with id: {company_id} is not found", 404)
        return handle_response(terminals_data, 200)
