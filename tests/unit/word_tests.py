# -*- coding: utf-8 -*-
from nose.tools import *

from polish_case_trainer.word.word import Word, CaseNotSupported


@raises(TypeError)
def test_instantiation_fails_without_arguments():
    word = Word()

def test_instantiation_succeeds_with_arguments():
    word = Word(u"dzień", "m inan")

def test_instantiation_accepts_valid_values():
    basic_form = u"dzień"
    gender = "m inan"
    word = Word(basic_form, gender)

def test_instantiated_values_are_accessible_via_getters():
    basic_form = u"dzień"
    gender = "m inan"
    word = Word(basic_form, gender)
    assert word.get_basic_form() == basic_form
    assert word.get_gender() == gender

@raises(TypeError)
def test_setting_case_forms_needs_dict():
    word = Word(u"dzień", "m inan")
    word.set_case_forms("m inan", None)

def test_set_case_forms_accepts_valid_data():
    word = Word(u"dzień", "m inan")
    word.set_case_forms("singular", {"nominative": "dzień"})

def test_supports_method_works_with_unset_case_forms():
    word = Word(u"dzień", "m inan")
    assert word.supports("singular", "accusative") is False

def test_supports_method_correctly_identifies_available_case_forms():
    word = Word(u"dzień", "m inan")
    word.set_case_forms("singular", {"nominative": "dzień"})
    assert word.supports("singular", "accusative") is False
    assert word.supports("plural", "nominative") is False
    assert word.supports("singular", "nominative") is True

@raises(CaseNotSupported)
def test_get_case_form_throws_error_for_non_supported_forms():
    word = Word(u"dzień", "m inan")
    word.get_case_form("singular", "nominative")

def test_get_case_form_returns_correct_values():
    word = Word(u"dzień", "m inan")
    word.set_case_forms("singular", {"nominative": "dzień", "instrumental": "dniem"})
    word.set_case_forms("plural", {"nominative": "dni", "locative": "dniach"})
    assert word.get_case_form("singular", "nominative") == "dzień"
    assert word.get_case_form("plural", "nominative") == "dni"
    assert word.get_case_form("plural", "locative") == "dniach"

def test_set_case_forms_overwrites_all_for_specific_number():
    word = Word(u"dzień", "m inan")
    word.set_case_forms("singular", {"nominative": "dzień", "instrumental": "dniem"})
    word.set_case_forms("plural", {"nominative": "dni", "locative": "dniach"})
    # Overwrite the values for singular
    word.set_case_forms("singular", {"nominative": "something", "vocative": "else"})
    assert not word.supports("singular", "instrumental")
    assert word.get_case_form("singular", "nominative") == "something"
    assert word.get_case_form("singular", "vocative") == "else"
    assert word.get_case_form("plural", "nominative") == "dni"
    assert word.get_case_form("plural", "locative") == "dniach"

def test_clear_case_forms_functions_as_advertised():
    word = Word(u"dzień", "m inan")
    word.set_case_forms("singular", {"nominative": "dzień", "instrumental": "dniem"})
    word.set_case_forms("plural", {"nominative": "dni", "locative": "dniach"})
    assert word.get_case_form("singular", "nominative") == "dzień"
    assert word.get_case_form("plural", "nominative") == "dni"
    assert word.get_case_form("plural", "locative") == "dniach"
    word.clear_case_forms()
    assert not word.supports("singular", "nominative")
    assert not word.supports("plural", "nominative")
    assert not word.supports("plural", "locative")

def test_list_case_forms():
    word = Word(u"dzień", "m inan")
    assert word.list_case_forms() == []
    word.set_case_forms("singular", {"nominative": "dzień", "instrumental": "dniem"})
    word.set_case_forms("plural", {"nominative": "dni", "locative": "dniach"})
    assert set(word.list_case_forms()) == set([
        ("singular", "nominative"),
        ("singular", "instrumental"),
        ("plural", "nominative"),
        ("plural", "locative"),
    ])
