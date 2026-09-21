import json


def load_data(filename: str) -> list[dict]:
    """Загружает данные из JSON-файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    except (OSError, json.JSONDecodeError):
        print('Не удалось загрузить данные')
        return []


def save_data(filename: str, data: list[dict]) -> bool:
    """Сохраняет данные в JSON-файл."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return True
    except OSError:
        print('Не удалось сохранить данные')
        return False
