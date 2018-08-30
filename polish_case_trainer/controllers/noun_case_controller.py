from ..word.word_repository import WordRepository
from ..word.word_factory import WordFactory
from ..word.word_service import WordService
from ..word.word_bag import WordBag
from ..question.question_bag import NounCaseQuestionBag


class NounCaseController:

    _available_numbers = ["singular", "plural"]
    _available_cases = [
        "nominative", "genitive", "dative", "accusative",
        "instrumental", "locative", "vocative"
    ]

    def __init__(self, io_service):
        self.io_service = io_service
        word_service = WordService(WordRepository(), WordFactory())
        self.noun_bag = WordBag(word_service.get_noun_list())
        self.adjective_bag = WordBag(word_service.get_adjective_list())

    def main(self):
        numbers, cases = self._get_question_options()
        self._question_answer_loop(NounCaseQuestionBag(
            self.noun_bag,
            self.adjective_bag,
            numbers,
            cases
        ))

    def _get_question_options(self):
        while True:
            text = "Which grammatical numbers do you want to practise?"
            numbers = self.io_service.get_checkbox_options(
                text,
                self._available_numbers,
                self._available_numbers
            )
            if not numbers:
                self.io_service.display_message(
                    "Error: must select at least one")
            else:
                break
        while True:
            text = "Which cases do you want to practise?"
            available_cases = self._available_cases
            if numbers == ["singular"]:
                available_cases.remove("nominative")
            cases = self.io_service.get_checkbox_options(
                text,
                available_cases,
                available_cases
            )
            if not cases:
                self.io_service.display_message(
                    "Error: must select at least one")
            else:
                break
        return numbers, cases

    def _question_answer_loop(self, question_bag):
        self.io_service.display_message("\n(Ctrl+D to exit)\n")
        while True:
            question = question_bag.get_question()
            self.io_service.display_message(question.get_question_text())
            try:
                answer = self.io_service.get_console_input()
            except EOFError:
                self.io_service.display_message("Exit")
                break
            if question.evaluate(answer):
                self.io_service.display_message("Correct!\n")
            else:
                self.io_service.display_message(
                    u"Incorrect, should have been {}\n".format(
                        question.get_correct_answer())
                )
