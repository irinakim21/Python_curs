elem_count = int(input("Введите количество элементов списка "))
m_List = []
i = 0
elem = 0
while i < elem_count:
    m_List.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_List)/2)):
        m_List[elem], m_List[elem + 1] = m_List [elem + 1], m_List[elem]
        elem += 2
print(m_List)