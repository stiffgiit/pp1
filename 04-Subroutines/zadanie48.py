def f(product_code):
    
    three_digits = product_code[:3]
    control = int(product_code[3])
    remainder = sum(int(digit) for digit in three_digits) % 7
    
    return remainder == control

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))