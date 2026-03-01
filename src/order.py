from src.abstracts import BaseOrder
from src.mixins import MixinLog
from src.classes import Product

class Order(MixinLog, BaseOrder):
    """Класс для представления заказа на один товар"""

    def __init__(self, product: Product, quantity: int) -> None:
        """Конструктор для инициализации заказа"""

        if not isinstance(product, Product):
            raise TypeError # Заказ можно оформить только на объект класса Product или его наследников

        self.__product = product
        self.name = product.name
        self.quantity = quantity

        super().__init__(
            name = self.name,
            quantity = self.quantity
        )


    @property
    def total_cost(self) -> float:
        """Итоговая стоимость заказа"""
        return self.__product.price * self.quantity

    @property
    def total_quantity(self) -> int:
        """Количество купленного товара"""
        return self.quantity

    def __str__(self) -> str:
        """Строковое отображение заказа"""
        return f"Заказ: {self.__product.name}, {self.quantity} шт. Итого: {self.total_cost} руб."



