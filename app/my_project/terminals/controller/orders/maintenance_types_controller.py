from my_project.terminals.controller.general_controller import GeneralController
from my_project.terminals.controller.__init__ import MaintenanceTypeService
from my_project.terminals.controller.utils import handle_error, handle_response

class MaintenanceTypeController(GeneralController):
    def __init__(self):
        super().__init__(MaintenanceTypeService())

    def get_maintenance_type_service_orders(self, maintenance_type_id):
        service_orders_data = self.service.get_service_orders(maintenance_type_id)
        if service_orders_data is None:
            return handle_error(f"No service orders found for maintenance type with ID {maintenance_type_id}", 404)
        return handle_response(service_orders_data, 200)
