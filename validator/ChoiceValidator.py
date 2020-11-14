from validator.BaseValidator import BaseValidator

class ChoiceValidator(BaseValidator):

    message = "This value is not valid choice"
    choices = []
    caseSensitive = True

    def validate(self, value):

        #possible null values
        if value is None:
            return True

        value = super(ChoiceValidator, self).validate(value)

        if self.caseSensitive == False:
            value = value.lower()

        if value in self.choices:
            return True

        return False

    def __init__(self, params):
        super(ChoiceValidator, self).__init__(params)

        if not 'choices' in params:
            raise ValueError("Valid choice are not set")
        self.choices = params.get('choices')

        if 'caseSensitive' in params:
            self.caseSensitive = params.get('caseSensitive')
