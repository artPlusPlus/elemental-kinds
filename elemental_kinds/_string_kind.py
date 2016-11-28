import re

from .errors import (
    AttributeKindValueProcessingError,
    AttributeKindValueValidationError
)
from ._attribute_kind import AttributeKind


class StringKind(AttributeKind):
    @staticmethod
    def process_value(value, **type_properties):
        do_lower = type_properties.get('lower', False)
        do_upper = type_properties.get('upper', False)

        try:
            result = str(value)
            result = result.lower() if do_lower else result
            result = result.upper() if do_upper else result
        except Exception as e:
            msg = 'Failed to process value "{0}" into a string: {1}'
            msg = msg.format(value, e)

            raise AttributeKindValueProcessingError(msg, inner_error=e)

        return result

    @staticmethod
    def validate_value(value, **type_properties):
        expr = type_properties.get('regex')
        if expr and not re.match(expr, value):
            msg = 'Value "{0}" does not conform to expression "{1}".'
            msg = msg.format(value, expr)

            raise AttributeKindValueValidationError(msg)

    @staticmethod
    def filter_value(value, **filter_params):
        result = True

        try:
            expr = filter_params['match']
        except KeyError:
            pass
        else:
            result = bool(re.match(expr, value))

        try:
            expr = filter_params['search']
        except KeyError:
            pass
        else:
            result = bool(re.search(expr, value))

        try:
            expr = filter_params['contains']
        except KeyError:
            pass
        else:
            result = expr in value

        return result
