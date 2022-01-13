with open('1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('введите новую строку - ')
        is not line:
            break
        f.write(f'{line}\n')
