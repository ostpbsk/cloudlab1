from my_project.terminals.dao.general_dao import GeneralDAO

class ServiceOrderPartDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import ServiceOrderPart
    def __init__(self):
        super().__init__(self.ServiceOrderPart)