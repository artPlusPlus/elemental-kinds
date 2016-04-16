import re

from .errors import (
    AttributeKindValueProcessingError,
    AttributeKindValueValidationError
)
from ._attribute_kind import AttributeKind


class StringKind(AttributeKind):
    @staticmethod
    def process_value(value, **type_properties):
        try:
            result = str(value)
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
