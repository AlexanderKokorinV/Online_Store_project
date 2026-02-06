from src.utils import get_data_from_json, PATH_TO_JSON_FILE
from src.classes import Category

if __name__ == "__main__":
    result = get_data_from_json(PATH_TO_JSON_FILE)
    print(f"Загружено категорий: {len(result)}")
    print(f"Всего категорий в системе: {Category.category_count}")
    print(f"Всего товаров в системе: {Category.product_count}")