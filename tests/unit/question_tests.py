# -*- coding: utf-8 -*-
from nose.tools import *
from mock import Mock

from polish_case_trainer.question.question import Question, NounCaseQuestion
from polish_case_trainer.word.word import \
    Word, Adjective, GenderNotSupported, CaseNotSupported


def _get_mock_noun(basic_form, gender, case_supported=True):
    noun = Mock(spec=Word)
    noun.get_basic_form = Mock(return_value=basic_form)
    noun.get_gender = Mock(return_value=gender)
    noun.supports = Mock(return_value=case_supported)
    return noun


def _get_mock_adjective(basic_form, gender_supported=True, case_supported=True):
    adjective = Mock(spec=Adjective)
    adjective.get_basic_form = Mock(return_value=basic_form)
    adjective.supports = Mock(return_value=case_supported)
    adjective.set_gender = Mock()
    if not gender_supported:
        adjective.set_gender.side_effect = GenderNotSupported("gender")
    return adjective


@raises(TypeError)
def test_cannot_instantiate_question_abstract_object():
    Question()


@raises(TypeError)
def test_noun_case_question_instantiation_fails_without_arguments():
    NounCaseQuestion()


@raises(TypeError)
def test_noun_case_question_instantiation_fails_if_first_argument_isnt_word_object():
    noun = Mock()
    NounCaseQuestion(noun, None, None, None)


@raises(TypeError)
def test_noun_case_question_instantiation_fails_if_second_argument_isnt_adjective_object():
    noun = Mock(spec=Word)
    adjective = Mock()
    NounCaseQuestion(noun, adjective, None, None)


@raises(GenderNotSupported)
def test_noun_case_question_fails_if_adjective_doesnt_have_forms_for_gender():
    noun = _get_mock_noun("kobieta", "f")
    adjective = _get_mock_adjective("dobry", False)
    NounCaseQuestion(noun, adjective, "plural", "nominative")
    adjective.set_gender.assert_called()


@raises(CaseNotSupported)
def test_noun_case_question_fails_if_noun_doesnt_support_case_form():
    noun = _get_mock_noun("kobieta", "f", False)
    adjective = _get_mock_adjective("dobry")
    NounCaseQuestion(noun, adjective, "plural", "nominative")
    noun.supports.assert_called()


@raises(CaseNotSupported)
def test_noun_case_question_fails_if_nominative_singular_is_requested():
    noun = _get_mock_noun("kobieta", "f")
    adjective = _get_mock_adjective("dobry")
    NounCaseQuestion(noun, adjective, "singular", "nominative")
    adjective.supports.assert_called()


@raises(CaseNotSupported)
def test_noun_case_question_fails_if_adjective_doesnt_support_case_form():
    noun = _get_mock_noun("kobieta", "f")
    adjective = _get_mock_adjective("dobry", True, False)
    NounCaseQuestion(noun, adjective, "plural", "nominative")
    adjective.supports.assert_called()


def test_noun_case_question_instantiation_succeeds_if_passed_all_valid_arguments():
    noun = _get_mock_noun("kobieta", "f")
    adjective = _get_mock_adjective("dobry")
    question = NounCaseQuestion(noun, adjective, "plural", "nominative")
    assert isinstance(question, Question) and isinstance(
        question, NounCaseQuestion)


def test_noun_case_question_get_question_text():
    noun = _get_mock_noun("kobieta", "f")
    adjective = _get_mock_adjective("dobry")
    question = NounCaseQuestion(noun, adjective, "singular", "accusative")
    assert question.get_question_text() == "Noun: kobieta (f)\nAdjective: dobry\n" +\
        "Decline for singular accusative\n"
    noun = _get_mock_noun(u"chłopiec", "m pers")
    adjective = _get_mock_adjective(u"mały")
    question = NounCaseQuestion(noun, adjective, "singular", "accusative")
    assert question.get_question_text() == u"Noun: chłopiec (m pers)\nAdjective: mały\n" +\
        "Decline for singular accusative\n"


def test_incorrect_answer_evaluates_false():
    noun = _get_mock_noun("kobieta", "f")
    noun.get_case_form = Mock(return_value=u"kobietę")
    adjective = _get_mock_adjective("dobry")
    adjective.get_case_form = Mock(return_value=u"dobrą")
    question = NounCaseQuestion(noun, adjective, "singular", "accusative")
    assert not question.evaluate(u"incorrect answer")


def test_correct_answer_evaluates_true():
    noun = _get_mock_noun("kobieta", "f")
    noun.get_case_form = Mock(return_value=u"kobietę")
    adjective = _get_mock_adjective("dobry")
    adjective.get_case_form = Mock(return_value=u"dobrą")
    question = NounCaseQuestion(noun, adjective, "singular", "accusative")
    assert question.evaluate(u"dobrą kobietę")
