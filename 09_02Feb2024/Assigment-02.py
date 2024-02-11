side1 = int(input("enter 1st length"))
side2 = int(input("enter 2nd length"))
side3 = int(input("enter 3rd length"))

if side1 == side2 == side3:
    print("Equivalent triangle")
elif side1 == side2 and side1 != side3:
    print("Isosceles triangle")
elif side2 == side3 and side2 != side1:
    print("Isosceles triangle")
elif side3 == side1 and side3 != side2:
    print("Isosceles triangle")
else:
    print("no sides are equal")
