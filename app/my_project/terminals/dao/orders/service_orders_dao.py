from my_project.terminals.dao.general_dao import GeneralDAO
from my_project.terminals.dao.__init__ import ServiceOrder

class ServiceOrderDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import ServiceOrder
    def __init__(self):
        super().__init__(self.ServiceOrder)

    def get_parts_by_service_order_id(self, service_order_id):
        service_order = ServiceOrder.query.get(service_order_id)
        return service_order.parts if service_order else None
    
    def get_technicians_by_service_order_id(self, service_order_id):
        service_order = ServiceOrder.query.get(service_order_id)
        return service_order.technicians if service_order else None
    
    