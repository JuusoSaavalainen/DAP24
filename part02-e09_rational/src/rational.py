#!/usr/bin/env python3

class Rational(object):
    def __init__(self, integer1, integer2):
        self.rnum1 = integer1
        self.rnum2 = integer2

    def __str__(self):
        return str(f'{self.rnum1}/{self.rnum2}')

    def __mul__(self, other: object):
        y = self.rnum1 * other.rnum1
        a = self.rnum2 * other.rnum2
        return (Rational(y, a))

    def __truediv__(self, other: object):
        y = self.rnum1 * other.rnum2
        a = self.rnum2 * other.rnum1
        return (Rational(y, a))

    def __add__(self, other: object):
        y = (self.rnum1 * other.rnum2) + (other.rnum1 * self.rnum2)
        a = self.rnum2 * other.rnum2
        return (Rational(y, a))

    def __sub__(self, other: object):
        y = (self.rnum1 * other.rnum2) - (other.rnum1 * self.rnum2)
        a = self.rnum2 * other.rnum2
        return (Rational(y, a))

    def __eq__(self, other: object):
        y = (self.rnum1 * other.rnum2) - (other.rnum1 * self.rnum2)
        return (y == 0)

    def __gt__(self, other: object):
        y = (self.rnum1 * other.rnum2) - (other.rnum1 * self.rnum2)
        return (y > 0)

    def __lt__(self, other: object):
        y = (self.rnum1 * other.rnum2) - (other.rnum1 * self.rnum2)
        return (y < 0)


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
