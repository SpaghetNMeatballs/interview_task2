from ..src.Circle import Circle
from pytest import approx, raises
from math import pi


def test_correct_square():
    a = Circle(r=1.0)
    assert a.square() == approx(pi, 0.1)


def test_lte_zero():
    with raises(AttributeError):
        a = Circle(r=-1.0)
