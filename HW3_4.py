def my_pow_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "Ошибка х должен быть больше 0, а у должен быть меньше 0"
        else:
            result = 1
            for _in range(abs(y)):
                result *= 1 / x
            return f' результат возведения х в степень у: {round(result, 6)}'
    except VaueError:
            return 'Программа работает только с числами'

    print(my_pow_func(2, -3))