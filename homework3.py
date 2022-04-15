def num(a, b):
    if a == 0:
        return b
    else:
        return num(b % a, a)


class Fraction:
    def __init__(self, numertor, denumerator):
        hcf1 = num(numertor, denumerator)
        self.numertor = numertor // hcf1
        self.denumerator = denumerator // hcf1

    def __str__(self):
        if self.denumerator == 1:
            return str(self.numertor)


        elif self.numertor > self.denumerator:
            return str(self.numertor // self.denumerator) + " " + \
                   str(Fraction(self.numertor % self.denumerator, self.denumerator))

        else:
            return str(self.numertor) + "/" + str(self.denumerator)

    def __add__(self, other):
        new_numertor = self.numertor * other.denumerator + other.numertor * self.denumerator
        new_denumerator = self.denumerator * other.denumerator
        return Fraction(new_numertor, new_denumerator)

    def __sub__(self, other):
        new_numertor = self.numertor * other.denumerator - other.numertor * self.denumerator
        new_denumerator = self.denumerator * other.denumerator
        return Fraction(new_numertor, new_denumerator)

    def __mul__(self, other):
        new_numertor = self.numertor * other.numertor
        new_denumerator = self.denumerator * other.denumerator
        return Fraction(new_numertor, new_denumerator)

    def __floordiv__(self, other):
        new_num = self.numertor // other.denumerator
        new_den = self.denumerator // other.denumerator
        return Fraction(new_num, new_den)


a = Fraction(10, 5)
b = Fraction(14, 7)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
