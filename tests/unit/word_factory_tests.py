# -*- coding: utf-8 -*-
import json
from nose.tools import *

from polish_case_trainer.word.word_factory import WordFactory
from polish_case_trainer.word.word import Word, Adjective


noun_sample_obj = json.loads('{"url": "https://en.wiktionary.org/wiki/ogrodniczka", \
    "gender": "f", "case_forms": {"plural": {"accusative": "ogrodniczki", \
    "instrumental": "ogrodniczkami", "dative": "ogrodniczkom", "locative": \
    "ogrodniczkach", "genitive": "ogrodniczek", "nominative": "ogrodniczki", \
    "vocative": "ogrodniczki"}, "singular": {"accusative": "ogrodniczk\u0119", \
    "instrumental": "ogrodniczk\u0105", "dative": "ogrodniczce", "locative": \
    "ogrodniczce", "genitive": "ogrodniczki", "nominative": "ogrodniczka", \
    "vocative": "ogrodniczko"}}, "word": "ogrodniczka"}')

adjective_sample_obj = json.loads('{"url": "https://en.wiktionary.org/wiki/bogaty", \
    "gender": "m", "case_forms": {"plural": {"m pers": {"accusative": "bogatych", \
    "instrumental": "bogatymi", "dative": "bogatym", "locative": "bogatych", \
    "genitive": "bogatych", "nominative": "bogaci", "vocative": "bogaci"}, "other": \
    {"accusative": "bogate", "instrumental": "bogatymi", "dative": "bogatym", \
    "locative": "bogatych", "genitive": "bogatych", "nominative": "bogate", \
    "vocative": "bogate"}}, "singular": {"m pers": {"accusative": "bogatego", \
    "instrumental": "bogatym", "dative": "bogatemu", "locative": "bogatym", \
    "genitive": "bogatego", "nominative": "bogaty", "vocative": "bogaty"}, "f": \
    {"accusative": "bogat\u0105", "instrumental": "bogat\u0105", "dative": \
    "bogatej", "locative": "bogatej", "genitive": "bogatej", "nominative": "bogata", \
    "vocative": "bogata"}, "m inan": {"accusative": "bogaty", "instrumental": \
    "bogatym", "dative": "bogatemu", "locative": "bogatym", "genitive": "bogatego", \
    "nominative": "bogaty", "vocative": "bogaty"}, "m anim": {"accusative": \
    "bogatego", "instrumental": "bogatym", "dative": "bogatemu", "locative": \
    "bogatym", "genitive": "bogatego", "nominative": "bogaty", "vocative": \
    "bogaty"}, "n": {"accusative": "bogate", "instrumental": "bogatym", "dative": \
    "bogatemu", "locative": "bogatym", "genitive": "bogatego", "nominative": \
    "bogate", "vocative": "bogate"}}}, "word": "bogaty"}')


def test_noun_creation():
    word_factory = WordFactory()
    word = word_factory.create_noun_from_json_object(noun_sample_obj)
    assert isinstance(word, Word)
    assert word.get_basic_form() == "ogrodniczka"
    assert word.get_gender() == "f"


def test_noun_case_forms():
    word_factory = WordFactory()
    word = word_factory.create_noun_from_json_object(noun_sample_obj)
    assert word.get_case_form('plural', 'accusative') == "ogrodniczki"
    assert word.get_case_form('singular', 'accusative') == u"ogrodniczkę"
    assert word.get_case_form('singular', 'instrumental') == u"ogrodniczką"
    assert word.get_case_form('plural', 'dative') == "ogrodniczkom"


def test_adjective_creation():
    word_factory = WordFactory()
    adjective = word_factory.create_adjective_from_json_object(
        adjective_sample_obj)
    assert isinstance(adjective, Adjective)
    assert adjective.get_basic_form() == "bogaty"
    assert adjective.get_gender() == "m"


def test_adjective_case_forms():
    word_factory = WordFactory()
    adjective = word_factory.create_adjective_from_json_object(
        adjective_sample_obj)
    adjective.set_gender("m pers")
    assert adjective.get_case_form('singular', 'accusative') == "bogatego"
    assert adjective.get_case_form('singular', 'dative') == "bogatemu"
    assert adjective.get_case_form('plural', 'dative') == "bogatym"
    assert adjective.get_case_form('plural', 'vocative') == "bogaci"
    adjective.set_gender("n")
    assert adjective.get_case_form('singular', 'instrumental') == "bogatym"
    assert adjective.get_case_form('singular', 'genitive') == "bogatego"
    assert adjective.get_case_form('plural', 'genitive') == "bogatych"
    assert adjective.get_case_form('plural', 'accusative') == "bogate"
