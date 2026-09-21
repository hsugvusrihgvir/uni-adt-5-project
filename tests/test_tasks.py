from tasks import (
    add_task,
    assign_responsible,
    change_status,
    filter_tasks_by_category,
    find_tasks,
    is_task_available,
    remove_responsible,
    sort_tasks
)


def make_task() -> dict:
    return {
        'id': 1,
        'name': 'Помыть пол',
        'category': 'Уборка',
        'responsible_user': None,
        'deadline': None,
        'status': 'Не назначена'
    }


def test_add_task():
    tasks = []
    add_task(tasks, 'Помыть посуду', 'Кухня')
    assert len(tasks) == 1
    assert tasks[0]['responsible_user'] is None


def test_empty_task_is_not_added():
    tasks = []
    assert add_task(tasks, '', 'Уборка') is None
    assert tasks == []


def test_find_tasks():
    tasks = [
        {
            'id': 1,
            'name': 'Помыть пол',
            'category': 'Уборка'
        }
    ]
    assert find_tasks(tasks, 'пол')


def test_sort_tasks():
    tasks = [
        {'id': 1, 'name': 'Помыть пол', 'category': 'Уборка'},
        {'id': 2, 'name': 'Вынести мусор', 'category': 'Уборка'}
    ]
    assert sort_tasks(tasks)[0]['name'] == 'Вынести мусор'


def test_filter_tasks_by_category():
    tasks = [
        {'id': 1, 'name': 'Помыть пол', 'category': 'Уборка'},
        {'id': 2, 'name': 'Приготовить ужин', 'category': 'Готовка'}
    ]
    result = list(filter_tasks_by_category(tasks, 'Уборка'))
    assert len(result) == 1


def test_assign_and_remove_responsible():
    tasks = [make_task()]
    assert is_task_available(tasks, 1)
    assert assign_responsible(tasks, 1, 'Даша', '2026-09-23')
    assert not is_task_available(tasks, 1)
    assert remove_responsible(tasks, 1)
    assert is_task_available(tasks, 1)


def test_task_cannot_be_assigned_twice():
    tasks = [make_task()]
    assign_responsible(tasks, 1, 'Даша', '2026-09-23')
    assert not assign_responsible(tasks, 1, 'Иван', '2026-09-24')


def test_change_status():
    tasks = [make_task()]
    assign_responsible(tasks, 1, 'Даша', '2026-09-23')
    assert change_status(tasks, 1, True)
    assert tasks[0]['status'] == 'Выполнена'
