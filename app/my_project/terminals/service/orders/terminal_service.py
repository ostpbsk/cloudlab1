# my_project/terminals/service/terminal_service.py
from my_project.terminals.service.general_service import GeneralService
from my_project.terminals.service.__init__ import TerminalDAO
from my_project.terminals.service.__init__ import Terminal

class TerminalService(GeneralService):
    def __init__(self):
        super().__init__(TerminalDAO(), Terminal)
