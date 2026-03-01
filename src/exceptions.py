class ZeroQuantityError(Exception):
    """Исключение для товаров с нулевым количеством"""

    def __init__(self, message: str = "Товар с нулевым количеством не может быть добавлен") -> None:
        self.message = message
        super().__init__(self.message)
