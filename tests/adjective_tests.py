# -*- coding: utf-8 -*-
from nose.tools import *
from polish_case_trainer.word import Adjective, Word, GenderNotSupported

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
