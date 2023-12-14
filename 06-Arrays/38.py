array = [1,2,3,4,5,6]

enter = int(input("Enter number:" ))

count = 0

for element in array:
    if element > enter: 
        count += 1
        
print(count)