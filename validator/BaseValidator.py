from abc import ABCMeta, abstractmethod, abstractproperty

class BaseValidator:
    __metaclass__ = ABCMeta

    trim = False

    @abstractproperty
    def message(self):
        pass

    @abstractmethod
    def validate(self, value):
        if self.trim is True and (type(value) is str or type(value) is str):
            return value.strip()

        return value

    def getMessage(self):
        return self.message

    @classmethod
    def __subclasshook__(cls, C):
        if cls is BaseValidator:
            if any("validate" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

    def __init__(self, params):
        if params is not None and 'message' in params:
            self.message = params.get('message')

        if params is not None and 'trim' in params:
            self.trim = params.get('trim')
