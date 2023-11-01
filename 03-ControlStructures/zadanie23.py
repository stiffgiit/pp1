age = int(input("Enter the dog's age in human years: "))
if age <= 2:
    num = age * 10.5
else:
    num = 2 * 10.5 + (age - 2) * 4

print(f"The dog's age in dog's years is {num:.0f} years")