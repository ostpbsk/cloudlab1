from my_project.terminals.dao.general_dao import GeneralDAO

class PaymentDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import Payment
    def __init__(self):
        super().__init__(self.Payment)