#Write a program to create a class called Shape with methods called getPerimeter() and
getArea(). Create a subclass called Circle that overrides the getPerimeter() and getArea() 
methods to calculate the area and perimeter of a circle.(use abstract classes and methods)

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    
    @abstractmethod
    def getPerimeter(self):
        pass
    
    @abstractmethod
    def getArea(self):
        pass


class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def getPerimeter(self):
        return 2 * math.pi * self.radius
    
    def getArea(self):
        return math.pi * (self.radius ** 2)


radius = 5
circle = Circle(radius)
print(f"Circle with radius {radius}")
print(f"Perimeter: {circle.getPerimeter()}")
print(f"Area: {circle.getArea()}")