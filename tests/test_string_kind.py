import uuid
import inspect
import pytest

from elemental_kinds import StringKind
from elemental_kinds.errors import (
    AttributeKindValueProcessingError,
    AttributeKindValueValidationError
)


_uuid_value = uuid.uuid4()
_formatter = 'test_{'


class _StringKindProcessParams(object):
    values = [
        (None, 'None'),
        (True, 'True'),
        (False, 'False'),
        (object(), str(object)),
        (_uuid_value, str(_uuid_value)),
    ]


@pytest.mark.parametrize('value', _StringKindProcessParams.values)
def test_string_kind_no_format_process_value(value):
    test_value, expected_value = value
    if inspect.isclass(expected_value) and issubclass(expected_value, Exception):
        with pytest.raises(expected_value):
            StringKind.process_value(value)
    else:
        StringKind.process_value(test_value) == expected_value


class _StringKindValidateParams(object):
    values = [
        'pass'
    ]
    params = [
        ({}, True),
        (
            {
                'regex': '.*',
            },
            True
        ),
        (
            {
                'regex': 'foo',
            },
            AttributeKindValueValidationError
        )
    ]


@pytest.mark.parametrize('value', _StringKindValidateParams.values)
@pytest.mark.parametrize('params', _StringKindValidateParams.params)
def test_integer_kind_validate_value(value, params):
    test_params, expected_result = params

    if inspect.isclass(expected_result) and issubclass(expected_result, Exception):
        with pytest.raises(expected_result):
            StringKind.validate_value(value, **test_params)
    else:
        StringKind.validate_value(value, **test_params)
