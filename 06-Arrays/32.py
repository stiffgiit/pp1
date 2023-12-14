number = int(input("Number: "))

def occurs(number, array):
    if number in array:
        print(f"\nResult: number {number} appears in the array")
    else:
        print(f"\nResult: number {number} does not appear in the array")    
    return " "
        
arr = [2,3,4,5,6,7,8]
print("Array: ", *arr, end=" ")
print(occurs(number, arr))