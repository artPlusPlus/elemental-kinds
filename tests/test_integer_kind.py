import inspect
import pytest

from elemental_kinds import IntegerKind
from elemental_kinds.errors import (
    AttributeKindValueProcessingError,
    AttributeKindValueValidationError
)


class _IntegerKindProcessParams(object):
    values = [
        ('-123', -123),
        (456, 456),
        (None, AttributeKindValueProcessingError),
        (True, 1),
        (False, 0)
    ]


@pytest.mark.parametrize('value', _IntegerKindProcessParams.values)
def test_integer_kind_process_value(value):
    test_value, expected_value = value
    if inspect.isclass(expected_value) and issubclass(expected_value, Exception):
        with pytest.raises(expected_value):
            IntegerKind.process_value(value)
    else:
        IntegerKind.process_value(test_value) == expected_value


class _IntegerKindValidateParams(object):
    values = [
        0
    ]
    params = [
        ({}, True),
        (
            {
                'minimum': 0,
            },
            True
        ),
        (
            {
                'maximum': 0,
            },
            True
        ),
        (
            {
                'minimum': -1,
                'maximum': 1
            },
            True
        ),
        (
            {
                'minimum': 1,
            },
            AttributeKindValueValidationError
        ),
        (
            {
                'maximum': -1,
            },
            AttributeKindValueValidationError
        )
    ]


@pytest.mark.parametrize('value', _IntegerKindValidateParams.values)
@pytest.mark.parametrize('params', _IntegerKindValidateParams.params)
def test_integer_kind_validate_value(value, params):
    test_params, expected_result = params

    if inspect.isclass(expected_result) and issubclass(expected_result, Exception):
        with pytest.raises(expected_result):
            IntegerKind.validate_value(value, **test_params)
    else:
        IntegerKind.validate_value(value, **test_params)
