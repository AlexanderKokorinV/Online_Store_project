from typing import List


class Product:
    """Класс для представления продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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


class Category:
    """Класс для представления категорий"""

    category_count = 0  # Атрибут класса для подсчета категорий
    product_count = 0  # Атрибут класса для подсчета продуктов

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет товары в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер, который выводит список товаров в виде строк в заданном формате"""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт. \n"
        return result

    @property
    def products_list(self) -> List[Product]:
        """Геттер, возвращающий сам список объектов"""
        return self.__products
