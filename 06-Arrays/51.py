array = [
    [1, 2, 3, 4 ,5],
    [6,4,4,4,4],
    [9,9,9,9,9]
]

def f(arr, row1, row2):
    arr[row1], arr[row2] = arr[row2], arr[row1]
    
    
f(array, 0, 2)

for i in array:
    print(i)
