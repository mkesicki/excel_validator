import BaseValidator
from validate_email import validate_email
class EmailValidator(BaseValidator.BaseValidator):

    message = "Value is not correct email address"

    def validate(self, value):

        #possible null values
        if value is None:
            return True

        value = super(EmailValidator, self).validate(value)
        if type(value) is str or type(value) is str:
            return  validate_email(value)

        return False

    def __init__(self, params):
        super(EmailValidator, self).__init__(params)

