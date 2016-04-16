import uuid
import inspect
import pytest

from elemental_kinds import FormattedStringKind
from elemental_kinds.errors import AttributeKindValueProcessingError

_formatter = 'test_{name}'


class _StringKindProcessParams(object):
    values = [
        (
            None,
            {},
            AttributeKindValueProcessingError
        ),
        (
            None,
            {
                'formatter': '   '
            },
            AttributeKindValueProcessingError
        ),
        (
            {'name': None},
            {
                'formatter': 'test_{name}'
            },
            'test_None'
        ),
        (
            {'name': 'Foo'},
            {
                'formatter': 'test_{name}'
            },
            'test_Foo'
        ),
        (
            {'count': 2},
            {
                'formatter': 'test_{count:2d}'
            },
            'test_02'
        ),
    ]


@pytest.mark.parametrize('value', _StringKindProcessParams.values)
def test_string_kind_no_format_process_value(value):
    test_value, test_params, expected_value = value

    if inspect.isclass(expected_value) and issubclass(expected_value, Exception):
        with pytest.raises(expected_value):
            FormattedStringKind.process_value(value, **test_params)
    else:
        result = FormattedStringKind.process_value(test_value, **test_params)
        result == expected_value
