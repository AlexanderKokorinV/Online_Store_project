import json
import os
from typing import List

from src.classes import Category, Product

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))  # Определяем путь к корневой папке проекта
PATH_TO_JSON_FILE = os.path.join(ROOT_DIR, "data", "products.json")  # Формируем путь к файлу operations.json


def get_data_from_json(PATH_TO_JSON_FILE: str) -> List[Category]:
    """Подгружает данные по категориям и товарам из файла JSON и создает объекты классов"""

    if not os.path.exists(PATH_TO_JSON_FILE):
        return []

    with open(PATH_TO_JSON_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for item in data:
        # 1. Создаем список объектов Product для текущей категории
        product_objects = []
        for prod_data in item.get("products", []):
            product = Product(
                name=prod_data["name"],
                description=prod_data["description"],
                price=prod_data["price"],
                quantity=prod_data["quantity"],
            )
            product_objects.append(product)

        # 2. Создаем объект Category, передавая в него список продуктов
        category = Category(name=item["name"], description=item["description"], products=product_objects)
        categories.append(category)

    return categories
