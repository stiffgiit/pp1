def f(arr, num_columns):
    return [arr[i:i+num_columns] for i in range(0, len(arr), num_columns)]


arr = [1,2,3,4,5,6,7,8,9]
num_columns = 3

a2d = f(arr, num_columns)

for row in a2d:
    print(row)
    
    
def conv1d(ar2d):
    return [element for i in ar2d for element in i]


arrajka2d = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

a = conv1d(arrajka2d)

for row in a:
    print(row)