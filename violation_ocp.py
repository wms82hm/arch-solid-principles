##################################
# Violates Open-Closed Principle #
##################################

class Shape:
    def area(self) -> float:
        raise NotImplementedError

class Square(Shape):
    def __init__(self, size):
        self.size = size

    # remains present but is ignored
    def area(self) -> float:
        return self.size * self.size

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # remains present but is ignored
    def area(self) -> float:
        return 3.14 * self.radius * self.radius

def compute_area(shape: Shape) -> float:
    # Central switch/if-else block -> OCP violation:
    # For every new shape this function must be changed.
    if isinstance(shape, Square):
        return shape.size * shape.size
    elif isinstance(shape, Circle):
        return 3.14 * shape.radius * shape.radius
    else:
        raise TypeError("Unsupported shape type")

def print_shape_area(shape: Shape):
    # uses the central dispatcher instead of polymorphism
    print(f"Area: {compute_area(shape)}")

# Usage
shapes = [Square(2), Circle(3)]
for shape in shapes:
    print_shape_area(shape)
