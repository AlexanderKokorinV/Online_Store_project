import json
from unittest.mock import mock_open, patch

from src.classes import Category
from src.utils import get_data_from_json


def test_get_data_from_json() -> None:
    """Тест загрузки данных из JSON файла"""

    # 1. Подготавливаем mock-данные
    mock_data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {"name": "iPhone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
            ],
        }
    ]

    # Превращаем в строку
    json_string = json.dumps(mock_data)

    # 2. Патчим 'builtins.open' и 'os.path.exists'
    with patch("builtins.open", mock_open(read_data=json_string)):
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True

            result = get_data_from_json("mock_path.json")

    # 3. Проверки
    assert len(result) == 1
    assert result[0].name == "Смартфоны"
    assert "iPhone 15" in result[0].products
    assert "Samsung Galaxy C23 Ultra" in result[0].products
    assert len(result[0].products.strip().split('\n')) == 2

    # 4. Проверка работы счетчиков внутри классов
    assert Category.category_count == 1
    assert Category.product_count == 2
