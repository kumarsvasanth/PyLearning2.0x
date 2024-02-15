"""
Write a program that classifies a triangle based on its side lengths

Given three input values representing the lengths of the sides,
determine if the triangle is equilateral(all the sides are equal),
isosceles(2 sides are equal) or scalene(no sides are equal)

use an if-else statement to classify the triangle"""
side1 = int(input("enter side1"))
side2 = int(input("enter side2"))
side3 = int(input("enter side3"))

if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
