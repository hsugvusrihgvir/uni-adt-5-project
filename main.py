from storage import load_data, save_data
from task_statistics import get_statistics
from tasks import (
    add_task,
    assign_responsible,
    change_status,
    filter_tasks_by_category,
    find_tasks,
    get_task_status,
    remove_responsible,
    sort_tasks
)
from utils import input_date, input_int, input_yes_no


TASKS_FILE = 'data/tasks.json'


def show_tasks(tasks: list[dict]) -> None:
    """Выводит список домашних задач."""
    if not tasks:
        print('Задачи не найдены')
        return

    for task in sort_tasks(tasks):
        responsible = task['responsible_user'] or 'не назначен'
        deadline = task['deadline'] or 'не установлен'
        print(
            f"{task['id']}. {task['name']} "
            f"({task['category']}); "
            f"ответственный: {responsible}; "
            f"срок: {deadline}; "
            f"статус: {task['status']}"
        )


def main() -> None:
    """Запускает меню приложения."""
    tasks = load_data(TASKS_FILE)

    while True:
        print('\n=== Распределение домашних обязанностей ===')
        print('1. Показать задачи')
        print('2. Добавить задачу')
        print('3. Найти задачу')
        print('4. Отобрать задачи по категории')
        print('5. Проверить, назначена ли задача')
        print('6. Назначить ответственного')
        print('7. Снять ответственного')
        print('8. Изменить статус задачи')
        print('9. Показать статистику')
        print('0. Выход')

        choice = input('Выберите действие: ')

        if choice == '1':
            show_tasks(tasks)

        elif choice == '2':
            name = input('Название задачи: ')
            category = input('Категория: ')

            if add_task(tasks, name, category) is not None:
                save_data(TASKS_FILE, tasks)
                print('Задача добавлена')
            else:
                print('Название и категория не должны быть пустыми')

        elif choice == '3':
            query = input('Введите часть названия: ')
            show_tasks(find_tasks(tasks, query))

        elif choice == '4':
            category = input('Категория: ')
            filtered_tasks = list(
                filter_tasks_by_category(tasks, category)
            )
            show_tasks(filtered_tasks)

        elif choice == '5':
            task_id = input_int('Идентификатор задачи: ')
            print(get_task_status(tasks, task_id))

        elif choice == '6':
            task_id = input_int('Идентификатор задачи: ')
            user_name = input('Ответственный: ')
            deadline = input_date('Дата выполнения: ')

            if assign_responsible(
                tasks,
                task_id,
                user_name,
                deadline
            ):
                save_data(TASKS_FILE, tasks)
                print('Ответственный назначен')
            else:
                print('Задача не найдена или уже имеет ответственного')

        elif choice == '7':
            task_id = input_int('Идентификатор задачи: ')
            if remove_responsible(tasks, task_id):
                save_data(TASKS_FILE, tasks)
                print('Ответственный снят')
            else:
                print('Задача не найдена или ответственный не назначен')

        elif choice == '8':
            task_id = input_int('Идентификатор задачи: ')
            is_completed = input_yes_no('Задача выполнена? (да/нет): ')

            if change_status(tasks, task_id, is_completed):
                save_data(TASKS_FILE, tasks)
                print('Статус изменён')
            else:
                print('Сначала назначьте ответственного')

        elif choice == '9':
            statistics = get_statistics(tasks)
            print(f"Всего задач: {statistics['total']}")
            print(f"С ответственным: {statistics['assigned']}")
            print(f"Без ответственного: {statistics['unassigned']}")
            print(f"Выполнено: {statistics['completed']}")
            print(f"Не выполнено: {statistics['not_completed']}")

        elif choice == '0':
            break

        else:
            print('Неизвестная команда')


if __name__ == '__main__':
    main()
