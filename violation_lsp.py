##########################################
# Violates Liskov Substitution Principle #
##########################################

class Shape:
    def area(self) -> float:
        raise NotImplementedError

class Square(Shape):
    def __init__(self, size):
        self.size = size

    def area(self) -> float:
        return self.size * self.size

class BrokenCircle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # LSP violation: overrides area() but violates expectations
    # - Return type is not float
    # - Function changes global state (prints to console)
    # - or throws an error instead of functioning correctly
    def area(self) -> float:
        print("Circles don’t have an area!")  # Unexpected behavior
        return None  # Should be a float

def print_shape_area(shape: Shape):
    # Expects that area() always returns a float value
    print(f"Area: {shape.area()}")

# Usage
shapes = [Square(2), BrokenCircle(3)]
for shape in shapes:
    print_shape_area(shape)
