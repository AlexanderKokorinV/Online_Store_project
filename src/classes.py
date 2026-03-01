from typing import List

from src.abstracts import BaseOrder, BaseProduct
from src.mixins import MixinLog


class Product(MixinLog, BaseProduct):
    """Класс для представления продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Конструктор для продукта"""

        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.__price = price
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(
        cls, name: str, description: str, price: float, quantity: int, products_list: List["Product"]
    ) -> "Product":
        """Принимает на вход параметры товара в словаре и возвращает созданный объект класса Product"""

        for product in products_list:  # Перебираем имеющийся список товаров
            if product.name.lower() == name.lower():  # Если товар найден, суммируем количество
                product.quantity += quantity
                product.price = max(product.price, price)
                return product

        return cls(name, description, price, quantity)  # Если совпадений не найдено, создаем и возвращаем новый объект

    @property
    def price(self) -> float:
        """Геттер для атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для атрибута цены с проверкой корректности"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:  # В случае если цена товара понижается
            confirm = input(f"Вы хотите снизить цену с {self.__price} до {new_price} руб.? (y/n): ")
            if confirm.lower() == "y":
                self.__price = new_price
                print("Цена успешно снижена")
            else:
                print("Действие отменено, цена осталась прежней")
        else:
            self.__price = new_price

    def __str__(self) -> str:
        """Возвращает строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Складывает два продукта одного класса и возвращает полную стоимость всех товаров обоих видов на складе"""
        if type(self) is type(other):  # Проверяем, что объекты принадлежат строго одному и тому же классу
            return (self.price * self.quantity) + (other.price * other.quantity)

        raise TypeError  # Если типы разные, вызываем исключение


class Category(MixinLog, BaseOrder):
    """Класс для представления категорий"""

    category_count = 0  # Атрибут класса для подсчета категорий
    product_count = 0  # Атрибут класса для подсчета продуктов

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        """Конструктор для категории"""

        self.name = name
        self.description = description
        self.__products = products

        super().__init__(name, description, 0.0, len(products))

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Строковое отображение категории"""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity

        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет товары в категорию. Проверяет, является ли объект экземпляром класса Product или его наследником"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

        else:
            raise TypeError  # Выбрасываем ошибку типа в случае попытки добавить не продукт

    @property
    def products(self) -> str:
        """Геттер, который выводит список товаров в виде строк в заданном формате"""
        result = ""
        for product in self.__products:
            result += f"{product}\n"
        return result

    @property
    def products_list(self) -> List[Product]:
        """Геттер, возвращающий сам список объектов"""
        return self.__products

    @property
    def total_cost(self) -> float:
        """Полная стоимость всех товаров на складе в этой категории"""
        return sum(p.price * p.quantity for p in self.__products)

    @property
    def total_quantity(self) -> int:
        """Суммарное количество всех единиц товара в категории"""
        return sum(p.quantity for p in self.__products)

    def middle_price(self) -> float:
        """Подсчитывает средний ценник всех товаров в категории. В случае исключений возвращает ноль"""
        try:
            total_sum = sum(product.price for product in self.__products) # Считаем сумму цен всех уникальных товаров
            middle_price = total_sum / len(self.__products) # Делим на количество наименований (объектов в списке)
            return round(middle_price, 2)

        except ZeroDivisionError:
            return 0.0 # Если список пуст, возвращаем ноль


