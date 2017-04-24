import random, sys, locale, unicodedata

from .word_repository import WordRepository
from .word_factory import WordFactory
from .word_service import WordService
from .word_bag import WordBag
from .word import CaseNotSupported, GenderNotSupported


class Controller:

    def main(self):
        word_repository = WordRepository()
        word_factory = WordFactory()
        word_service = WordService(word_repository, word_factory)
        noun_bag = WordBag(word_service.get_noun_list())
        adjective_bag = WordBag(word_service.get_adjective_list())
        for i in range(20):
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
                    break
            noun_form = noun.get_case_form(number, case)
            adjective_form = adjective.get_case_form(number, case)
            print u"Noun: {} ({})\nAdjective: {}\nDecline for {} {}\n".format(
                noun.get_basic_form(), noun.get_gender(), adjective.get_basic_form(), number, case
            )
            print "> ",
            user_input = self._get_console_input()
            correct_forms = u"{} {}".format(adjective_form, noun_form)
            if self._compare_unicode_values(user_input, correct_forms):
                print "Correct!\n"
            else:
                print u"Incorrect, should have been {}\n".format(correct_forms)

    def _get_console_input(self):
        return raw_input().decode(sys.stdin.encoding or locale.getpreferredencoding(True))

    def _compare_unicode_values(self, a, b):
        return unicodedata.normalize('NFC', a) == unicodedata.normalize('NFC', b)


if __name__ == "__main__":
    Controller().main()
