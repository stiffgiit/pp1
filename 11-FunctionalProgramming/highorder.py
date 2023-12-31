#High order functions
a = "high order functions"
b = a.upper()
print(b)


numbers = [1,2,3,4,5,6,7]
odd = list(filter(lambda x: x%2 == 1, numbers))
print(odd) #output: [1,3,5,7]

from functools import reduce

numbers = [1,2,3,4,5]
product = reduce(lambda x, y: x*y, numbers)
print(product) #output: 120, applies the given function from left to right
                # to reduce the iterable to a single value


numbers = [4,2,7,1,9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

numbers = [0,1,2,3]
has_positive = all(map(lambda x: x > 0, numbers))
print(has_positive) # the all() function returns true or false,
                    # in this example it return false because there is zero

a = 5
square = lambda x: x**2 
print(square(5))