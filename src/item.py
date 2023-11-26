import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[0: 10]

    @classmethod
    def instantiate_from_csv(cls, filename):
        cls.all.clear()
        with open(filename) as file:
            items = csv.DictReader(file)
            for item in items:
                name = item.get('name')
                price = item.get('price')
                quantity = item.get('quantity')
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str):
        return int(float(value))

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'









