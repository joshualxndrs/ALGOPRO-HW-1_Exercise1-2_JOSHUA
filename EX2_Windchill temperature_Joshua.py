import math

ta = float(input("Input temperature in Fahrenheit: "))

while ta < -58 or ta > 41 :
    print("Temperature should be between -58F and 41 F")
    ta = eval(input("Input temperature in Fahrenheit: "))

v = float(input("Input the wind speed in miles/hour: "))

while v < 2:
    print("The speed should be > or = 2 .")
    v = float(input("Input the wind speed in miles/hour: "))

final_product = 35.74 + (0.6215 * ta) - (35.75 * pow(v,0.16)) + 0.4275 * ta * pow(v,0.16)
print("The wind chill index is %2.3f"%final_product)