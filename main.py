from abc import ABC, abstractmethod

# Abstraction
class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

# Implementations
class SquareRenderer:
    def render(self):
        return "Drawing a square"

class CircleRenderer:
    def render(self):
        return "Drawing a circle"

# Refined Abstractions
class Square(Shape):
    def draw(self):
        return self.renderer.render()

class Circle(Shape):
    def draw(self):
        return self.renderer.render()

# Usage
if __name__ == "__main__":
    square = Square(SquareRenderer())
    print(square.draw())  # Output: Drawing a square

    circle = Circle(CircleRenderer())
    print(circle.draw())  # Output: Drawing a circle
