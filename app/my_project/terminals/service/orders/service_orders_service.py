# my_project/customer_companies/service/customer_company_service.py
from my_project.terminals.service.general_service import GeneralService
from my_project.terminals.service.__init__ import ServiceOrder
from my_project.terminals.service.__init__ import ServiceOrderDAO


class ServiceOrdersService(GeneralService):

    def __init__(self):
        super().__init__(ServiceOrderDAO(), ServiceOrder)
    
    def get_parts(self, service_order_id):
        parts = self.dao.get_parts_by_service_order_id(service_order_id)
        if parts is None:
            return None
        return [part.to_dict() for part in parts]
    
    def get_technicians(self, service_order_id):
        technicians = self.dao.get_technicians_by_service_order_id(service_order_id)
        if technicians is None:
            return None
        return [technician.to_dict() for technician in technicians]