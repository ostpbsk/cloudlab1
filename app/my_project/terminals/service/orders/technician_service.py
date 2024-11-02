# my_project/customer_companies/service/customer_company_service.py
from my_project.terminals.service.general_service import GeneralService
from my_project.terminals.service.__init__ import Technician
from my_project.terminals.service.__init__ import TechnicianDAO


class TechnicianService(GeneralService):

    def __init__(self):
        super().__init__(TechnicianDAO(), Technician)

#    def get_customers_with_terminals(self):
#        return self.dao.get_customers_with_terminals()
