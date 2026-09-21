from storage import load_data, save_data


def test_save_and_load_data(tmp_path):
    filename = tmp_path / 'tasks.json'
    tasks = [{'id': 1, 'name': 'Помыть пол'}]

    assert save_data(filename, tasks)
    assert load_data(filename) == tasks


def test_missing_file_returns_empty_list(tmp_path):
    assert load_data(tmp_path / 'missing.json') == []


def test_broken_json_returns_empty_list(tmp_path):
    filename = tmp_path / 'tasks.json'
    filename.write_text('{', encoding='utf-8')

    assert load_data(filename) == []
