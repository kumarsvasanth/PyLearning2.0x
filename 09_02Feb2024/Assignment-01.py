""" Create a program that determines whether a given
year is a leap year
A leap year is divisible by 4 ,but not by 100
unless it is also divisible by 400
Use an if-else statement to make this determination

Input = 2024
Output = Leap Year"""

year = 2004
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a leap year")
