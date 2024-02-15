"""Factorial of a number
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24"""

"""n = int(input("Enter a number"))
factorial = math.factorial(n)
print(factorial)"""

# or
n = int(input("Enter the number to find the factorial: "))
factorial = 1
if n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
print(f"The factorial of number is: ", factorial)
