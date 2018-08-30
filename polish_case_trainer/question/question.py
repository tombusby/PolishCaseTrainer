import unicodedata
from abc import ABCMeta, abstractmethod

from ..word.word import Word, Adjective, CaseNotSupported


class Question:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_question_text(self):
        pass

    @abstractmethod
    def get_question_options(self):
        pass

    @abstractmethod
    def evaluate(self, answer):
        pass

    @abstractmethod
    def get_correct_answer(self):
        pass


class NounCaseQuestion(Question):

    def __init__(self, noun, adjective, number, case):
        if not isinstance(noun, Word):
            raise TypeError("noun must be a Word object")
        if not isinstance(adjective, Adjective):
            raise TypeError("adjective must be a Ajective object")
        if number == "singular" and case == "nominative":
            raise CaseNotSupported(number, case)
        # May throw GenderNotSupported Exception
        adjective.set_gender(noun.get_gender())
        if not noun.supports(number, case) or not adjective.supports(number, case):
            raise CaseNotSupported(number, case)
        self._noun = noun
        self._adjective = adjective
        self._number = number
        self._case = case

    def get_question_text(self):
        return u"Noun: {} ({})\nAdjective: {}\nDecline for {} {}\n".format(
            self._noun.get_basic_form(),
            self._noun.get_gender(),
            self._adjective.get_basic_form(),
            self._number,
            self._case
        )

    def get_question_options(self):
        """
        Returning None signifies that this is not muliple choice.
        Because of this, the terminal service will give a standard text prompt.
        """
        return None

    def evaluate(self, answer):
        correct_forms = self.get_correct_answer()
        return unicodedata.normalize('NFC', answer) \
            == unicodedata.normalize('NFC', correct_forms)

    def get_correct_answer(self):
        noun_form = self._noun.get_case_form(self._number, self._case)
        adjective_form = self._adjective.get_case_form(
            self._number, self._case)
        return u"{} {}".format(adjective_form, noun_form)
