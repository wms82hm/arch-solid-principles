###########################################
# Violates Dependency Inversion Principle #
###########################################

# Concrete detail (low level)
class ConsolePrinter:
    def print(self, msg: str):
        print(msg)

class Shape:
    # Abstraction depends on a concrete detail -> DIP violation
    def __init__(self):
        self._printer = ConsolePrinter()  # Dependency on low level

    def area(self) -> float:
        raise NotImplementedError

    def log(self, msg: str):
        # Abstraction uses concrete logger directly
        self._printer.print(f"[ShapeLog] {msg}")

class Square(Shape):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def area(self) -> float:
        a = self.size * self.size
        self.log(f"Square area computed: {a}")  # uses concrete logger
        return a

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self) -> float:
        a = 3.14 * self.radius * self.radius
        self.log(f"Circle area computed: {a}")  # uses concrete logger
        return a

# High-level module that depends on concrete details -> DIP violation
class AreaReporter:
    def __init__(self):
        self.printer = ConsolePrinter()  # direct coupling to concrete output

    def report(self, shape_type: str, value: float):
        # High level chooses concrete implementations
        if shape_type == "square":
            shape = Square(value)
        elif shape_type == "circle":
            shape = Circle(value)
        else:
            # This high-level module must be changed for new shapes
            raise ValueError("Unsupported shape type")

        self.printer.print(f"Area: {shape.area()}")

# Original function ignores the abstraction principle and
# uses the concrete reporter (and thus concrete details).
def print_shape_area(shape):
    # no longer used; kept only to show the change
    print(f"Area: {shape.area()}")

# Usage (high level depends on concrete classes and I/O)
reporter = AreaReporter()
reporter.report("square", 2)
reporter.report("circle", 3)
