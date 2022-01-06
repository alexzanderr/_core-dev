
import pytest
from _core.algorithms import float_eq
from _core.algorithms import greatest_common_divisor as gcd



@pytest.mark.parametrize("x, y", [
    (.1 *3, .3),
])
def test_float_eq_returns_true(x: float, y: float):
    assert float_eq(x, y) == True


@pytest.mark.parametrize("x, y", [
    (.1 * 3, .4)
])
def test_float_eq_returns_false(x: float, y: float):
    assert float_eq(x, y) == False


@pytest.mark.parametrize("x, y, expected_result", [
    (1, 1, 1),
])
def test_gcd(x: int, y: int, expected_result: int):
    assert gcd(x, y) == expected_result