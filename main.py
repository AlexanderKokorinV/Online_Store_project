from src.classes import Category, Product
from src.utils import PATH_TO_JSON_FILE, get_data_from_json

def main():
    categories = get_data_from_json(PATH_TO_JSON_FILE)

    if not categories:
        print("Данные не загружены.")
        return

    # 1. Выводим список товаров первой категории через геттер
    first_category = categories[0]
    print(f"--- Категория: {first_category.name} ---")
    print(first_category.products)

    # 3. Создание нового товара через new_product и добавление в категорию
    print("--- Добавление нового товара через new_product ---")

    # Создаем/обновляем товар (используя данные, которых нет в JSON)
    new_prod_data = {
        "name": "Sony",
        "description": "XRay",
        "price": 15000.0,
        "quantity": 10
    }


    current_list = first_category.products_list

    new_obj = Product.new_product(
        name=new_prod_data["name"],
        description=new_prod_data["description"],
        price=new_prod_data["price"],
        quantity=new_prod_data["quantity"],
        products_list=current_list
    )

    # Добавляем в категорию, если это новый объект
    if new_obj not in current_list:
        first_category.add_product(new_obj)

    print("\n--- Список товаров после обновления ---")
    print(first_category.products)

    # 4. Запрос на изменение цены у загруженного товара в случае, если она ниже старой цены
    print("--- Запрос на изменение цены загруженного товара ---")
    some_product = current_list[0]
    some_product.price = some_product.price * 0.5  # Пробуем снизить на 50%




if __name__ == "__main__":
    main()
