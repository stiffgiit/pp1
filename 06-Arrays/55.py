array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


arrajka = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]




def f(n):
    transpose = [[n[j][i] for j in range(len(n))] for i in range(len(n[0]))]
    return transpose


def display(arr):
    for i in arr:
        for element in i:
            print(element, end=" ")
        print()
        
display(f(arrajka))
