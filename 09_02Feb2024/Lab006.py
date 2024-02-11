for i in range(2, 10, 2):
    print("Hello Vasanth", i)

"""write a program that calculates and displays the letter grade for a given numeric score
(e.g. A,B,C,D,E,F)
Based on the following grade scale:
input - score - 89
output - B
#A: 90-100
#B: 80 -89
#C: 70 -79
#D: 60- 69
#E : 0-59
"""

scale = int(input("Enter the marks"))

if 100 >= scale >= 90:
    print("The Grade is A")
elif (scale <= 89) and (scale >= 80):
    print("The Grade is B")
elif (scale <= 79) and (scale >= 70):
    print("The Grade is C")
elif (scale <= 69) and (scale >= 60):
    print("The Grade is D")
elif scale<=59 and scale>=0:
    print("The Grade is E")
else:
    print("Invalid input")
