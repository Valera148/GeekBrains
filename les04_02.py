my_list = [1, 3, 10, 300, 250, 1000, 329]
my_list2 = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num-1]]
print(my_list2)