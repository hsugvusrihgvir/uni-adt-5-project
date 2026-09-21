from collections.abc import Iterator


def add_task(
    tasks: list[dict],
    name: str,
    category: str
) -> int | None:
    """Добавляет домашнюю задачу."""
    name = name.strip()
    category = category.strip()

    if not name or not category:
        return None

    task_id = max((task['id'] for task in tasks), default=0) + 1
    tasks.append({
        'id': task_id,
        'name': name,
        'category': category,
        'responsible_user': None,
        'deadline': None,
        'status': 'Не назначена'
    })
    return task_id


def find_tasks(tasks: list[dict], query: str) -> list[dict]:
    """Ищет задачи по названию."""
    result = []

    for task in tasks:
        if query.lower() in task['name'].lower():
            result.append(task)

    return result


def find_task_by_id(tasks: list[dict], task_id: int) -> dict | None:
    """Ищет задачу по идентификатору."""
    for task in tasks:
        if task['id'] == task_id:
            return task

    return None


def filter_tasks_by_category(
    tasks: list[dict],
    category: str
) -> Iterator[dict]:
    """Отбирает задачи указанной категории."""
    return (
        task for task in tasks
        if task['category'].lower() == category.lower()
    )


def sort_tasks(tasks: list[dict]) -> list[dict]:
    """Сортирует задачи по названию."""
    return sorted(tasks, key=lambda task: task['name'].lower())


def is_task_available(tasks: list[dict], task_id: int) -> bool:
    """Проверяет, свободна ли задача."""
    task = find_task_by_id(tasks, task_id)
    return task is not None and task['responsible_user'] is None


def assign_responsible(
    tasks: list[dict],
    task_id: int,
    user_name: str,
    deadline: str
) -> bool:
    """Назначает ответственного и срок."""
    user_name = user_name.strip()

    if not user_name or not is_task_available(tasks, task_id):
        return False

    task = find_task_by_id(tasks, task_id)
    task['responsible_user'] = user_name
    task['deadline'] = deadline
    task['status'] = 'Не выполнена'
    return True


def remove_responsible(tasks: list[dict], task_id: int) -> bool:
    """Снимает ответственного с задачи."""
    task = find_task_by_id(tasks, task_id)

    if task is None or task['responsible_user'] is None:
        return False

    task['responsible_user'] = None
    task['deadline'] = None
    task['status'] = 'Не назначена'
    return True


def change_status(
    tasks: list[dict],
    task_id: int,
    is_completed: bool
) -> bool:
    """Меняет статус задачи."""
    task = find_task_by_id(tasks, task_id)

    if task is None or task['responsible_user'] is None:
        return False

    task['status'] = 'Выполнена' if is_completed else 'Не выполнена'
    return True


def get_task_status(tasks: list[dict], task_id: int) -> str:
    """Возвращает информацию об ответственном."""
    task = find_task_by_id(tasks, task_id)

    if task is None:
        return 'Задача не найдена'
    if is_task_available(tasks, task_id):
        return 'Ответственный не назначен'
    return f"Ответственный: {task['responsible_user']}"
