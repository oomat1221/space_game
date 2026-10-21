task_list = []

list={
    'id': 1,
    'title': 'Python',
    'description': 'Сделать домашку по Python',
    'status': 'новая'
}


def add_task(title, description):
    task = {
        "id": len(task_list) + 1,
        "title": title,
        "description": description,
        "status": "новая"
    }
    task_list.append(task)
    return task

while True:
    print("\n=== Менеджер задач ===")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Изменить задачу")
    print("4. Удалить задачу")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        task = add_task(title, description)
        print(f"Задача '{task['title']}' добавлена с ID {task['id']}.")

    elif choice == "2":
        if not task_list:
            print("Список задач пуст.")
        else:
            print("\nСписок задач:")
            for task in task_list:
                print(f"ID: {task['id']}, Название: {task['title']}, Описание: {task['description']}, Статус: {task['status']}")

    elif choice == "3":
        task_id = int(input("Введите ID задачи для изменения : "))
        for task in task_list:
            if task['id'] == task_id:
                new_title = input("Введите новое название задачи: ")
                new_description = input("Введите новое описание задачи: ")
                task['title'] = new_title
                task['description'] = new_description
                print(f"Задача '{task['title']}' изменена.")

                break
        else:
            print("Задача с указанным ID не найдена.")

    elif choice == "4":
        task_id = int(input("Введите ID задачи для удаления: "))
        for task in task_list:
            if task['id'] == task_id:
                task_list.remove(task)
                print(f"Задача '{task['title']}' удалена.")
                break
        else:
            print("Задача с указанным ID не найдена.")

    elif choice == "5":
        print("Выход из программы.")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")