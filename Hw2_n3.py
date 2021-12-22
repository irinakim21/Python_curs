season = {'spring': (3, 4, 5), 'summer': (6, 7, 8), 'autumn': (9, 10, 11), 'winter': (1, 2, 12)}
month = int(input('Введите номер месяца- '))
if month < 1 or month > 12:
    raise ValueError("Неверный номер месяца")
for key in se3-ей задачеason.keys():
    if month in season[key]:
        print(key)
