from typing import List


class Product:
    """Класс для представления продуктов"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категорий"""
    name: str
    description: str
    products: List[Product]
    category_count = 0 # Атрибут класса для подсчета категорий
    product_count = 0 # Атрибут класса для подсчета продуктов

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)









