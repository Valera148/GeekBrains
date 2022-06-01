with open('text.txt', 'w', encoding=utf-8) as f_obj:
    while True:
        line = ('Введите строку или оставьте её пустой для завершения программы: ')
        if not line:
            break
            print(line, file=f_obj)

