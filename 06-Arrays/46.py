array = [
    [1,2,3,4],
    [5,6,7,8]
]
'''
for row in array:
    print(*row)
    '''
    
for row in array:
    for element in row:
        print(element, end="\t")
    print()