# -*- coding: utf-8 -*-
from nose.tools import *

from polish_case_trainer.word.word import Adjective, Word, GenderNotSupported


def test_Adjective_is_also_valid_Word_object():
    adjective = Adjective("dobry", "m")
    assert isinstance(adjective, Word)

@raises(GenderNotSupported)
def test_set_gender_fails_if_data_not_available():
    adjective = Adjective("dobry", "m")
    adjective.set_gender("m inan")

@raises(TypeError)
def test_setting_gender_case_forms_needs_dict():
    adjective = Adjective("dobry", "m")
    adjective.set_gender_case_forms("m inan", "singular", None)

def test_set_gender_writes_case_forms_to_Word_superclass():
    adjective = Adjective("dobry", "m")
    adjective.set_gender_case_forms("m pers", "singular", {"nominative": "dobry"})
    adjective.set_gender_case_forms("f", "singular", {"nominative": "dobra"})
    adjective.set_gender_case_forms("f", "plural", {"nominative": "dobre"})
    adjective.set_gender("f")
    assert adjective.supports("singular", "nominative")
    assert adjective.supports("plural", "nominative")
    assert adjective.get_case_form("singular", "nominative") == "dobra"
    assert adjective.get_case_form("plural", "nominative") == "dobre"
    adjective.set_gender("m pers")
    assert adjective.supports("singular", "nominative")
    assert adjective.get_case_form("singular", "nominative") == "dobry"
    assert not adjective.supports("plural", "nominative")

def test_other_gender_forms_work_correctly():
    adjective = Adjective("bogaty", "m")
    adjective.set_gender_case_forms("m pers", "singular", {
        "nominative": "bogaty", "accusative": "bogatego", "dative": "bogatemu"})
    adjective.set_gender_case_forms("m pers", "plural", {
        "nominative": "bogaci", "accusative": "bogatych", "dative": "bogatym"})
    adjective.set_gender_case_forms("f", "singular", {
        "nominative": "bogata", "accusative": u"bogatą", "dative": "bogatej"})
    adjective.set_gender_case_forms("other", "plural", {
        "nominative": "bogate", "accusative": "bogate", "dative": "bogatym"})
    adjective.set_gender("m pers")
    adjective.get_case_form("singular", "accusative") == "bogatego"
    adjective.get_case_form("singular", "dative") == "bogatemu"
    adjective.get_case_form("plural", "nominative") == "bogaci"
    adjective.get_case_form("plural", "dative") == "bogatemu"
    adjective.set_gender("f")
    adjective.get_case_form("singular", "accusative") == u"bogatą"
    adjective.get_case_form("singular", "dative") == "bogatej"
    adjective.get_case_form("plural", "nominative") == "bogate"
    adjective.get_case_form("plural", "dative") == "bogatym"

@raises(GenderNotSupported)
def test_ensure_gender_cant_be_set_to_other():
    adjective = Adjective("bogaty", "m")
    adjective.set_gender_case_forms("other", "plural", {
        "nominative": "bogate", "accusative": "bogate", "dative": "bogatym"})
    adjective.set_gender("other")
