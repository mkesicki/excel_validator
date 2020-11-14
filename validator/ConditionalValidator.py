from validator.BaseValidator import BaseValidator

class ConditionalValidator(BaseValidator):

    operator = None #should be a lambda expression which return boolean variable
    message = "This value is not valid"

    def validate(self, fieldA, fieldB):

        fieldA = super(ConditionalValidator, self).validate(fieldA)
        fieldB = super(ConditionalValidator, self).validate(fieldB)

        return self.operator(fieldA, fieldB)

    def __init__(self, params):
        super(ConditionalValidator, self).__init__(params)

        if 'fieldB' in params:
            self.fieldB = params.get('fieldB')
        else:
            raise ValueError("Missing conditional field parameter")

        if 'operator' in params:
            self.operator = eval(params.get('operator'))
        else:
            raise ValueError("Missing operator parameter")

        if self.operator.__name__ != "<lambda>":
            raise ValueError("Operator should be an lambda function")
