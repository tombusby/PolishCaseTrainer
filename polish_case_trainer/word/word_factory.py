from .word import Word, Adjective


class WordFactory:

    def create_noun_from_json_object(self, obj):
        noun = Word(obj['word'], obj['gender'])
        for number, case_forms in obj['case_forms'].items():
            noun.set_case_forms(number, case_forms)
        return noun

    def create_adjective_from_json_object(self, obj):
        adjective = Adjective(obj['word'], obj['gender'])
        for number, gender_case_forms in obj['case_forms'].items():
            for gender, case_forms in gender_case_forms.items():
                adjective.set_gender_case_forms(gender, number, case_forms)
        return adjective
