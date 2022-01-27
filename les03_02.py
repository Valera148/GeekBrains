def my_func(name, surname, birthday, city, email, phone):
    return f'Имя: {name}, Фамилия: {surname}, Дата рождения: {birthday}, город проживания: {city}, ' \
           f'Электронная почта: {email}, Телефон: {phone}'

print(my_func(surname=input('Введите фамилию: '), name=input('Введите имя: '),
              birthday=input('Введите год рождения: '),
               city=input('город проживания: '), email=input('Введите email: '),
              phone=input('Введите телефон: '),))