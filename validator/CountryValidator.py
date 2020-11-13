from validator.BaseValidator import BaseValidator
import pycountry

class CountryValidator(BaseValidator):

    message = "This value is not correct country name"
    countries = pycountry.countries

    def validate(self, value):

        #possible null values
        if value is None:
            return True

        value = super(CountryValidator, self).validate(value)
        try:
            CountryValidator.countries.get(name = value)
            return True
        except(KeyError):
            return False

    def __init__(self, params):
        super(CountryValidator, self).__init__(params)
