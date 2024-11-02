# my_project/customer_companies/service/customer_company_service.py
from my_project.terminals.service.general_service import GeneralService
from my_project.terminals.service.__init__ import TechnicianMaintenance
from my_project.terminals.service.__init__ import TechnicianMaintenanceDAO


class TechnicianMaintenanceService(GeneralService):

    def __init__(self):
        super().__init__(TechnicianMaintenanceDAO(), TechnicianMaintenance)