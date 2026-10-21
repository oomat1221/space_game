



#Задание 2

# data_tuple = ('h', 6.13, 'C', ['e', 'T'], True, 'k', 'e', '3', 'e', 1, ('g', 'x'), False)

# letters = []
# numbers = []


# for i in data_tuple:

#     if isinstance(i, (list, tuple)):
#         for x in i:
#             letters.append(x)

#     elif isinstance(i, bool):
#         letters.append(i)

#     elif isinstance(i, (int, float)):
#         numbers.append(i)

#     elif isinstance(i, str):
#         if i.isdigit():
#             numbers.append(int(i))
#         else:
#             letters.append(i)


# if 6.13 in numbers:
#     numbers.remove(6.13)



# for x in letters[:]:
#     if isinstance(x, bool):
#         letters.remove(x)
#         letters.append(x)


# i3 = numbers.index(3)
# i1 = numbers.index(1)

# if i3 < i1:
#     numbers.insert(i3 + 1, 2)
# else:
#     numbers.insert(i1 + 1, 2)


# numbers.sort(reverse=True)

# letters = letters[::-1]


# for i in range(len(letters)):
#     if isinstance(letters[i], str):
#         letters[i] = letters[i].swapcase()



# word = ['C', 'h', 'e', 'e', 't', 'a', 'h']


# for x in letters:
#     if isinstance(x, bool):
#         word.append(x)

# print("numbers:", numbers)
# print("letters:", letters)
# print("Итог:", word)

#Задание 1

# flags = {
#     'ru': {'red', 'blue', 'white'},
#     'kg': {'red', 'yellow'},
#     'ua': {'blue', 'yellow'},
#     'uk': {'yellow', 'blue', 'red'},
#     'kz': {'blue', 'yellow'},
    
#     'us': {'red', 'blue', 'white'},
#     'de': {'black', 'red', 'yellow'},
#     'fr': {'blue', 'white', 'red'}
# }

# while True:
#     color1 = input("Введите первый цвет | (или finish для завершения): ")
    
#     if color1 == "finish":
#         break

#     color2 = input("Введите второй цвет: ")

#     if color2 == "finish":
#         break

#     print("Подходящие домены:")

#     for domain, colors in flags.items():
#         if color1 in colors and color2 in colors:
#             print(domain)








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
#         spend += price
#         print(f"{name} куплен. Остаток: {balance}")
#     else:
#         print("Недостаточно денег")

# print("Вы потратили:", spend)
# print("Осталось:", balance)