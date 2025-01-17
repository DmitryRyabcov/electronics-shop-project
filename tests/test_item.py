"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest
from src.phone import Phone


@pytest.fixture
def test_class():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def test_class2():
    return  Phone("iPhone 14", 120_000, 5, 2)


def test_func(test_class):
    assert test_class.name == "Смартфон"
    assert test_class.price == 10000
    assert test_class.quantity == 20

def test_price(test_class):
    pay_rate = 0.8
    assert test_class.price * Item.pay_rate == 8000.0

def test_total_price(test_class):
    assert test_class.price * test_class.quantity == 200000

def test_name(test_class):
    assert len(test_class.name) < 10

def test_instantiate():
    Item.instantiate_from_csv('../src/items.csv')  # создание объектов из данных файла
    print(len(Item.all))
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test__repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test__str__():
    item1 = Item('Смартфон', 10000, 20)
    assert str(item1) == 'Смартфон'

def test_phone(test_class, test_class2):
    assert str(test_class2) == 'iPhone 14'
    assert repr(test_class2) == "Phone('iPhone 14', 120000, 5, 2)"
    assert test_class + test_class2 == 25
    assert test_class2 + test_class2 == 10

