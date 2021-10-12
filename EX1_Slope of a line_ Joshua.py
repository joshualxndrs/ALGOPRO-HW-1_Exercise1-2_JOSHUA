print("Hello, welcome to the slope calculator, please follow the steps below...")

x1 = float(input("Enter the number for X1: "))
x2 = float(input("Enter the number for X2: "))
y1 = float(input("Enter the number for Y1: "))
y2 = float(input("Enter the number for Y2: "))

slope = (y2-y1) / (x2-x1)

print("The slope of the line that connects two of the points", (x1,y1), "and", (x2,y2), "is", round(slope,5))