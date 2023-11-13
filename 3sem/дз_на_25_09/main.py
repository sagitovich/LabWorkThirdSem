import random
n = random.randint(1, 100)

while True:

    print('\n', f'Ваше число: {n}')

    if not n == 0:
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)

        print('Выберете одно из трёх действий: ', '\n',
        f'1) Увеличить число на {a}', '\n',
        f'2) Уменьшить число на {b}', '\n',
        f'3) Завершить игру')
        choise = int(input('Ваш выбор: '))
            
        if choise == 1:
            n += a
        elif choise == 2:
            n -= b
        elif choise == 3:
            print('Что ж, очень жаль...')
            exit()
        

    else:
        print('Поздравляю! Вы прошли игру!')
        exit()

