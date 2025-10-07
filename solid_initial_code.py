#######################################
# Initial Code Example                #
#######################################

class Shape:
    def area(self) -> float:
        raise NotImplementedError

class Square(Shape):
    def __init__(self, size):
        self.size = size

    def area(self) -> float:
        return self.size * self.size

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius

def print_shape_area(shape):
    print(f"Area: {shape.area()}")

# Usage
shapes = [Square(2), Circle(3)]
for shape in shapes:
    print_shape_area(shape)
