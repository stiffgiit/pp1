products = int(input("Number of products purchased: "))
price = int(input("Product price: "))
if products <= 2:
    result = products * price
else:
    result = products * (price * 0.75) + 20

print(f"Amount to pay: {result:.2f}")