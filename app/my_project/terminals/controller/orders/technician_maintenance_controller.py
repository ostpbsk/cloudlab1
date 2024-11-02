from my_project.terminals.controller.general_controller import GeneralController
from my_project.terminals.controller.__init__ import TechnicianMaintenanceService

class TechnicianMaintenanceController(GeneralController):
    def __init__(self):
        super().__init__(TechnicianMaintenanceService())
