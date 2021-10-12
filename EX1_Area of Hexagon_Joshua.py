import math

length = float(input("Insert the side length of the hexagon: "))
hexagon = ((3 * math.sqrt(3)) * (length** 2)) / 2

print ("The area of the hexagon with the side length of", length, "is %2.3f"%hexagon)