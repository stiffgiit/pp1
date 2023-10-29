a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
p = (a+b+c)/2
area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
circumference = a+b+c
print(f"Triangle area: {area} \n Triangle circumference: {circumference}")
print(p)