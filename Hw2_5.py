m_list = [9, 8, 7, 7, 6, 5, 5, 3, 2, 1]
new_number = int(input('Введите новый элемент рейтинга в виде натурального числа - '))
i = 0

for n in m_list:
    if new_number <= n:
        i +=1
    elif new_number > n:
        break
m_list.insert(i, float(new_number))
print(m_list)