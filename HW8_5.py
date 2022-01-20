class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = '(a + b) / i'

    def __add__(self, other):
        print(f'Сумма x1 и x2 равна')
        return f'x = {self.a + other.a} + {self.b + other.b} / i'

    def __mul__(self, other):
        print(f'Произведение x1 и x2 равно')
        return f'z = {self.a * other.a + (self.b * other.b)} - {self.b * other.a} / i'

    def __str__(self):
        return f'x = {self.a} + {self.b} / i'


x_1 = ComplexNumber(3, -4)
x_2 = ComplexNumber(1, 14)
print(x_1)
print(x_1 + x_2)
print(x_1 / x_2)
