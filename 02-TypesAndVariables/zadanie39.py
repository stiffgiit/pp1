price = float(input("Enter price: "))
discount = float(input("Enter dicount %: "))

amount = price - (price*(discount/100))
redu = price - amount

print(f"Price with discount: {amount:.2f}")
print(f"Reduction: {redu:.2f}")
