# my_project/customer_companies/service/customer_company_service.py
from my_project.terminals.service.general_service import GeneralService
from my_project.terminals.service.__init__ import Payment
from my_project.terminals.service.__init__ import PaymentDAO


class PaymentService(GeneralService):

    def __init__(self):
        super().__init__(PaymentDAO(), Payment)