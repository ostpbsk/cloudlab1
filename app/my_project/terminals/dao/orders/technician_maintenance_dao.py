from my_project.terminals.dao.general_dao import GeneralDAO

class TechnicianMaintenanceDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import TechnicianMaintenance
    def __init__(self):
        super().__init__(self.TechnicianMaintenance)