from collections import Iterable
from elemental_core import ElementalBase


class AttributeKind(ElementalBase):
    """
    Base class for Attribute Kinds.
    """

    @staticmethod
    def process_value(value, **params):
        return value

    @staticmethod
    def validate_value(value, **params):
        return True

    @staticmethod
    def filter_value(value, **params):
        return True

    @staticmethod
    def sort_values(values, **params):
        reverse = params.get('reverse')
        keys = params.get('keys', [])

        if not isinstance(keys, Iterable):
            keys = [keys]

        if keys:
            result = values[:]
            for key in keys:
                result = sorted(result, key=key)
        else:
            result = sorted(values)

        if reverse:
            result = reversed(result)

        return result
