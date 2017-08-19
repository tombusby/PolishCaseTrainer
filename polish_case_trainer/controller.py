import random, sys, locale, unicodedata

from .word.word_repository import WordRepository
from .word.word_factory import WordFactory
from .word.word_service import WordService
from .word.word_bag import WordBag
from .word.word import GenderNotSupported, CaseNotSupported
from .question.question import NounCaseQuestion
from .question.question_bag import NounCaseQuestionBag

class Controller:

    def __init__(self):
        word_service = WordService(WordRepository(), WordFactory())
        noun_bag = WordBag(word_service.get_noun_list())
        adjective_bag = WordBag(word_service.get_adjective_list())
        self.question_bag = NounCaseQuestionBag(
            noun_bag,
            adjective_bag,
            ["singular", "plural"],
            [
                "accusative", "instrumental", "dative", "locative",
                "genitive", "nominative", "vocative"
            ]
        )

    def main(self):
        # Opportunity to add a menu for other game modes here
        self._adjective_noun_case_trainer()

    def _adjective_noun_case_trainer(self):
        print "\n(Ctrl+D to exit)\n"
        while True:
            question = self.question_bag.get_question()
            self._print_instructions(question)
            try:
                answer = self._get_console_input()
            except EOFError:
                print "Exit"
                break
            self._display_answer_result(question, answer)

    def _print_instructions(self, question):
        print question.get_question_text()
        print "> ",

    def _get_console_input(self):
        return raw_input().decode(sys.stdin.encoding or locale.getpreferredencoding(True))

    def _display_answer_result(self, question, answer):
        if question.evaluate(answer):
            print "Correct!\n"
        else:
            print u"Incorrect, should have been {}\n".format(question.get_correct_answer())

if __name__ == "__main__":
    Controller().main()
