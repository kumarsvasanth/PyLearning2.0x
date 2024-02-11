""" Create a program that determines whether a given
year is a leap year
A leap year is divisible by 4 ,but not by 100
unless it is also divisible by 400
Use an if-else statement to make this determination

Input = 2024
Output = Leap Year"""

year = 2024
if year % 4 == 0:
    print("2024 is a Leap Year")
elif year % 100 == 0 and year % 400 == 0:
    print("2024 is a Leap Year")
else:
    print("2024 is not a leap year")