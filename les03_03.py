def my_func(s_1, s_2, s_3):
    my_list = [s_1, s_2, s_3]
    try:
       my_list.remove(min(my_list))
    except TypeError:
       return 'Вводите только числа'
    return sum(my_list)

print(my_func(int(input('Введите первое значение: ')), int(input('Введите второе значение: ')),
              int(input('Введите третье значение: ')), ))

