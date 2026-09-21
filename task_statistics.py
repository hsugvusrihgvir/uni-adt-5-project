def get_statistics(tasks: list[dict]) -> dict:
    """Считает статистику по задачам."""
    assigned = 0
    completed = 0

    for task in tasks:
        if task['responsible_user'] is not None:
            assigned += 1
        if task['status'] == 'Выполнена':
            completed += 1

    return {
        'total': len(tasks),
        'assigned': assigned,
        'unassigned': len(tasks) - assigned,
        'completed': completed,
        'not_completed': assigned - completed
    }
