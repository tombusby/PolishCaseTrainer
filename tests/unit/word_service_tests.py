# -*- coding: utf-8 -*-
from nose.tools import *
from mock import Mock

from polish_case_trainer.word.word_service import WordService


class MockClass:
    pass


def _get_mock_word_repository():
    word_repository = MockClass()
    word_repository.retrieve_nouns = Mock(return_value=[])
    word_repository.retrieve_adjectives = Mock(return_value=[])
    return word_repository


def _get_mock_word_factory():
    word_factory = MockClass()
    word_factory.create_noun_from_json_object = Mock(return_value=MockClass())
    word_factory.create_adjective_from_json_object = Mock(
        return_value=MockClass())
    return word_factory


def test_get_noun_list_calls_word_repository_once():
    word_repository = _get_mock_word_repository()
    word_factory = _get_mock_word_factory()
    word_service = WordService(word_repository, word_factory)
    assert word_service.get_noun_list() == []
    word_repository.retrieve_nouns.assert_called_once()


def test_get_noun_calls_word_factory_correct_number_of_times():
    word_repository = _get_mock_word_repository()
    word_factory = _get_mock_word_factory()
    word_service = WordService(word_repository, word_factory)
    word_repository.retrieve_nouns.return_value = [
        {'foo': 'bar'},
        {'fizz': 'buzz'}
    ]
    assert len(word_service.get_noun_list()) == 2
    word_factory.create_noun_from_json_object.assert_called()
    word_factory.create_adjective_from_json_object.assert_not_called()


def test_get_adjective_list_calls_word_repository_once():
    word_repository = _get_mock_word_repository()
    word_factory = _get_mock_word_factory()
    word_service = WordService(word_repository, word_factory)
    assert word_service.get_adjective_list() == []
    word_repository.retrieve_adjectives.assert_called_once()


def test_get_adjective_calls_word_factory_correct_number_of_times():
    word_repository = _get_mock_word_repository()
    word_factory = _get_mock_word_factory()
    word_service = WordService(word_repository, word_factory)
    word_repository.retrieve_adjectives.return_value = [
        {'foo': 'bar'},
        {'fizz': 'buzz'}
    ]
    assert len(word_service.get_adjective_list()) == 2
    word_factory.create_adjective_from_json_object.assert_called()
    word_factory.create_noun_from_json_object.assert_not_called()
