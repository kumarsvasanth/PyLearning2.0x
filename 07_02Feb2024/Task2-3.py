"""Develop a Python script that calculates the
 square and cube of a given number"""
import math

num = 10
"""square = num**2
cube = num**3
print(f"Square of a number 10 is {square}")
print(f"Cube of a number 10 is {cube}")"""

# OR

square = pow(num, 2)
#cube = pow(num, 3)
cube = math.pow(num,2)
print("Square of a number 10 is ", square)
print("Cube of a number 10 is ", cube)


