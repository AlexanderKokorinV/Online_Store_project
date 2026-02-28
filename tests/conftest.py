import pytest

from src.classes import Category, Product


@pytest.fixture
def product_iphone() -> Product:
    """Фикстура для тестирования инициализации товара iPhone"""
    return Product("iPhone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_samsung() -> Product:
    """Фикстура для тестирования инициализации товара Samsung"""
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture(autouse=True)
def clean_category_counters() -> None:
    """Автоматически очищает счетчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0
