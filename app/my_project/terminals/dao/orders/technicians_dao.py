from my_project.terminals.dao.general_dao import GeneralDAO

class TechnicianDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import Technician
    def __init__(self):
        super().__init__(self.Technician)