from validator.BaseValidator import BaseValidator

class LengthValidator(BaseValidator):

    min = None
    max = None
    minMessage = "Min length error"
    maxMessage = "Max length error"
    message = "This value has incorrect length"

    def validate(self, value):

        #possible null values
        if value is None:
            return True

        value = super(LengthValidator, self).validate(value)

        if type(value) is not str:
            value = (str)(value)

        if self.min is not None and len(value) < self.min:
            if self.minMessage is not None:
                self.message = self.minMessage;
            return False

        if self.max is not None and len(value) > self.max:
            if self.maxMessage is not None:
                self.message = self.maxMessage;
            return False

    def __init__(self, params):
        super(LengthValidator, self).__init__(params)

        if 'min' in params:
            self.min = params.get('min')

        if 'max' in params:
            self.max = params.get('max')

        if 'minMessage' in params:
            self.minMessage = params.get('minMessage')

        if 'maxMessage' in params:
            self.maxMessage = params.get('maxMessage')