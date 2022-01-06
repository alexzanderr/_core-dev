

import pytest

# pip install pytest_steps
from pytest_steps.steps import test_steps

def get_total_decimals(real_number: float | str):
    if isinstance(real_number, float):
        real_number = str(real_number)

    _int, _real = real_number.split(".")
    return len(_real)

from _core._math import fixed_set_precision_str
@pytest.mark.parametrize(
    "real_number, precision, expected_result",
    # testcases
    [
        (123.123, 2, "123.12"),
        ("123.123", 2, "123.12"),
        ("123.1231111111123123123123123", 2, "123.12"),
        ("123123x.x123", 2, "123.123"),
        ("123123x.123123x", 2, "123.123"),
        (777, 2, "777.00"),
        (777.3333, 4, "777.3333"),
        ("xasd123b.x", 2, "123.123"),
        ("x.x", 2, "123.123"),
    ]
)
@test_steps(
    "correct number of decimals ?",
    "is type str ?",
    "result == expected ?"
)
def test_fixed_set_precision_str(
    real_number: float | str,
    precision: int,
    expected_result: float,
):
    try:
        # we know that this raises if the @real_number its not valid
        result = fixed_set_precision_str(real_number, precision)
        print(result)

    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)
    else:
        _decimals = get_total_decimals(result)

        # correct number of decimals ?
        assert _decimals == precision
        yield

        # is type str ?
        assert isinstance(result, str)
        yield

        # result == expected ?
        assert result == expected_result
        yield

    yield




from _core._math import fixed_set_precision_float
@pytest.mark.parametrize(
    "real_number, precision, expected_result",
    # testcases
    [
        (123.123, 2, 123.12),
        ("123.123", 2, 123.12),
        ("123.1231111111123123123123123", 2, 123.12),
        ("x.x", 2, 123.123),
        ("xasd123b.x", 2, 123.123),
        ("123123x.x123", 2, 123.123),
        ("123123x.123123x", 2, 123.123),
    ]
)
def test_fixed_set_precision_float(
    real_number: float | str,
    precision: int,
    expected_result: float
):
    try:
        # we know that this raises if the @real_number its not valid
        result = fixed_set_precision_float(real_number, precision)
    except ValueError:
        print("oops. catched exception")
    else:
        _decimals = get_total_decimals(result)
        assert _decimals == precision
        assert isinstance(result, float)
        assert result == expected_result






from _core._math import hex_to_int
@pytest.mark.parametrize(
    "hex_string, expected_result",
    # testcases
    [
        (0x000000000, 0),
        (0x0, 0),
        (0x00, 0),
        ("0x000000000", 0),
        ("0x0", 0),
        ("0x00", 0),
    ]
)
def test_hex_to_int(
    hex_string: int | str,
    expected_result: float
):

    try:
        result = hex_to_int(hex_string)
    except Exception as error:
        print(error)
        pass
    else:
        assert isinstance(result, int)
        assert result == expected_result