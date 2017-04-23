from .word import Word, Adjective


class WordFactory:

    def create_noun_from_json_object(self, obj):
        noun = Word(obj['word'], obj['gender'])
        for number, case_forms in obj['case_forms'].items():
            noun.set_case_forms(number, case_forms)
        return noun
