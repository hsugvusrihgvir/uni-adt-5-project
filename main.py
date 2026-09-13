from datetime import date, timedelta

task_name = "помыть пол"
category = "уборка"

responsible_user = ""
deadline = None
status = "не назначена"

# назначить ответственного
def assign_responsible(user_name):
    if user_name != "":
        print("Ответственный назначен")
        return user_name
    return "Ответственный не назначен"

# установить дедлайн
def set_deadline(days):
    days = int(days)
    return date.today() + timedelta(days=days)

# поменять статус
def change_status(is_completed):
    if is_completed:
        return "Выполнена"
    return "Не выполнена"


responsible_user = assign_responsible("Даша")
deadline = set_deadline('3')
status = change_status(False)


print(f"Задача: {task_name}")
print(f"Категория: {category}")
print(f"Ответственный: {responsible_user}")
print(f"Срок выполнения: {deadline}")
print(f"Статус: {status}")