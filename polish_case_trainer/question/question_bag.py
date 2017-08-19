import random
from abc import ABCMeta, abstractmethod

from ..word.word import CaseNotSupported, GenderNotSupported
from ..word.word_bag import WordBag
from ..question.question import NounCaseQuestion

class QuestionBag:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_question(self):
        pass

class NounCaseQuestionBag(QuestionBag):

    def __init__(self, noun_bag, adjective_bag, allowed_numbers, allowed_cases):
        if not isinstance(noun_bag, WordBag) or not isinstance(adjective_bag, WordBag):
            raise TypeError("noun_bag and adjective_bag must be WordBag objects")
        if not isinstance(allowed_cases, list) or not isinstance(allowed_numbers, list):
            raise TypeError("allowed_cases and allowed_numbers must be list objects")
        self._noun_bag = noun_bag
        self._adjective_bag = adjective_bag
        self._allowed_numbers = allowed_numbers
        self._allowed_cases = allowed_cases

    def get_question(self):
        while True:
            noun = self._noun_bag.get_word_from_bag()
            adjective = self._adjective_bag.get_word_from_bag()
            try:
                number, case = self._get_case_and_number()
                question = NounCaseQuestion(noun, adjective, number, case)
            except (GenderNotSupported, CaseNotSupported):
                continue
            return question

    def _get_case_and_number(self):
        return random.choice(self._allowed_numbers), random.choice(self._allowed_cases)
