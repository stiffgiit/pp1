array = [1,2,3,4,5,6,7,8,9]

even = []
odd = []

for element in array:
    if element%2 == 0:
        even.append(element)
    elif element%2 == 1:
        odd.append(element)
        
gen = even + odd

print(gen)