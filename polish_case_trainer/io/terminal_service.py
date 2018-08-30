import sys
import locale
import inquirer


class TerminalService:

    def display_message(self, text):
        print text

    def prompt_question_response(self, choices=None):
        if isinstance(choices, list):
            # Will be used later for multiple choice questions
            pass
        elif choices is None:
            return self.get_console_input()
        else:
            raise TypeError("The choices argument must be a list")

    def get_console_input(self):
        print "> ",
        return raw_input().decode(sys.stdin.encoding or locale.getpreferredencoding(True))

    def get_checkbox_options(self, text, choices, default=[]):
        result = inquirer.prompt([
            inquirer.Checkbox("checkbox",
                              message=text +
                              " (X/O -Space to select, Enter to submit)",
                              choices=choices,
                              default=default,
                              ),
        ])
        return result["checkbox"] if result else None
