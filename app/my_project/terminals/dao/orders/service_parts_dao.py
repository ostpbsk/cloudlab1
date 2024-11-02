from my_project.terminals.dao.general_dao import GeneralDAO

class ServicePartDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import ServicePart
    def __init__(self):
        super().__init__(self.ServicePart)