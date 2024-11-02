# my_project/terminals/controller/terminal_controller.py
from my_project.terminals.controller.general_controller import GeneralController
from my_project.terminals.controller.__init__ import TerminalService

class TerminalController(GeneralController):
    def __init__(self):
        super().__init__(TerminalService())
