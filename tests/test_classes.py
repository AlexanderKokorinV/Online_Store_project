from src.classes import Category, Product


def test_product_init(product_iphone: Product) -> None:
    """Тест инициализации объектов класса Product"""
    assert product_iphone.name == "iPhone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_category_init(product_iphone: Product, product_samsung: Product) -> None:
    """Тест инициализации категории и подсчета товаров в ней"""

    products = [product_iphone, product_samsung]
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        products,
    )

    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(category.products) == 2
    assert category.products[0].name == "iPhone 15"


def test_category_counters() -> None:
    """Тест счетчиков категорий и товаров"""

    product_1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product_4 = Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)

    category_1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [product_1, product_2, product_3],
    )
    category_2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_4],
    )

    # Проверяем, что создано 2 категории
    assert Category.category_count == 2

    # Проверяем, что общее количество товаров 4
    assert Category.product_count == 4

    assert len(category_1.products) == 3  # Проверяем, что в category_1 ровно 3 товара
    assert len(category_2.products) == 1  # Проверяем, что в category_2 ровно 1 товар
