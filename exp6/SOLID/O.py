# O: Open/Closed Principle
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius**2)


# New shapes can be added without modifying existing code
shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print(shape.area())
