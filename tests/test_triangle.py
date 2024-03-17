from ..src.Triangle import Triangle
from pytest import approx, raises
from math import pi


def test_correct_square():
    a = Triangle(a=45.0, b=20.0, c=30.0)
    assert not a.is_right
    assert a.square() == approx(239.05, 0.1)


def test_right_triangle():
    a = Triangle(a=3.0, b=4.0, c=5.0)
    assert a.is_right
    assert a.square() == approx(6.0, 0.1)


def test_impossible_sides():
    with raises(AttributeError):
        a = Triangle(0.0, -10.0, 20.0)
    with raises(AttributeError):
        a = Triangle(4, 5, 9)
