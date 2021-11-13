from class1 import *

ch = input("inset Geometric shape parameters > c(circle) - sr(square)&(rectangle) - t(triangle)")

if ch == 'c':
    r = float(input("Enter Circle Radius: "))
    circle = Circle(r)
    print("Area of Circle:", "%.2f" % circle.getArea())
    print("Circumference of Circle:", "%.2f" % circle.getCircumference())

elif ch == 'sr':
    print("Enter length and width:")
    length = float(input())
    width = float(input())
    square = Square(length, width)
    print("Area of Square:", "%.2f" % square.getArea())
    print("Circumference of Square:", "%.2f" % square.getCircumference())

    print("#########################")
    rectangle = Rectangle(length, width)
    print("Area of Rectangle:", "%.2f" % rectangle.getArea())
    print("Circumference of Rectangle:", "%.2f" % rectangle.getCircumference())

elif ch == 't':
    s1 = float(input("Enter the first side of the triangle : "))
    s2 = float(input("Enter the second side of the triangle : "))
    s3 = float(input("Enter the third side of the triangle : "))

    triangle = Triangle(s1, s2, s3)
    print("Area of triangle:", "%.2f" % triangle.getArea())
    print("Circumference of triangle:", "%.2f" % triangle.getCircumference())


