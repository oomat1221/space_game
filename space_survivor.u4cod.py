
#SPACE SURVIVOR by Umar

import random

print(">>> SPACE SURVIVOR <<<")
print("Твоя задача - выжить в космосе!")

while True:
    health = 100
    shield = 1
    score = 0
    turn = 1

    print("\nНовый полет начался!")

    while health > 0:
        print("\n====================")
        print("Ход:", turn)
        print("Здоровье:", health)
        print("Щит:", shield)
        print("Очки:", score)

        print("\nЧто будешь делать?")
        print("1 - Продолжить полет")
        print("2 - Проверить корабль")
        print("3 - Закончить игру")

        try:
            choice = int(input("Твой выбор: "))
        except ValueError:
            print("Ошибка! Введи число.")
            continue

        if choice == 1:
            event = random.randint(1, 4)

            if event == 1:
                print("\nНа пути астероид!")
                print("1 - Увернуться")
                print("2 - Использовать щит")
                print("3 - Выстрелить")

                while True:
                    try:
                        action = int(input("Твой выбор: "))

                        if action == 1:
                            if random.randint(1, 100) <= 70:
                                print("Ты увернулся!")
                                score += 10
                            else:
                                print("Маневр не удался!")
                                health -= 30
                            break

                        elif action == 2:
                            if shield > 0:
                                shield -= 1
                                print("Щит заблокировал астероид!")
                                score += 15
                                break
                            else:
                                print("Щита нет! Выбери другое действие.")

                        elif action == 3:
                            if random.randint(1, 100) <= 70:
                                print("Астероид уничтожен!")
                                score += 20
                            else:
                                print("Ты промахнулся!")
                                health -= 20
                            break

                        else:
                            print("Введи число от 1 до 3.")

                    except ValueError:
                        print("Введи число!")

            elif event == 2:
                print("\nТы встретил космический мусор!")
                if random.randint(1, 100) <= 50:
                    print("Ты пролетел мимо!")
                    score += 10
                else:
                    print("Корабль получил повреждения!")
                    health -= 15

            elif event == 3:
                print("\nНайден ремонтный модуль!")
                health += 20
                if health > 100:
                    health = 100
                print("Здоровье восстановлено!")

            else:
                print("\nВ космосе спокойно.")
                score += 5

            turn += 1

        elif choice == 2:
            print("\nСостояние корабля:")
            print("Здоровье:", health)
            print("Заряд щита:", shield)
            print("Набранные очки:", score)

        elif choice == 3:
            print("\nТы покинул игру.")
            break

        else:
            print("Выбери число от 1 до 3.")

    if health <= 0:
        print("\n=== КОРАБЛЬ УНИЧТОЖЕН ===")
        print("Ты продержался ходов:", turn - 1)
        print("Твои очки:", score)

    print("\nНачать новую игру?")
    print("1 - Да")
    print("2 - Нет")

    while True:
        try:
            again = int(input("Твой выбор: "))

            if again == 1:
                break
            elif again == 2:
                print("Спасибо за игру!")
                exit()
            else:
                print("Введи 1 или 2.")

        except ValueError:
            print("Введи число!")



