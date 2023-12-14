array = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(array)):
    array[i][i] = 1
    
for row in array:
    for val in row:
        print(val, end=" ")
    print()