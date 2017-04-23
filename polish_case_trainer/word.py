
class Word(object):

    def __init__(self, basic_form, gender):
        self.basic_form = basic_form
        self.gender = gender
        self.case_forms = {}

    def get_basic_form(self):
        return self.basic_form

    def get_gender(self):
        return self.gender

    def set_case_forms(self, number, case_forms):
        if not isinstance(case_forms, dict):
            raise TypeError("case_forms must be a dict object")
        self.case_forms[number] = case_forms

    def clear_case_forms(self):
        self.case_forms = {}

    def list_case_forms(self):
        return [(number, case_name) \
            for number, case_dict in self.case_forms.items() \
            for case_name in case_dict.keys()]

    def supports(self, number, case):
        return number in self.case_forms and case in self.case_forms[number]

    def get_case_form(self, number, case):
        if not self.supports(number, case):
            raise CaseNotSupported(number, case)
        return self.case_forms[number][case]

class Adjective(Word):
    """ An adjective is just considered a word that can change its own gender """

    def __init__(self, *args):
        super(Adjective, self).__init__(*args)
        self.gender_case_forms = {}

    def set_gender(self, gender):
        if gender == "other" or gender not in self.gender_case_forms:
            raise GenderNotSupported(gender)
        self.clear_case_forms()
        for number, case_forms in self.gender_case_forms[gender].items():
            self.set_case_forms(number, case_forms)
        if "other" in self.gender_case_forms:
            for number, case_forms in self.gender_case_forms["other"].items():
                if number not in self.case_forms:
                    self.set_case_forms(number, case_forms)

    def set_gender_case_forms(self, gender, number, case_forms):
        if not isinstance(case_forms, dict):
            raise TypeError("case_forms must be a dict object")
        if gender not in self.gender_case_forms:
            self.gender_case_forms[gender] = {}
        self.gender_case_forms[gender][number] = case_forms

class CaseNotSupported(Exception):

    def __init__(self, number, case):
        self.number = number
        self.case = case
        Exception.__init__(self, "The case '{} {}' is not supported by this word".format(number, case))

class GenderNotSupported(Exception):

    def __init__(self, gender):
        self.gender = gender
        Exception.__init__(self, "The gender '{}' is not supported by this word".format(gender))
