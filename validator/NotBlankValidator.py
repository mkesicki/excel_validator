from  validator.BaseValidator import BaseValidator
import re


class NotBlankValidator(BaseValidator):

    required = True
    message = "Cell can not be blank"

    def validate(self, value):

        if self.required == False or (value != None and value != ""):
            return True

        return False

    def __init__(self, params):
        super(NotBlankValidator, self).__init__(params)

