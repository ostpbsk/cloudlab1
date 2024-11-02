# my_project/customer_companies/service/customer_company_service.py
from my_project.terminals.service.general_service import GeneralService
from my_project.terminals.service.__init__ import MaintenanceType
from my_project.terminals.service.__init__ import MaintenanceTypeDAO


class MaintenanceTypeService(GeneralService):

    def __init__(self):
        super().__init__(MaintenanceTypeDAO(), MaintenanceType)

    def get_service_orders(self, maintenance_type_id):
        service_orders = self.dao.get_service_orders_by_maintenance_type_id(maintenance_type_id)
        if not service_orders:
            return None
        return [service_order.to_dict() for service_order in service_orders]