v = float(input("Enter the take of speed in m/s: "))
a = float(input("Enter the take of speed in m/s**2: "))

length_of_runway = (v**2) / (2*a)
print("The minimum runway length for the airplane is %2.4f"%length_of_runway)