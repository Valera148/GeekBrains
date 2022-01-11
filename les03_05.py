def my_func():
    s = 0
    while True:
        list = (input('Введите числа через запятую: ')).split()
        for n in list:
            if n.lower() == 'q':
                return s
            else:
                try:
                    s += int(n)
                except ValueError:
                    print('Если хотите выйти, введите "q"')
    print('Сумма введенных чисел равна: {s}')

print(my_func())

