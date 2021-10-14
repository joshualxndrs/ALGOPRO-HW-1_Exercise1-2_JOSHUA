def checkValidity(a, b, c):

    if (a + b <= c) or (a + c <= b) or (b + c <= a ):
        return False
    else:
        return True

a = float(input("Please enter edge1: "))
b = float(input("Please enter edge2: "))
c = float(input("Please enter edge3: "))

if checkValidity(a, b, c):
    print("This is a valid triangle.")
    P = a + b + c
    print("The perimeter for this triangle is ", P)
else:
    print("ERROR. Perimeter could not be calculated.")