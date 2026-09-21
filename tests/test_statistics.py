from task_statistics import get_statistics


def test_statistics():
    tasks = [
        {
            'id': 1,
            'responsible_user': 'Даша',
            'status': 'Выполнена'
        },
        {
            'id': 2,
            'responsible_user': None,
            'status': 'Не назначена'
        }
    ]
    result = get_statistics(tasks)
    assert result['total'] == 2
    assert result['assigned'] == 1
    assert result['completed'] == 1
