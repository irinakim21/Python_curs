def aver_check(x, y):
    try:
        x, y = int(x), int(y)
        z = x / y
        return z
    except ZeroDivisionError:
        return "на ноль нельзя делить"
    except ValueError:
        return 'введите числа'

print(aver_check(input("введите общую сумму  x = "), input("введите общее количество покупок y = ")))