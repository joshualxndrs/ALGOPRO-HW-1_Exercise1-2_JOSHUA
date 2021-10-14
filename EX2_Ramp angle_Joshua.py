#Input mass, Input Force
#C = 9.8
#Formula for angle --> angle = f/(m*c)
#Asin(angle) --> degrees

import math

m = float(input("Please enter the mass of the cart (unit in kg): "))
f = float(input("Please enter the force acting on the cart (unit in N): "))
c = 9.8

angle = f/(m*c)

A = math.asin(angle)
Final = math.degrees(A)
print("The angle of the ramp is %2.1f"%Final)
