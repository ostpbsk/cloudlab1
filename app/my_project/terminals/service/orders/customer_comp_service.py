# my_project/customer_companies/service/customer_company_service.py
from my_project.terminals.service.general_service import GeneralService
from my_project.terminals.service.__init__ import CustomerCompany
from my_project.terminals.service.__init__ import CustomerCompanyDAO


class CustomerCompanyService(GeneralService):

    def __init__(self):
        super().__init__(CustomerCompanyDAO(), CustomerCompany)

    def get_company_terminals(self, company_id):
        return self.dao.get_company_terminals(company_id)
