"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest
@pytest.fixture
def test_class():
    return Item("Смартфон", 10000, 20)


def test_func(test_class):
    assert test_class.name == "Смартфон"
    assert test_class.price == 10000
    assert test_class.quantity == 20

