from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Базовый абстрактный класс, который является родительским для класса продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Обязательная инициализация для всех продуктов"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """Обязательное строковое представление для всех продуктов"""
        pass


class BaseOrder(ABC):
    """Абстрактный класс для категорий и заказов"""

    def __init__(self, name: str, description: str, price: float, quantity: int, **kwargs: Any) -> None:
        """Конструктор для инициализации категорий и заказов"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        super().__init__()

    @abstractmethod
    def __str__(self) -> str:
        """Обязательное строковое представление для всех продуктов"""
        pass

    @property
    @abstractmethod
    def total_cost(self) -> float:
        """Итоговая стоимость всех товаров в объекте"""
        pass

    @property
    @abstractmethod
    def total_quantity(self) -> int:
        """Общее количество товаров в объекте"""
        pass
