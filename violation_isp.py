############################################
# Violates Interface Segregation Principle #
############################################

class Shape:
    def area(self) -> float:
        raise NotImplementedError

    def volume(self) -> float:  # <-- New, inappropriate method for 2D shapes
        raise NotImplementedError

    def perimeter(self) -> float:  # <-- Also unnecessary for some shapes
        raise NotImplementedError


class Square(Shape):
    def __init__(self, size):
        self.size = size

    def area(self) -> float:
        return self.size * self.size

    def volume(self) -> float:
        # Square has no volume – but still must implement
        raise NotImplementedError("Square has no volume!")

    def perimeter(self) -> float:
        return 4 * self.size


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius

    def volume(self) -> float:
        # Circle is 2D, no volume – unnecessarily forced
        raise NotImplementedError("Circle has no volume!")

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius


def print_shape_area(shape):
    print(f"Area: {shape.area()}")


# Usage
shapes = [Square(2), Circle(3)]
for shape in shapes:
    print_shape_area(shape)
