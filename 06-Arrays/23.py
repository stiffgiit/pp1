array = [-15, 8, -31, 47, -2, 19]

max_element = array[0]
min_element = array[0]


for element in array:
    if element > max_element:
        max_element = element
    elif element < min_element:
        min_element = element
        
  
print(max_element)
print(min_element)