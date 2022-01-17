class Clothers:
    def __init__(self, width, dlina):
        self.width = width
        self.dlina = dlina

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.dlina * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Spending full cloth \n'
                   f' {(self.width / 6.5 + 0.5) + (self.dlina * 2 + 0.3)}')


class Coat(Clothers):
    def __init__(self, width, dlina):
        super().__init__(width, dlina)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'spending coat {self.square_c}'


class Jacket(Clothers):
    def __init__(self, width, dlina):
        super().__init__(width, dlina)
        self.square_j = round(self.dlina * 2 + 0.3)

    def __str__(self):
        return f'spending jacket {self.square_j}'


coat = Coat(4, 80)
jacket = Jacket(2, 6)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square_c())
print(jacket.get_square_j())
