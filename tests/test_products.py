import pytest
from src.products import Smartphone, LawnGrass
from src.classes import Category

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