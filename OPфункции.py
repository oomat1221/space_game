
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









# univer=[]
# technikum=[]
# army=[]
# married=[]

# abiturients = [
#     {'name': 'Igor', 'ОРТ':110, 'gender': 'male'},
#     {'name': 'Alina', 'ОРТ': 120, 'gender': 'female'},
#     {'name': 'Igor', 'ОРТ': 110, 'gender': 'male'},
#     {'name': 'Akylai', 'ОРТ': 40, 'gender': 'female'},
#     {'name': 'Ivan', 'ОРТ': 50, 'gender': 'male'},
#     {'name': 'Aizika', 'ОРТ': 30, 'gender': 'female'},
#     {'name': 'Aleksey', 'ОРТ': 90, 'gender': 'male'},
#     {'name': 'Igor', 'ОРТ':110, 'gender': 'male'},
#     {'name': 'Abbas', 'ОРТ': 80, 'gender': 'male'},
# ]

# def all_abid(lst):
#     for i in lst:
        


# selection(abiturients)



# def menu(**kwargs):
#     return f'Меню ресторана: {kwargs}'

# result = menu(breakfast = 'Яичница', lunch = 'Борщ', dinner = 'Плов')

# print(result)





# def result_temp_kg(*args):
#      return f'СР значение температуры в Кыргызстане на сегодня: {round(sum(args)/len(args), 2)} градусов по Цельсию'


# result = result_temp_kg(float(input('Введите температуру в городе Иссык-Куль: ')), 
#                         float(input('Введите температуру в городе Чуй: ')), 
#                         float(input('Введите температуру в городе Ош: '))
#                         )

# print(result)




#НЕ РАБОТАЕТ
# def result_temp_kg(*args):
#     return f'СР значение температуры в Кыргызстане на сегодня: {sum(args)/len(args)} градусов по Цельсию'

# issyk_kul = result_temp_kg(float(input('Введите температуру в городе Иссык-Куль: ')))
# chui = result_temp_kg(float(input('Введите температуру в городе Чуй: ')))
# osh = result_temp_kg(float(input('Введите температуру в городе Ош: ')))

# print(float(result_temp_kg(issyk_kul, chui, osh)))






# def students_stipends(name="Иван", stipend=1000):
#     return f'Студент {name} получает стипендию в размере {stipend} сомов'
# result = students_stipends(name = 'Алексей', stipend = 1500)
# print(result)





# def greeting(name):
#     return f'Дарова {name}!'

# result = greeting(str(input('Как тебя зовут? ')))
# print(result)




# def summa(a,b):
#     return f'{a} + {b} = {a + b}'
    
# result = summa(a=5, b=10)
# print(result)