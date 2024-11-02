from my_project.terminals.dao.general_dao import GeneralDAO

class MaintenanceTypeDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import MaintenanceType
    def __init__(self):
        super().__init__(self.MaintenanceType)

    def get_service_orders_by_maintenance_type_id(self, maintenance_type_id):
        from my_project.terminals.dao.__init__ import ServiceOrder
        return ServiceOrder.query.filter_by(maintenance_type_id=maintenance_type_id).all()