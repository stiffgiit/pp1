decimal = int(input("Enter decimal number: "))

binary = ""
quotient = decimal

while quotient > 0:
    remainder = quotient%2
    binary = str(remainder) + binary
    quotient = quotient//2
    
print(f"{decimal}(10) = {binary}(2)")