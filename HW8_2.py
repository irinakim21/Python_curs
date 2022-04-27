class ImpossibleNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator


def divide_null(divider, denominator):
    try:
        return divider / denominator
    except:
        return f"Деление на ноль недопустимо"


div = ImpossibleNull(10, 100)
print(ImpossibleNull.divide_null(10, 0))
print(ImpossibleNull.divide_null(10, 0.1))
print(div.impossible_null(100, 0))
