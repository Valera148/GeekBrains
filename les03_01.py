def my_func(s_1, s_2):
    try:
        sub = s_1/s_2
    except ZeroDivisionError:
           return "Err"
    return round(sub, 2)

print(my_func(int(input('Введите первое значение: ')), int(input('Введите второе значение: '))))
