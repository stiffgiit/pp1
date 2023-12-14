array = [
    [-38,19],
    [5,40],
    [-7,11],
    [29,16]
]

min_element = array[0][0]
max_element = array[0][0]
max_row = 0
min_row = 0
max_col = 0
min_col = 0

for i in range(len(array)):
    for j in range(len(array[0])):
        if array[i][j] > max_element:
            max_element = array[i][j]
            max_row = i
            max_col = j
        elif array[i][j] < min_element:
            min_element = array[i][j]
            min_row = i
            min_col = j
            
a = max_element, (max_row, max_col),  min_element, (min_row, min_col)

print(f"The max, and min elements are {a}")