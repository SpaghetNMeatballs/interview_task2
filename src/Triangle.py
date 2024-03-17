from .ShapesInterface import Shape
from math import sqrt


class Triangle(Shape):
    sides = []
    is_right = False

    def __init__(self, a: float, b: float, c: float):
        self.sides = [a, b, c]
        self.sides.sort()
        if a + b <= c or not all([i > 0 for i in self.sides]):
            raise AttributeError("Triangle has invalid sides")
        self.is_right = self.sides[0] ** 2 + self.sides[1] ** 2 == self.sides[2] ** 2

    def square(self) -> float:
        if self.is_right:
            return (self.sides[0] * self.sides[1]) / 2

        s = sum(self.sides) / 2
        result = s
        for i in self.sides:
            result *= s - i
        return sqrt(result)
