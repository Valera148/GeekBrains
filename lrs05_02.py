with open('text.txt', 'r', encoding='utf-8') as f_obj:
    n = [f'{line}.{count.strip()} - {len(count.split())} слов' for line, count in enumerate(f_obj, 1)]
    print(*n, f'Всего строк: {len(n)}.', sep='\n')
