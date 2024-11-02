from my_project.terminals.controller.general_controller import GeneralController
from my_project.terminals.controller.__init__ import ServiceOrdersService
from my_project.terminals.controller.utils import handle_error, handle_response


class ServiceOrderController(GeneralController):
    def __init__(self):
        super().__init__(ServiceOrdersService())

    def get_service_order_parts(self, service_order_id):
        parts_data = self.service.get_parts(service_order_id)
        if parts_data is None:
            return handle_error(f"No parts found for service order with ID {service_order_id}", 404)
        return handle_response(parts_data, 200)
    
    def get_service_order_technicians(self, service_order_id):
        technicians_data = self.service.get_technicians(service_order_id)
        if technicians_data is None:
            return handle_error(f"No technicians found for service order with ID {service_order_id}", 404)
        return handle_response(technicians_data, 200)
