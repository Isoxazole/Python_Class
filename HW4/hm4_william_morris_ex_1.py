"""
Homework 4, Exercise 1
William Morris
2/22/19
This program has 3 classes: Rectangle, Circle, and Square. Each class has the
functions to get the Area, Diagonal, and perimeter of their respective shape.
At the end of this program, the perimeter of a circle with radius the half of the diagonal of a
rectangle with length 20 and width 10 is calculated
"""
import math
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getArea(self):
        return self.width * self.length

    def getDiagonal(self):
        return math.sqrt(self.length ** 2 + self.width **2)

    def getPerimeter(self):
        return 2 * self.length + 2 * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def getDiagonal(self):
        return self.radius * 2

    def getPerimeter(self):
        return self.radius * 2 * math.pi

class Square:
    def __index__(self, side_length):
        self.side_length = side_length

    def getArea(self):
        return self.side_length **2

    def getDiagonal(self):
        return math.sqrt(self.length ** 2 + self.width ** 2)

    def getPerimeter(self):
        return 4 * self.side_length


length = 20
width = 10

rectangle = Rectangle(length, width)

radius = rectangle.getDiagonal() / 2

circle = Circle(radius)

perimeter = circle.getPerimeter()

print(perimeter)


