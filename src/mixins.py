from typing import Any


class MixinLog:
    """Миксин для логирования создания объекта"""

    name: str  # Прописываем аннотации типов
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int, **kwargs: Any) -> None:
        """Вызывает инициализацию родителя (BaseProduct)"""
        super().__init__(
            name, description, price, quantity, **kwargs
        )  # Инициализируем объект через родительские классы

        print(repr(self))  # Выводим в консоль

    def __repr__(self) -> str:
        """Возвращает строковое представление класса с параметрами"""
        attributes = []
        # Собираем основные атрибуты, которые есть у всех продуктов
        for value in [self.name, self.description, self.price, self.quantity]:
            attributes.append(f"'{value}'" if isinstance(value, str) else str(value))

        return f"{self.__class__.__name__}({', '.join(attributes)})"
