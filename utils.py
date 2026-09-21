from datetime import datetime


DATE_FORMAT = '%Y-%m-%d'


def input_int(prompt: str) -> int:
    """Запрашивает целое число."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Введите целое число')


def input_date(prompt: str) -> str:
    """Запрашивает дату в формате ГГГГ-ММ-ДД."""
    while True:
        value = input(prompt)
        try:
            datetime.strptime(value, DATE_FORMAT)
            return value
        except ValueError:
            print('Введите дату в формате ГГГГ-ММ-ДД')


def input_yes_no(prompt: str) -> bool:
    """Запрашивает ответ "да" или "нет"."""
    while True:
        answer = input(prompt).strip().lower()

        if answer == 'да':
            return True
        if answer == 'нет':
            return False

        print('Введите "да" или "нет"')
