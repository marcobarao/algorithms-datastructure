from __future__ import division
from math import gcd

class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        if self.numer == 0 and other.numer == 0:
            return True
        
        if not (self.numer == other.numer and self.denom == other.denom):
            if self.denom < 0 and self.numer < 0:
                self.denom = abs(self.denom)
                self.numer = abs(self.numer)
            elif self.denom < 0:
                self.denom = abs(self.denom)
                self.numer = -self.numer

            _gcd = float('inf')
            while _gcd > 1:
                _gcd = gcd(self.numer, self.denom)
                self.numer = self.numer // _gcd
                self.denom = self.denom // _gcd

        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

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

    def __abs__(self):
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)
        return self

    def __pow__(self, power):
        if power < 0:
            self.numer = self.denom ** abs(power)
            self.denom = self.numer ** abs(power)
            return self
        self.numer = self.numer ** power
        self.denom = self.denom ** power
        return self

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
