sum_of_numbers = 0
count = 0

while True:
    try:
        number = float(input("Enter a number: "))
        if number== 0:
            break
        sum_of_numbers += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
        
if count > 0:
    mean = sum_of_numbers / count
else:
    mean = 0
    
print(f"RESULT: Quantity={count}, Sum={sum_of_numbers:.0f}, Mean={mean:.0f}")