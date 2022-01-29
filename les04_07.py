def my_func(num):
    n = 1
    for i in range(num+1):
        yield f'{i}! = {n}'
        n *= i + 1
for el in my_func(int(input('Введите значение: '))):
    print(el)
