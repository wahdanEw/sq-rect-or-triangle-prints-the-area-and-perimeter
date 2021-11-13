import math


class GeometricShape:
    def __init__(self, radius):
        self.__radius = radius

    def setRadius(self, usr_input):
        self.__radius = usr_input
    def getRadius(self):
        return self.__radius


class Circle(GeometricShape):
    def getArea(self):
        global pi
        pi = float("%.2f" % (math.pi))
        return pi * Circle.getRadius(self) * Circle.getRadius(self)

    def getCircumference(self):
        return 2 * pi * Circle.getRadius(self)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def setLength(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def getArea(self):
        return self.getLength() * self.getWidth()

    def getCircumference(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def getArea(self):
        return Square.getLength(self) * Square.getLength(self)

    def getCircumference(self):
        return 4 * Square.getLength(self)


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        # calculate the area
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def getCircumference(self):
        return self.side1 + self.side2 + self.side3
