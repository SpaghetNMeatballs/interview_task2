from .ShapesInterface import Shape
from math import pi


class Circle(Shape):
    def __init__(self, r: float):
        if r <= 0:
            raise AttributeError("Radius must be greater than zero")
        self.r = r

    def square(self) -> float:
        return pi * self.r ** 2
