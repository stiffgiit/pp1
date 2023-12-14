import random
def rand_elem(array):
    return random.choices(array, k=3)


arr = [1,2,3,4,5,6]

print(rand_elem(arr))