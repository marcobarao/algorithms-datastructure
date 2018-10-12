class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __repr__(self):
        no_refactor = "{}/{}".format(self.numer, self.denom)

        numer = 0
        denom = 0
        c = 0

        if self.numer == 0:
            return 1

        if self.denom > self.numer:
            numer = self.denom
            denom = self.numer
        else:
            denom = self.denom
            numer = self.numer

        while(numer % denom != 0):
            c = numer % denom
            numer = denom
            denom = c

        self.numer = int(self.numer / denom)
        self.denom = int(self.denom / denom)

        if self.denom < 0 and self.numer < 0:
            self.denom = abs(self.denom)
            self.numer = abs(self.numer)
        elif self.denom < 0:
            self.denom = abs(self.denom)
            self.numer = -self.numer

        return no_refactor, "{}/{}".format(self.numer, self.denom)

    def __str__(self):
        nr, r = self.__repr__()
        return "{0} = {1}".format(nr, r)

    def __add__(self, other):
        self.numer = self.numer * other.denom + other.numer * self.denom
        self.denom = self.denom * other.denom
        return self

    def __sub__(self, other):
        self.numer = self.numer * other.denom - other.numer * self.denom
        self.denom = self.denom * other.denom
        return self

    def __mul__(self, other):
        self.numer = self.numer * other.numer
        self.denom = self.denom * other.denom
        return self

    def __truediv__(self, other):
        if self.denom and other.numer:
            self.numer = self.numer * other.denom
            self.denom = other.numer * self.denom
            return self
        raise ZeroDivisionError("division by zero")


n = int(input())

for _ in range(n):
    inp = input().split()
    fr = Rational(int(inp[0]), int(inp[2]))
    sr = Rational(int(inp[4]), int(inp[6]))
    if inp[3] == '+':
        result = fr + sr
    elif inp[3] == '-':
        result = fr - sr
    elif inp[3] == '*':
        result = fr * sr
    else:
        result = fr / sr
    
    print(result)

