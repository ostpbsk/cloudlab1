# my_project/terminals/dao/terminal_dao.py
from my_project.terminals.dao.general_dao import GeneralDAO

class TerminalDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import Terminal
    def __init__(self):
        super().__init__(self.Terminal)
