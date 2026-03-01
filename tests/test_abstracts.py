import pytest

from src.abstracts import BaseProduct
from src.classes import Product


def test_base_product_abc_error() -> None:
    """Проверка, что нельзя создать объект абстрактного класса BaseProduct"""
    with pytest.raises(TypeError):
        # Попытка инициализации абстрактного класса вызовет ошибку
        BaseProduct("Test", "Desc", 100.0, 5)


def test_base_product_attributes_transfer(product_iphone: Product) -> None:
    """Проверка, что атрибуты, определенные в BaseProduct, корректно доходят до наследников"""
    assert product_iphone.name == "iPhone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.quantity == 8
