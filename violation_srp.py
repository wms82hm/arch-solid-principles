############################################
# Violates Single Responsibility Principle #
############################################

class Shape:
    def area(self) -> float:
        raise NotImplementedError

    def print_area(self):  # <-- New responsibility: output
        print(f"Area: {self.area()}")

class Square(Shape):
    def __init__(self, size):
        self.size = size

    def area(self) -> float:
        return self.size * self.size

    def save_to_file(self, filename):  # <-- Additional responsibility: file handling
        with open(filename, "w") as f:
            f.write(f"Square with size {self.size}, area = {self.area()}\n")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius

    def print_details(self):  # <-- Mixing calculation and presentation
        print(f"Circle radius: {self.radius}, area: {self.area()}")

# Usage
shapes = [Square(2), Circle(3)]
for shape in shapes:
    shape.print_area()  # Output is part of the class (SRP violation)
