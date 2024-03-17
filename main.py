from src.Circle import Circle
from src.Triangle import Triangle

if __name__ == "__main__":
    sides = []
    flag = False
    while not flag:
        try:
            sides = [
                float(i)
                for i in input("Input sides of the shape divided by space: ").split()
            ]
            flag = True
        except ValueError:
            print(
                "Your input could not be processed as it contains symbols that couldn't be processed into floats"
            )
    if len(sides) == 1:
        try:
            circle = Circle(sides[0])
        except AttributeError:
            print("A circle with given radius does not exist")
            exit(1)
        print(
            f"You've entered radius of a circle, it's square is equal to {circle.square()}"
        )
    elif len(sides) == 3:
        try:
            triangle = Triangle(*sides)
        except AttributeError:
            print("A triangle with given sides does not exist")
            exit(1)
        print(
            f"You've entered sides of a {'right ' if triangle.is_right else ''}triangle, it's square is equal to {triangle.square():2}"
        )
    else:
        print("This number of sides is not supported yet")
        exit(1)
