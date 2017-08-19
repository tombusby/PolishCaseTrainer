import json, os


class WordRepository:

    def __init__(self, dir_path=None):
        if dir_path is None:
            dir_path = os.path.dirname(os.path.realpath(__file__))
        self.noun_path = os.path.join(dir_path, "word-data", "nouns.json")
        self.adjective_path = os.path.join(dir_path, "word-data", "adjectives.json")

    def retrieve_nouns(self):
        with open(self.noun_path) as f:
            for line in f:
                yield json.loads(line)

    def retrieve_adjectives(self):
        with open(self.adjective_path) as f:
            for line in f:
                yield json.loads(line)
