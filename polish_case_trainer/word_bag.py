import random


class WordBag:

    def __init__(self, word_list):
        if not isinstance(word_list, list):
            raise TypeError("word_list must be a list object")
        self.word_list = word_list

    def get_word_from_bag(self):
        return random.choice(self.word_list)
