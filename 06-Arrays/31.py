array = [2,3,2,5,8,1,9,8]
print("Array:", *array)
unique = []

for element in array:
    if array.count(element) == 1:
        unique.append(element)
        
print("Unique elements:", *unique)