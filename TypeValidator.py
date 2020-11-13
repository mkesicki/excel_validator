import BaseValidator

class TypeValidator(BaseValidator.BaseValidator):

    message = "Wrong type"
    type = ""
    types = {
        "integer": "isInteger",
        "float": "isFloat",
        "bool": "isBool"
    }

    def validate(self, value):

        #possible null values
        if value is None:
            return True

        value = super(TypeValidator, self).validate(value)

        #call validation method
        return getattr(self, self.types[self.type])(value)

    def isInteger(self, value):

        try:
            int(value)

            return True

        except ValueError:

            return False

    def isBool(self, value):

        if str(value) == '1' or str(value) == '0':
            return True

        return False

    def isFloat(self, value):

        try:
            float(value)

            return True

        except ValueError:

            return False

    def __init__(self, params):
        super(TypeValidator, self).__init__(params)
        self.type = params.get('type')
        if not 'message' in params:
            self.message = "Cell should be type of %s"  % self.type

        if not self.type in self.types:
            raise ValueError(self.type + " does not exists")
