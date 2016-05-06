from .errors import AttributeKindValueProcessingError
from ._string_kind import StringKind


class FormattedStringKind(StringKind):
    @staticmethod
    def process_value(value, **type_properties):
        formatter = type_properties.get('formatter')
        formatter = str(formatter).strip().format if formatter else formatter

        if formatter:
            try:
                result = formatter(**value)
            except Exception as e:
                msg = 'Value "{0}" does not conform to format "{0}".'
                msg = msg.format(value, formatter)

                raise AttributeKindValueProcessingError(msg, inner_error=e)
        else:
            msg = 'Invalid formatter: "{0}"'
            msg = msg.format(formatter)

            raise AttributeKindValueProcessingError(msg)

        return result
