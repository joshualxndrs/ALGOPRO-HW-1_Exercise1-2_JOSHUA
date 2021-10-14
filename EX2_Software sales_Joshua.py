price = 99.00

package_quantity = float(input("Enter the number of packages purchased: "))

if package_quantity < 0:
    print("Quantity of package should be greater than 0.")
else:
    discount = 0

    if package_quantity < 10:
        discount = 0
    elif package_quantity >= 10 and package_quantity <= 19:
        discount = .10
    elif package_quantity >= 20 and package_quantity <= 49:
        discount = .20
    elif package_quantity >= 50 and package_quantity <= 99:
        discount = .30
    elif package_quantity >= 100:
         discount = .40

    total_package = package_quantity * price
    discount_amount = total_package * discount
    grandtotal = total_package - discount_amount
    display = "Total package = $%2.2f"%package_quantity + \
              "\nDiscount Percentage = " + format(discount, '.0%') + \
              "\nDiscount amount = $%2.2f"%discount_amount + \
              "\nGrand total  = $%2.2f"%grandtotal
print ("\n" + display + "\n")