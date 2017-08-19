from .io.terminal_service import TerminalService
from .controllers.noun_case_controller import NounCaseController


class Controller:

    def __init__(self):
        self.io_service = TerminalService()

    def main(self):
        title = "\n====================\nPolish Case Trainer!\n====================\n"
        self.io_service.display_message(title)
        # Opportunity to add a menu for other game modes here
        NounCaseController(self.io_service).main()

if __name__ == "__main__":
    Controller().main()
