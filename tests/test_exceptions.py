import pytest
from src.classes import Category, Product


def test_product_init_zero_quantity() -> None:
    """Тест на создание товара с нулевым количеством вызывает ValueError"""
    # Проверяем, что выбрасывается именно ValueError с заданным сообщением
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_product_init_positive_quantity() -> None:
    """Тест того, что обычное создание товара (количество > 0) проходит без ошибок"""
    product = Product("Смартфон", "Описание", 50000.0, 10)
    assert product.quantity == 10


def test_category_average_price() -> None:
    """Тест на корректный расчет средней цены при наличии товаров"""
    p1 = Product("Товар 1", "Описание", 100.0, 5)
    p2 = Product("Товар 2", "Описание", 200.0, 10)
    category = Category("Электроника", "Описание", [p1, p2])

    assert category.middle_price() == 150.0 # (100 + 200) / 2 = 150.0


def test_category_average_price_zero_division() -> None:
    """Тест на возврат 0.0 при пустой категории (ZeroDivisionError)"""
    category = Category("Пустая категория", "Описание", [])

    assert category.middle_price() == 0.0