from abc import ABC, abstractmethod
import math

# --- Element Hierarchy (Stable data classes) ---

class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: 'Visitor'):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor: 'Visitor'):
        return visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor: 'Visitor'):
        return visitor.visit_rectangle(self)


# --- Visitors (New operation logic isolated here) ---

class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: 'Circle'):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: 'Rectangle'):
        pass

class JSONExportVisitor:
    def visit_circle(self, circle: 'Circle'):
        return f'{{"type": "Circle", "radius": {circle.radius}}}'

    def visit_rectangle(self, rectangle: 'Rectangle'):
        return f'{{"type": "Rectangle", "width": {rectangle.width}, "height": {rectangle.height}}}'


class AreaCalculatorVisitor:
    def visit_circle(self, circle: 'Circle'):
        return math.pi * circle.radius * circle.radius

    def visit_rectangle(self, rectangle: 'Rectangle'):
        return rectangle.width * rectangle.height


# --- Client Code ---
if __name__ == "__main__":

    # Define shapes 
    shapes = [Circle(5), Rectangle(10, 20)]

    # 1. Apply JSON visitor on shapes
    print("--- JSON repr of shapes ---")
    json_visitor = JSONExportVisitor()
    for shape in shapes:
        print(shape.accept(json_visitor))

    # 2. Apply area calculator visitor on shapes
    print("\n--- Area of shapes ---")
    area_visitor = AreaCalculatorVisitor()
    for shape in shapes:
        print(shape.accept(area_visitor))


