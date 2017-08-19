# -*- coding: utf-8 -*-
from nose.tools import *
from mock import Mock

from polish_case_trainer.question.question_bag import QuestionBag, NounCaseQuestionBag
from polish_case_trainer.word.word_bag import WordBag


@raises(TypeError)
def test_cannot_instantiate_question_bag_abstract_object():
    question_bag = QuestionBag()

@raises(TypeError)
def test_noun_case_question_bag_instantiation_fails_without_arguments():
    question_bag = NounCaseQuestionBag()

@raises(TypeError)
def test_noun_case_question_bag_instantiation_fails_if_first_argument_isnt_word_bag_object():
    noun_bag = Mock()
    question_bag = NounCaseQuestionBag(noun_bag, None, None, None)

@raises(TypeError)
def test_noun_case_question_bag_instantiation_fails_if_second_argument_isnt_adjective_object():
    noun_bag = Mock(spec=WordBag)
    adjective_bag = Mock()
    question_bag = NounCaseQuestionBag(noun_bag, adjective_bag, None, None)

@raises(TypeError)
def test_noun_case_question_bag_instantiation_fails_if_third_argument_isnt_list():
    noun_bag = Mock(spec=WordBag)
    adjective_bag = Mock(spec=WordBag)
    allowed_numbers = "invalid"
    question_bag = NounCaseQuestionBag(noun_bag, adjective_bag, allowed_numbers, None)

@raises(TypeError)
def test_noun_case_question_bag_instantiation_fails_if_fourth_argument_isnt_list():
    noun_bag = Mock(spec=WordBag)
    adjective_bag = Mock(spec=WordBag)
    allowed_numbers = []
    allowed_cases = "invalid"
    question_bag = NounCaseQuestionBag(noun_bag, adjective_bag, allowed_numbers, allowed_cases)

def test_noun_case_question_bag_instantiation_succeeds_with_valid_arguments():
    noun_bag = Mock(spec=WordBag)
    adjective_bag = Mock(spec=WordBag)
    allowed_numbers = []
    allowed_cases = []
    question_bag = NounCaseQuestionBag(noun_bag, adjective_bag, allowed_numbers, allowed_cases)
    assert isinstance(question_bag, QuestionBag) and isinstance(question_bag, NounCaseQuestionBag)

# Some more tests here would be good, after the coupling between NounCaseQuestionBag
# and NounCaseQuestion is removed.
