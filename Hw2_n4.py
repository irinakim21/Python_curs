m_str = input("Введите строку")
m_List = []
num = 1
for elem in range(m_str.count(" ") + 1):
    m_List = m_str.split()
    if len(str(m_List)) <= 10:
        print(f"{num} {m_List[elem]}")
        num += 1
    else:
        print(f"{num} {m_List[elem][0:10]}")
        num += 1