#Списки, кортежи, словари

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












# student = {
#     'name': 'Ivanov Ivan',
#     'age': 24,
#     True: 'education',
#     False: 123,
#     'numbers': ['0550123321', '077012321']
# }

# student['numbers'].append('234')


# #add
# student['city'] = 'Bishkek'
# student.update(car=False)

# #delete
# del student[False]

# #update
# student['age']=25
# student.update(age=30)


# print(student['numbers'])
# print(student)

# for k,v in student.items():
#     print(f'{k}-{v}')



# data_type = (3.14, 5,1,4, 'm', 'a','d', True)

# letters = []
# numbers = []

# for i in data_type:
#     if type(i) == str:
#         letters.append(i)
#     else:
#         numbers.append(i)

# letters.append('A')
# letters.reverse()

# numbers.remove(3.14)

# letters.append(numbers.pop(-1))

# numbers.append(2)
# numbers.append(3)

# numbers.sort()

# letters = tuple(letters)
# numbers = tuple(numbers)

# print(letters)
# print('-'*5)
# print(numbers)




# names = ('Naruto', 'Saskey', 'Sakura')
# names = list(names)
# names.append('Hinata')
# names = tuple(names)

# print(names)




# data_type_1 = [1,2,3,4,5,6,7]
# data_type_2 = ['J.Sean', 'FloRida', '50 Cent', 'Kesha']

# data_type_2.append(data_type_1.pop(4))


#Расширение списка другим списком
#data_type_1.extend(data_type_2)

# print(data_type_2)







# data_types = ['Ivanov', 23, True, 33.44, False, 33, 'Ivan']

# #add
# data_types.append('Radomir')
# #add 2
# data_types.insert(0, 'Iphone')
# #delete
# data_types.remove(23)
# del data_types[0]
# data_types[-2] = 'Dean W.'


#print(data_types)




# student = {
#     'name': 'Ivanov Ivan',
#     'age': 24,
#     True: 'education',
#     False: 123,
#     'numbers': ['0550123321', '077012321']
# }

# student['numbers'].append('234')


# #add
# student['city'] = 'Bishkek'
# student.update(car=False)

# #delete
# del student[False]

# #update
# student['age']=25
# student.update(age=30)


# print(student['numbers'])
# print(student)

# for k,v in student.items():
#     print(f'{k}-{v}')
