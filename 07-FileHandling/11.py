with open('nigger.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]
    
    
total = sum(numbers)


print("Numbers:", ''.join(map(str, numbers)))
print("Sum:", total)