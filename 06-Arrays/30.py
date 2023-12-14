arr = [3,2,4,1,5]

def bubblesort(array):
    n = len(array)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                
bubblesort(arr)

print("Sorted array:", arr)