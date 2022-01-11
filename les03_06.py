def my_func():
    for word in input('Введите слово с маленькой буквы: ').split():
        chars = 0
        for char in word:
            if 1072 <= ord(char) <= 1103:
                chars += 1
        print(word.title() if chars == len(word) else f'{word} - только русские маленькие буквы')
my_func()

