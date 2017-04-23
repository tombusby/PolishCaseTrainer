# -*- coding: utf-8 -*-
import json
from nose.tools import *

from polish_case_trainer.word_factory import WordFactory
from polish_case_trainer.word import Word, Adjective


noun_sample_obj = json.loads('{"url": "https://en.wiktionary.org/wiki/ogrodniczka", \
"gender": "f", "case_forms": {"plural": {"accusative": "ogrodniczki", \
"instrumental": "ogrodniczkami", "dative": "ogrodniczkom", "locative": \
"ogrodniczkach", "genitive": "ogrodniczek", "nominative": "ogrodniczki", \
"vocative": "ogrodniczki"}, "singular": {"accusative": "ogrodniczk\u0119", \
"instrumental": "ogrodniczk\u0105", "dative": "ogrodniczce", "locative": \
"ogrodniczce", "genitive": "ogrodniczki", "nominative": "ogrodniczka", "vocative": \
"ogrodniczko"}}, "word": "ogrodniczka"}')

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
