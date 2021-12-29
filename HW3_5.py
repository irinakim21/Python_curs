def sum_num():
    s = 0
    while True:
        in_list = input('Введите числа или Q для входа: ').split()
        for num in in_list:
            if num == 'q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    priint('Чтобы выйти из программы нажмите q-')
        print(f'Сумма числе = {s}')
print(sum_num())

