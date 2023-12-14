array = [
    [False,True],
    [False,False],
    [True,True]
]

print("Before:", array)

for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = not array[i][j]
    
    
print("After:", array)