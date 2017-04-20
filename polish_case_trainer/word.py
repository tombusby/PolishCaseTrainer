
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

    def supports(self, number, case):
        return number in self.case_forms and case in self.case_forms[number]

    def get_case_form(self, number, case):
        if not self.supports(number, case):
            raise KeyError("This grammatical number and case are not supported")
        return self.case_forms[number][case]
