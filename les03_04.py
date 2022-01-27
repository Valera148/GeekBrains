def my_func(x=1, y=-1):
    try:
       sub = x**y
    except TypeError:
       return 'Вводите только числа'
    return sub
print(my_func(float(input('Введите первое значение: ')), int(input('Введите второе отрицательное значение: '))))