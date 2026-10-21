
while 1:
    try:
        symbols = ['+', '-', '*', '/']
        number_1 = float(input('Введите первое число: '))
        operation = str(input('Введите операцию: + - * / '))
        if operation not in symbols:
            raise ValueError("Неверная операция!")
        number_2 = float(input('Введите второе число: '))

        if number_1 and number_2 != type(float):
            print("Неверный ввод чисел!")


        if operation == '+':
            print(f'{number_1} + {number_2} = {number_1 + number_2}')
        elif operation == '-':
            print(f'{number_1} - {number_2} = {number_1 - number_2}')
        elif operation == '*':
            print(f'{number_1} * {number_2} = {number_1 * number_2}')
        elif operation == '/':
            if number_2 == 0:
                print("Ошибка! Деление на ноль!")
            else:
                print(f'{number_1} / {number_2} = {number_1 / number_2}')
        print('-'*40)
    except ValueError:
        print("Ошибка! Введите корректные данные!")
        print('-'*40)
        continue








# try:
#     age = int(input("Введите возраст: "))

# except ValueError:
#     print("Нужно ввести число!")


# try:
#     age = int(input("Введите возраст: "))
#     print(age)

# except:
#     print("Ошибка!")






# temp_1 = float(input('Какая температура воздуха в Чуйской области?'))
# temp_2 = float(input('Какая температура воздуха в Нарынской области?'))
# temp_3 = float(input('Какая температура воздуха в Баткенской области?'))
# temp_4 = float(input('Какая температура воздуха в Талаской области?'))
# temp_5 = float(input('Какая температура воздуха в Джалал-Абадской области?'))
# temp_6 = float(input('Какая температура воздуха в Ошской области?'))
# temp_7 = float(input('Какая температура воздуха в Ысык-Кульской области?'))
# name = int('7')

# res = (temp_1+temp_2+temp_3+temp_4+temp_5+temp_6+temp_7)/name
# res_float = round (res, 2)

# print(f'Средняя температура воздуха в кр {res_float}')

# balance = 1000
# spend = 0

# while True:
#     print("\n1 — Хлеб (50 сом)")
#     print("2 — Молоко (80 сом)")
#     print("3 — Шоколад (150 сом)")
#     print("4 — Остаток")
#     print("0 — Выйти")

#     choice = input("Выберите пункт: ")

#     if choice == "1":
#         price = 50
#         name = "Хлеб"
#     elif choice == "2":
#         price = 80
#         name = "Молоко"
#     elif choice == "3":
#         price = 150
#         name = "Шоколад"
#     elif choice == "4":
#         print("Остаток:", balance)
#         continue
#     elif choice == "0":
#         break
#     else:
#         print("Неверный пункт")
#         continue

#     if balance >= price:
#         balance -= price
#         spent += price
#         print(f"{name} куплен. Остаток: {balance}")
#     else:
#         print("Недостаточно денег")

# print("Вы потратили:", spent)
# print("Осталось:", balance)






# data_types =  ['ivan, 12, True, False'] 

# print(data_types)

# names = ('John', 'Alice', 'Bob', 'Eve', 'Charlie')
# names_list = list(names)
# names_list.append('David')
# names_list.remove('Eve')
# names_list.insert(3, 'Frank')
# names = tuple(names_list)
# print(names)

# data_types = (3.14, 5, 67, 'l', 'o', 'l', True,)

# letters = []
# numbers = []

# for i in data_types:
#     if type(i) == str:
#         letters.append(i)
#     else:
#         numbers.append(i)


# print(letters)
# print("-"*5)
# print(numbers)






