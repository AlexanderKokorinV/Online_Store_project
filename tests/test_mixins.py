from typing import Any

from src.classes import Product
from src.products import Smartphone


def test_mixin_log_output(capsys: Any) -> None:
    """Проверка работы MixinLog: печать в консоль при создании объекта"""

    Product("Sony", "Android", 100000.0, 5)  # Создаем продукт, миксин должен напечатать repr в консоль

    captured = capsys.readouterr()
    assert "Product('Sony', 'Android', 100000.0, 5)" in captured.out


def test_smartphone_mixin_log(capsys: Any) -> None:
    """Проверка, что миксин логирует создание наследников (Smartphone)"""
    Smartphone("iPhone 15", "Gray", 120000.0, 5, 3.5, "Pro", 128, "Серый")

    captured = capsys.readouterr()
    # Проверяем, что имя класса в логе подставилось верно
    assert "Smartphone('iPhone 15', 'Gray', 120000.0, 5)" in captured.out
