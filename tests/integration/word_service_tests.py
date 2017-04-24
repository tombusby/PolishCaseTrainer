# -*- coding: utf-8 -*-
import os
from nose.tools import *

from polish_case_trainer.word_repository import WordRepository
from polish_case_trainer.word_factory import WordFactory
from polish_case_trainer.word_service import WordService


def test_retrieve_nouns():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    word_repository = WordRepository(dir_path)
    word_factory = WordFactory()
    word_service = WordService(word_repository, word_factory)
    nouns = word_service.get_noun_list()
    assert len(nouns) == 3
    assert nouns[0].get_basic_form() == "klucz"
    assert nouns[0].get_case_form("plural", "instrumental") == "kluczami"
    assert nouns[1].get_basic_form() == "niewolnictwo"
    assert nouns[1].get_gender() == "n"
    assert nouns[1].get_case_form("singular", "dative") == "niewolnictwu"
    assert not nouns[1].supports("plural", "nominative")
    assert nouns[2].get_basic_form() == "nora"
    assert nouns[2].get_case_form("singular", "accusative") == u"norę"
    assert nouns[2].get_case_form("singular", "instrumental") == u"norą"
    assert nouns[2].supports("plural", "nominative")

def test_retrieve_adjectives():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    word_repository = WordRepository(dir_path)
    word_factory = WordFactory()
    word_service = WordService(word_repository, word_factory)
    adjectives = word_service.get_adjective_list()
    assert len(adjectives) == 3
    assert adjectives[0].get_basic_form() == "alternatywny"
    adjectives[0].set_gender("n")
    assert adjectives[0].get_case_form("singular", "genitive") == "alternatywnego"
    assert adjectives[0].get_case_form("plural", "vocative") == "alternatywne"
    adjectives[0].set_gender("f")
    assert adjectives[0].get_case_form("singular", "genitive") == "alternatywnej"
    assert adjectives[1].get_basic_form() == u"lśniący"
    adjectives[1].set_gender("m pers")
    assert adjectives[1].get_case_form("singular", "locative") == u"lśniącym"
    assert adjectives[1].get_case_form("plural", "accusative") == u"lśniących"
    adjectives[1].set_gender("n")
    assert adjectives[1].get_case_form("singular", "dative") == u"lśniącemu"
    assert adjectives[2].get_basic_form() == u"poligamiczny"
    adjectives[2].set_gender("m inan")
    assert adjectives[2].get_case_form("singular", "accusative") == u"poligamiczny"
    assert adjectives[2].get_case_form("plural", "nominative") == u"poligamiczne"
    adjectives[2].set_gender("f")
    assert adjectives[2].get_case_form("singular", "instrumental") == u"poligamiczną"
