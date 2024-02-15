"""Factorial using function"""

num = int(input("Enter a number"))


def fact(factorial):
    if num == 0:
        print("Factorial of zero is 1")
    else:
        i = 1
        while i <= num:
            factorial = factorial * i
            i = i + 1
    return factorial


fac = fact(1)
print(fac)
