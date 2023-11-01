current = float(input("Current product price: "))
previous = float(input("Previous product price: "))
print("Buy the product!!")
reduction = previous - current
if reduction >= 10:
    print(f"Product price reduced by {reduction:.0f}% ")