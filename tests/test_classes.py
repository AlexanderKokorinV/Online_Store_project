from typing import Any

import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


def test_product_price_setter(product_iphone: Product) -> None:
    """Тест установки корректной цены"""
    product_iphone.price = 250000.0
    assert product_iphone.price == 250000.0


def test_product_price_setter_invalid(product_iphone: Product, capsys: Any) -> None:
    """Тест установки некорректной цены (0 или отрицательная)"""
    product_iphone.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_iphone.price == 210000.0  # Цена не изменилась


def test_product_price_reduction_confirm(product_iphone: Product, monkeypatch: Any) -> None:
    """Тест подтверждения снижения цены (ввод 'y')"""
    # Симулируем ввод 'y' в терминал
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product_iphone.price = 150000.0
    assert product_iphone.price == 150000.0


def test_product_price_reduction_reject(product_iphone: Product, monkeypatch: Any) -> None:
    """Тест отмены снижения цены (ввод 'n')"""
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product_iphone.price = 150000.0
    assert product_iphone.price == 210000.0  # Осталась старой


def test_new_product_merge(product_iphone: Product) -> None:
    """Тест создания товара с объединением дублей (регистронезависимо)"""
    products_list = [product_iphone]
    # Добавляем такой же айфон, но дороже и в другом регистре
    new_obj = Product.new_product("IPHONE 15", "Space Gray", 300000.0, 2, products_list)

    assert new_obj.quantity == 10  # 8 + 2
    assert new_obj.price == 300000.0  # Выбрана максимальная
    assert len(products_list) == 1  # Новый объект не создался в списке


def test_category_products_format(product_iphone: Product) -> None:
    """Тест строкового представления товаров в категории через геттер"""
    category = Category("Смартфоны", "Описание", [product_iphone])
    expected_output = "iPhone 15, 210000.0 руб. Остаток: 8 шт.\n"
    assert category.products == expected_output


def test_add_product_logic(product_samsung: Product) -> None:
    """Тест метода add_product и обновления счетчика"""
    category = Category("Электроника", "...", [])
    initial_count = Category.product_count
    category.add_product(product_samsung)
    assert Category.product_count == initial_count + 1


def test_product_str(product_iphone: Product) -> None:
    """Тест строкового отображения продукта"""
    assert str(product_iphone) == "iPhone 15, 210000.0 руб. Остаток: 8 шт."


def test_category_str(product_iphone: Product, product_samsung: Product) -> None:
    """Тест строкового отображения категории"""
    category = Category("Смартфоны", "Описание", [product_iphone, product_samsung])

    # iPhone (8 шт) + Samsung (5 шт) = 13 шт.
    assert str(category) == "Смартфоны, количество продуктов: 13 шт."


def test_product_add() -> None:
    """Тест сложения двух продуктов (полная стоимость склада)"""
    p1 = Product("Samsung", "Android", 100.0, 10)  # 100 * 10 = 1000
    p2 = Product("iPhone", "iOS", 200.0, 2)  # 200 * 2 = 400

    assert p1 + p2 == 1400.0


def test_category_products_getter_with_str(product_iphone: Product) -> None:
    """Тест геттера products в Category на использование __str__ продукта"""
    category = Category("Тест", "Описание", [product_iphone])

    # Геттер должен вернуть строку, сформированную через __str__ продукта
    expected_output = "iPhone 15, 210000.0 руб. Остаток: 8 шт.\n"
    assert category.products == expected_output


def test_smartphone_init() -> None:
    """Тест инициализации смартфона со специфичными атрибутами"""
    iphone = Smartphone("iPhone 15", "Gray", 120000.0, 5, 3.5, "Pro Max", 512, "Серый")
    assert iphone.name == "iPhone 15"
    assert iphone.efficiency == 3.5
    assert iphone.model == "Pro Max"
    assert iphone.memory == 512
    assert iphone.color == "Серый"


def test_lawn_grass_init() -> None:
    """Тест инициализации газонной травы"""
    grass = LawnGrass("Газонная трава", "Зеленый газон", 500.0, 20, "Австрия", "14 дней", "Ярко-зеленый")
    assert grass.name == "Газонная трава"
    assert grass.country == "Австрия"
    assert grass.germination_period == "14 дней"


def test_add_product_validation() -> None:
    """Тест защиты метода add_product от некорректных типов"""
    category = Category("Смартфоны", "Телефоны", [])
    iphone = Smartphone("iPhone 15", "Новый", 120000.0, 5, 3.5, "Pro", 128, "Gray")

    # Успешное добавление наследника
    category.add_product(iphone)
    assert len(category.products_list) == 1

    # Ошибка при добавлении строки вместо объекта Product
    with pytest.raises(TypeError):
        category.add_product("Not a product")


def test_product_add_strict_type_check() -> None:
    """Тест сложения: только объекты одного и того же класса"""
    iphone = Smartphone("iPhone 15", "Новый", 1000.0, 2, 3.5, "Pro", 128, "Gray")
    pixel = Smartphone("Pixel 8", "Новый", 800.0, 5, 3.2, "Standard", 128, "Black")

    # Складываем смартфоны (1000*2 + 800*5 = 6000)
    assert iphone + pixel == 6000.0


def test_category_str_with_subclasses() -> None:
    """Тест __str__ категории, содержащей разные подклассы продуктов"""
    iphone = Smartphone("iPhone 15", "...", 100.0, 10, 3.5, "Pro", 128, "Gray")
    grass = LawnGrass("Трава", "...", 50.0, 20, "RU", "7d", "Green")
    category = Category("Разное", "...", [iphone, grass])

    # 10 смартфонов + 20 единиц травы = 30 шт.
    assert str(category) == "Разное, количество продуктов: 30 шт."
