from nose.tools import *

from polish_case_trainer.word.word_bag import WordBag


@raises(TypeError)
def test_invalid_word_list_value_throws_error():
    word_bag = WordBag('invalid type data')

def test_get_word_from_bag_returns_item_from_input_list():
    input_list = [14, 52, 6, 9, 34, 23, 78]
    word_bag = WordBag(input_list)
    assert word_bag.get_word_from_bag() in input_list

