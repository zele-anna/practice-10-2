import pytest

from src.utils import calculate_taxes


@pytest.fixture
def prices_list():
    return [1.0, 100.0, 10.0]

@pytest.mark.parametrize("my_list, rate, expected", [
    ([1.0, 100.0, 10.0], 10, [1.1, 110.0, 11.0]),
    ([2.0, 200.0, 20.0], 10, [2.2, 220.0, 22.0]),
    ([2.0, 200.0, 20.0], 20, [2.4, 240.0, 24.0])
])
def test_calc_tax(my_list, rate, expected):
    assert calculate_taxes(my_list, rate) == expected

def test_calculate_taxes(prices_list):
    assert calculate_taxes(prices_list, 10.0) == [1.1, 110.0, 11.0]


def test_calculate_tax_zero_tax(prices_list):
    assert calculate_taxes(prices_list, 0) == [1.0, 100.0, 10.0]


def test_calculate_tax_empty_list():
    assert calculate_taxes([], 10) == []


def test_calculate_tax_neg_price():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([-3.0, 5.1, 6.7], 10)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Неверная цена"


def test_calculate_tax_neg_rate():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([2.0, 5.1, 6.7], -1.1)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Неверный налоговый процент"