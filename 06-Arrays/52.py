array = [
    [5,1,1,1,9],
    [2,2,2,2,4],
    [7,3,3,3,6]
]

def f(arr, col1, col2):
    for row in arr:
        row[col1], row[col2] = row[col2], row[col1]
    
    
f(array, 0, 4)

for i in array:
    print(i)