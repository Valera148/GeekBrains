from random import randint
my_list = [randint(10, 30) for _ in range(20)]
new_list = [n for n in my_list if my_list.count(n) == 1]
print(f'Отсортированный список: {new_list}')
