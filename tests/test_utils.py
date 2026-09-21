from utils import input_date, input_int, input_yes_no


def test_input_int_repeats_after_error(monkeypatch):
    answers = iter(['abc', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(answers))
    assert input_int('Число: ') == 7


def test_input_date_repeats_after_error(monkeypatch):
    answers = iter(['31.02.2026', '2026-09-23'])
    monkeypatch.setattr('builtins.input', lambda _: next(answers))
    assert input_date('Дата: ') == '2026-09-23'


def test_input_yes_no_repeats_after_error(monkeypatch):
    answers = iter(['не знаю', 'да'])
    monkeypatch.setattr('builtins.input', lambda _: next(answers))
    assert input_yes_no('Ответ: ')
