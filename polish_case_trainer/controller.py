import random, sys, locale, unicodedata

from .word_repository import WordRepository
from .word_factory import WordFactory
from .word_service import WordService
from .word_bag import WordBag
from .word import GenderNotSupported


class Controller:

    def __init__(self):
        word_repository = WordRepository()
        word_factory = WordFactory()
        self.word_service = WordService(word_repository, word_factory)

    def main(self):
        # Opportunity to add a menu for other game modes here
        self._adjective_noun_case_trainer()

    def _adjective_noun_case_trainer(self):
        print "\n(Ctrl+D to exit)\n"
        while True:
            noun, adjective, number, case = self._choose_compatible_noun_and_adjective()
            noun_form = noun.get_case_form(number, case)
            adjective_form = adjective.get_case_form(number, case)
            self._print_instructions(noun, adjective, number, case)
            try:
                answer = self._get_console_input()
            except EOFError:
                print "Exit"
                break
            self._process_user_answer(noun_form, adjective_form, answer)

    def _choose_compatible_noun_and_adjective(self):
        noun_bag = WordBag(self.word_service.get_noun_list())
        adjective_bag = WordBag(self.word_service.get_adjective_list())
        while True:
            noun, adjective = noun_bag.get_word_from_bag(), adjective_bag.get_word_from_bag()
            gender = noun.get_gender()
            try:
                adjective.set_gender(gender)
            except GenderNotSupported:
                continue
            if not noun.list_case_forms():
                continue
            number, case = random.choice(noun.list_case_forms())
            if adjective.supports(number, case):
                return noun, adjective, number, case

    def _print_instructions(self, noun, adjective, number, case):
        print u"Noun: {} ({})\nAdjective: {}\nDecline for {} {}\n".format(
            noun.get_basic_form(), noun.get_gender(), adjective.get_basic_form(), number, case
        )
        print "> ",

    def _get_console_input(self):
        return raw_input().decode(sys.stdin.encoding or locale.getpreferredencoding(True))

    def _process_user_answer(self, noun_form, adjective_form, answer):
        def _compare_unicode_values(a, b):
            return unicodedata.normalize('NFC', a) == unicodedata.normalize('NFC', b)
        correct_forms = u"{} {}".format(adjective_form, noun_form)
        if _compare_unicode_values(answer, correct_forms):
            print "Correct!\n"
        else:
            print u"Incorrect, should have been {}\n".format(correct_forms)

if __name__ == "__main__":
    Controller().main()
