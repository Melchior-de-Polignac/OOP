import pytest

from shop import calculate_discount, calculate_tax, calculate_total


@pytest.mark.parametrize(
    "price, percent, expected",
    [(100, 0, 100.0), (100, 10, 90.0), (100, 100, 0.0), (19.99, 15, 16.99)],
)
def test_calculate_discount(price, percent, expected):
    assert calculate_discount(price, percent) == expected


@pytest.mark.parametrize("price, percent", [(-1, 10), (100, -5), (100, 101)])
def test_calculate_discount_rejects_bad_input(price, percent):
    with pytest.raises(ValueError):
        calculate_discount(price, percent)


def test_calculate_tax_default_rate():
    assert calculate_tax(50) == 10.0


def test_calculate_total_includes_tax():
    prices = [10.0, 20.0, 30.0]
    assert calculate_total(prices) == 72.0


def test_calculate_total_of_nothing_is_zero():
    assert calculate_total([]) == 0
