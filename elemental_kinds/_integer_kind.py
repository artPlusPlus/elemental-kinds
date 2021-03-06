import operator

from .errors import (
    AttributeKindValueProcessingError,
    AttributeKindValueValidationError
)
from ._attribute_kind import AttributeKind


_filter_tests = (
    ('<', operator.lt),
    ('<=', operator.le),
    ('>', operator.gt),
    ('>=', operator.ge),
    ('==', operator.eq),
    ('!=', operator.ne)
)


class IntegerKind(AttributeKind):
    @staticmethod
    def process_value(value, **type_properties):
        try:
            return int(value)
        except Exception as e:
            msg = 'Value "{0}" cannot be converted to an integer.'
            msg = msg.format(value)

            raise AttributeKindValueProcessingError(msg, inner_error=e)

    @staticmethod
    def validate_value(value, **type_properties):
        minimum = type_properties.get('minimum')
        minimum = int(minimum) if minimum else None

        maximum = type_properties.get('maximum')
        maximum = int(maximum) if maximum else None

        if minimum is not None and value < minimum:
            msg = 'Value out of bounds: value "{0}" < minimum "{1}"'
            msg = msg.format(value, minimum)

            raise AttributeKindValueValidationError(msg)

        if maximum is not None and value > maximum:
            msg = 'Value out of bounds: value "{0}" > maximum "{1}"'
            msg = msg.format(value, maximum)

            raise AttributeKindValueValidationError(msg)

    @staticmethod
    def filter_value(cls, value, **filter_params):
        result = True

        for symbol, op in _filter_tests:
            try:
                op_param = filter_params[symbol]
            except KeyError:
                pass
            else:
                result = op(value, op_param)

        return result
