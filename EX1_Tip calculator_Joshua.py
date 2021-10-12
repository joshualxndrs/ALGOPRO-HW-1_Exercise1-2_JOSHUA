subtotal = float((input("Enter the sub-total : $")))
tip_amount = float(input("Enter tip amount (in %) : "))
tip = (tip_amount/100)*subtotal
total = subtotal+tip

print ("Sub-total: $%2.2f"%subtotal)
print ("Tip: $%2.2f"%tip)
print ("Total: $%2.2f"%total)